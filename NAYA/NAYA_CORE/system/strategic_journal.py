import redis
import os
import json
from datetime import datetime

class StrategicJournal:

    def __init__(self):
        self.redis = redis.Redis(
            host=os.environ.get("NAYA_REDIS_HOST", "localhost"),
            port=6379,
            decode_responses=True
        )
        self.stream = "naya_strategic_journal"

    def log(self, event_type, payload):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "type": event_type,
            "payload": payload
        }
        self.redis.xadd(self.stream, entry)

    def read_latest(self, count=10):
        return self.redis.xrevrange(self.stream, count=count)
