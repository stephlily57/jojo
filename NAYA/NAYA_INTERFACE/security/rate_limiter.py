import time

class RateLimiter:

    def __init__(self, limit=100):
        self.limit = limit
        self.calls = []

    def allow(self):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < 60]
        if len(self.calls) >= self.limit:
            raise Exception("Rate limit exceeded")
        self.calls.append(now)
        return True