import random
import requests
import uuid

FIRST_DAY = 1568675774000

def create_event(day_ms):
  """
  Makes a test event that, when done en masse, will look like something interesting
  """
  return {
    "name": "order_time_ms",
    "time": int(day_ms + random.uniform(0, 86400000)),
    "value": abs(float(random.gauss(mu=(day_ms - FIRST_DAY)/86400000/10, sigma=1))),
    "chain": random.choice(["mcdonwald", "burger queen", "springfield market", "subnoway"]),
    "food_type": random.choice(["chicken", "chicken", "chicken", "tofu", "salad"]),
    "trace_id": str(uuid.uuid4())
  }

if __name__ == "__main__":
  for day in range(180):
    for _ in range(100):
      requests.post(
        "http://127.0.0.1:8000/stream/abcd/write",
        json=create_event(FIRST_DAY + (day * 86400000))
      )
    print(f"Done with day ${day}")
