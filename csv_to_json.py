import csv
import datetime
import re
import json

import requests

def transactionToInflux(transaction_dict):
	"""
	"""
	date_string = transaction_dict.pop('Date')
	amt_string = transaction_dict.pop('Amount')

	date_object = datetime.datetime.strptime(date_string, "%m/%d/%Y")

	transaction_dict['name'] = 'transaction_amount'
	transaction_dict['time'] = int(date_object.timestamp() * 1000)
	transaction_dict['value'] = float(re.sub(r'[^0-9\.-]', '', amt_string))

	return transaction_dict


def main():
	"""
	"""
	with open("transactions.csv") as f:
		reader = csv.DictReader(f)
		for d in reader:
			# print(transactionToInflux(d))
			requests.post(
				"http://127.0.0.1:8000/stream/abcd/write",
				json=transactionToInflux(d)
			)

if __name__ == "__main__":
	main()
