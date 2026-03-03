# engine_adaptive_memory.py

class AdaptiveMemory:

    def __init__(self):
        self.patterns = []

    def learn(self, decision: dict):
        if decision.get("profit", 0) > 10000:
            self.patterns.append(decision)


ADAPTIVE_MEMORY = AdaptiveMemory()
