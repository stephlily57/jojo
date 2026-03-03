# auto_scaler.py

class AutoScaler:

    def __init__(self, worker_pool):
        self.worker_pool = worker_pool

    def evaluate(self, queue_size: int):

        if queue_size > 10:
            print("[AUTOMATION] Scaling up workers")
            self.worker_pool.max_workers += 1
