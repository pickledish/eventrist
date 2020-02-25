import time
import typing

from fastapi import FastAPI
from influxdb import InfluxDBClient
from pydantic import BaseModel
from starlette.requests import Request

# -----------------------------------------------------------------------------

app = FastAPI()

# wait for the influx container to actually start
time.sleep(5)

# can't address by localhost or IP, need service name
# https://docs.docker.com/compose/networking/
client = InfluxDBClient("influx", 8086, "root", "root")

# -----------------------------------------------------------------------------

class QueryDefinition(BaseModel):
  event_name: str
  aggregation: str # must be one of sum, count, etc
  rollup: str # must be one of 1h, 4h, 24h, etc
  start_time: int
  end_time: int
  filters: typing.Dict[str, str] = {}
  group_by: typing.List[str] = []

# -----------------------------------------------------------------------------

@app.post("/stream/{stream_id}/write")
async def root(stream_id: str, request: Request):
  """
  """
  request_dict = await request.json()

  event_name = request_dict.pop("name", None)
  event_time = request_dict.pop("time", time.time() * 1000)
  event_value = request_dict.pop("value", 1)

  if event_name is None:
    raise Exception("Can't write a data point with no name!")

  json_body = {
    "measurement": event_name,
    "tags": request_dict,
    "time": int(event_time),
    "fields": {"value": float(event_value)}
  }

  client.create_database(stream_id)
  client.write_points([json_body], database=stream_id, time_precision="ms")

@app.post("/stream/{stream_id}/query")
async def root(stream_id: str, query: QueryDefinition):
  """
  """
  template = "SELECT {} FROM {} WHERE {} GROUP BY {}"

  s_part = "COUNT(*)" # TODO

  f_part = "\"{}\"".format(query.event_name)

  filter_template = "\"{}\" = '{}'"
  filters = [filter_template.format(k, v) for k, v in query.filters.items()]

  w_part = " AND ".join([
    '"time" >= {}'.format(query.start_time),
    '"time" <= {}'.format(query.end_time),
    *filters
  ])

  g_part = ", ".join([
    "time({})".format(query.rollup),
    *query.group_by
  ])

  query_string = template.format(s_part, f_part, w_part, g_part)

  return client.query(query_string, database=stream_id).raw
