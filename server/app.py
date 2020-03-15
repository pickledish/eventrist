import logging
import time
import typing

from fastapi import FastAPI
from influxdb import InfluxDBClient
from pydantic import BaseModel
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware

# -----------------------------------------------------------------------------

app = FastAPI()
logger = logging.getLogger("api")

# wait for the influx container to actually start
time.sleep(5)

logger.info("Starting up!")

# can't address by localhost or IP, need service name
# https://docs.docker.com/compose/networking/
client = InfluxDBClient("influx", 8086, "root", "root")

origins = [
  "http:localhost",
  "http:localhost:8000",
  "http://127.0.0.1:5000",
  "http://localhost:5000",
  "http://app.inboxed.cc"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# -----------------------------------------------------------------------------

class QueryDefinition(BaseModel):
  event_name: str
  aggregation: str # must be one of sum, count, etc
  rollup: str = "" # must be one of 1h, 4h, 24h, etc
  start_time: int
  end_time: int
  # filters: typing.Dict[str, str] = {}
  filters: str = ""
  group_by: typing.List[str] = []
  timezone: str = "America/New_York"

class TagKeyRequest(BaseModel):
  event_name: str

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
  aggr_dict = {
    "raw": "SELECT *",
    "cnt": "SELECT COUNT(*)",
    "sum": "SELECT SUM(value)",
    "min": "SELECT MIN(value)",
    "max": "SELECT MAX(value)",
    "avg": "SELECT MEAN(value)",
    "p50": "SELECT PERCENTILE(value, 50)",
    "p75": "SELECT PERCENTILE(value, 75)",
    "p90": "SELECT PERCENTILE(value, 90)",
    "p95": "SELECT PERCENTILE(value, 95)",
    "p99": "SELECT PERCENTILE(value, 99)"
  }

  q_select = aggr_dict.get(query.aggregation, None)

  if q_select is None:
    raise Exception(f"Invalid aggregation {query.aggregation}")

  q_from = f"FROM \"{query.event_name}\""

  # filters = ["\"{}\" = '{}'".format(k, v) for k, v in query.filters.items()]
  q_filters = [query.filters] if query.filters else []

  q_times = [
    f"\"time\" >= {query.start_time * 1000000}",
    f"\"time\" <= {query.end_time * 1000000}"
  ]

  q_where = f"WHERE {' AND '.join(q_times + q_filters)}"

  q_rollup = [f"time({query.rollup})"] if query.rollup else []

  q_groupings = q_rollup + [f"\"{s}\"" for s in query.group_by]

  q_group_by = f"GROUP BY {', '.join(q_groupings)}" if q_groupings else ""

  q_timezone = f"TZ('{query.timezone}')"

  query_string = f"{q_select} {q_from} {q_where} {q_group_by} {q_timezone}"

  logger.info(query_string)

  return client.query(query_string, database=stream_id).raw

@app.post("/stream/{stream_id}/names")
async def root(stream_id: str):
  """
  """
  query_string = "SHOW MEASUREMENTS"

  return client.query(query_string, database=stream_id).raw

@app.post("/stream/{stream_id}/tagkeys")
async def root(stream_id: str, req: TagKeyRequest):
  """
  """
  q_from = "FROM {}".format(req.event_name) if req.event_name != "*" else ""

  query_string = f"SHOW TAG KEYS {q_from}"

  return client.query(query_string, database=stream_id).raw
