import time

class DecisionMonitor:

    def __init__(self):
        self.last_cycle = time.time()

    def heartbeat(self):
        self.last_cycle = time.time()

    def health(self):
        return {
            "status": "stable",
            "last_cycle": self.last_cycle
        }

DECISION_MONITOR = DecisionMonitor()
