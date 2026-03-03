# retry_policy.py

import time

class RetryPolicy:

    def __init__(self, max_attempts=3, base_delay=1):
        self.max_attempts = max_attempts
        self.base_delay = base_delay

    def execute(self, func, *args, **kwargs):

        for attempt in range(1, self.max_attempts + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == self.max_attempts:
                    raise
                delay = self.base_delay * (2 ** (attempt - 1))
                time.sleep(delay)
