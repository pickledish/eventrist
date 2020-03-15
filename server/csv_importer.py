import argparse
import csv
import datetime
import re
import json
import yaml

import requests

ROOT_URL = "http://127.0.0.1:8000"

def send_to_influx(source, row, dry_run):
	"""
	"""
	special_params = {"name": source.get("event_name")}

	date_field_name = source.get("event_date_field")
	date_field_value = row.pop(date_field_name, default=None)

	if date_field_name is None:
		print("Source does not have date field defined, events will have current time")
	elif date_field_value is None:
		print(f"Row does not contain date field {date_field_name}, will use current time")
	else:
		date_object = datetime.datetime.strptime(date_field_value, "%Y-%m-%d")
		special_params['time'] = int(date_object.timestamp() * 1000)

	value_field_name = source.get("event_value_field")
	value_field_value = row.pop(value_field_name, default=None)

	if value_field_name is None:
		print("Source does not have value field defined, events will have value 1.0")
	elif value_field_value is None:
		print(f"Row does not contain value field {value_field_name}, will use 1.0")
	else:
		fixed_value = re.sub(r'[^0-9\.-]', '', value_field_value)
		special_params['value'] = float(fixed_value)

	request = {**row, **special_params}

	if dry_run:
		print(request)
	else:
		requests.post(f"{ROOT_URL}/stream/{source.get('stream_id')}/write", json=request)


def main(input_file, source_name, dry_run):
	"""
	"""
	# TODO: actually keep this account-level info in some persistent db! Hah
	account_config = yaml.safe_load(open("account.yaml"))

	source = account_config.get("sources", {}).get(source_name)

	if source is None:
		raise Exception(f"Source with name {source_name} not found in user config")

	if source.get("source_type") != "csv":
		raise Exception(f"Source {source_name} has type {source.get('source_type')}, not CSV")

	input_location = input_file if input_file != "=" else "/dev/stdin"

	with open(input_location, mode='r', encoding='utf-8-sig') as file_obj:
		reader = csv.DictReader(file_obj)
		for row in reader:
			send_to_influx(source, row, dry_run)


def get_parser():
	"""
	"""
	parser = argparse.ArgumentParser(description="Given a source and a file, imports CSV")
	parser.add_argument("-f", "--input-file", help="File to import, or '-' for stdin", required=True)
	parser.add_argument("-s", "--source-name", help="Name of (existing) source mapper", required=True)
	parser.add_argument("--dry-run", help="Just print, don't send anything", action="store_true")
	return parser


if __name__ == "__main__":
	args = get_parser().parse_args()
	main(**vars(args))
