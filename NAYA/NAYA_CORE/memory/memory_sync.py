import redis
import os
import json

class MemorySync:

    def __init__(self):
        self.redis = redis.Redis(
            host=os.environ.get("NAYA_REDIS_HOST", "localhost"),
            port=6379,
            decode_responses=True
        )

    def push_state(self, key, value):
        self.redis.set(f"naya_memory:{key}", json.dumps(value))

    def pull_state(self, key):
        data = self.redis.get(f"naya_memory:{key}")
        return json.loads(data) if data else None
