import random
import requests
import uuid

def create_event():
  """
  Makes a test event that, when done en masse, will look like something interesting
  """
  return {
    "name": "response_time",
    "time": int(random.uniform(1582811415270, 1582856359000)),
    "value": float(random.gauss(mu=0, sigma=1)),
    "family": random.choice(["count", "export", "widget", "materialize"]),
    "app_name": random.choice(["query", "query", "query", "pipeline", "luigi"]),
    "trace_id": str(uuid.uuid4())
  }

if __name__ == "__main__":
	for i in range(700):
		requests.post("http://127.0.0.1:8000/stream/abcd/write", json=create_event())
