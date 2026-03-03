import json
import os

EVOLUTION_LOG = os.path.join(os.path.dirname(__file__), "../state/evolution_log.json")

class AdaptiveMemoryController:

    def __init__(self):
        self.history = []

    def store(self, opportunity: dict, result: dict):
        if result.get("status") == "EXECUTING":
            self.history.append(opportunity)
            self._persist()

    def _persist(self):
        os.makedirs(os.path.dirname(EVOLUTION_LOG), exist_ok=True)
        with open(EVOLUTION_LOG, "w") as f:
            json.dump(self.history[-100:], f, indent=2)

ADAPTIVE_MEMORY_CONTROLLER = AdaptiveMemoryController()
