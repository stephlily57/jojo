import time

class GuardianMode:
    def __init__(self):
        self.active = False

    def check(self, last_human_interaction_hours):
        if last_human_interaction_hours > 72:
            self.active = True
        return self.active

    def enforce(self):
        if self.active:
            return "GUARDIAN_ACTIVE"
        return "NORMAL"
