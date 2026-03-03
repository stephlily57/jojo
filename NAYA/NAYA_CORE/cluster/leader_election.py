import redis
import socket
import os

class LeaderElection:

    def __init__(self):
        self.node_id = socket.gethostname()
        self.redis = redis.Redis(
            host=os.environ.get("NAYA_REDIS_HOST", "localhost"),
            port=6379,
            decode_responses=True
        )
        self.key = "naya_cluster_leader"
        self.ttl = 10

    def try_become_leader(self):
        return self.redis.set(self.key, self.node_id, nx=True, ex=self.ttl)

    def refresh(self):
        if self.is_leader():
            self.redis.expire(self.key, self.ttl)

    def is_leader(self):
        return self.redis.get(self.key) == self.node_id
