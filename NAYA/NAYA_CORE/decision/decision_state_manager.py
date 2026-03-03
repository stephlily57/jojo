import json
import os

STATE_PATH = os.path.join(os.path.dirname(__file__), "../state/decision_state.json")

class DecisionStateManager:

    def save(self, state: dict):
        os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
        with open(STATE_PATH, "w") as f:
            json.dump(state, f, indent=2)

    def load(self):
        if not os.path.exists(STATE_PATH):
            return {}
        with open(STATE_PATH, "r") as f:
            return json.load(f)

DECISION_STATE_MANAGER = DecisionStateManager()
