import time

class IntentionLoop:
    def __init__(self):
        self.state = "IDLE"

    def evaluate(self, system_status):
        if system_status.get("errors"):
            self.state = "STABILIZE"
        elif system_status.get("no_activity"):
            self.state = "WAIT"
        else:
            self.state = "CONTINUE"
        return self.state

    def run(self, system_status):
        decision = self.evaluate(system_status)
        return decision
