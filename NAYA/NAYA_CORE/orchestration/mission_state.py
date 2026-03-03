# NAYA_CORE/mission_state.py

class MissionState:

    def __init__(self):
        self.active_missions = {}

    def start(self, mission_id):
        self.active_missions[mission_id] = "ACTIVE"

    def complete(self, mission_id):
        if mission_id in self.active_missions:
            self.active_missions[mission_id] = "COMPLETED"

    def abort(self, mission_id):
        if mission_id in self.active_missions:
            self.active_missions[mission_id] = "ABORTED"

    def is_any_active(self):
        return any(status == "ACTIVE" for status in self.active_missions.values())

    def get_active(self):
        return [m for m, s in self.active_missions.items() if s == "ACTIVE"]
