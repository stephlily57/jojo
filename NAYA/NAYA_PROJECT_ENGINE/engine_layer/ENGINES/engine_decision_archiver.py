# engine_decision_archiver.py

class DecisionArchiver:

    def __init__(self):
        self.archive = []

    def store(self, decision: dict):
        if decision.get("useful", False):
            self.archive.append(decision)


DECISION_ARCHIVER = DecisionArchiver()
