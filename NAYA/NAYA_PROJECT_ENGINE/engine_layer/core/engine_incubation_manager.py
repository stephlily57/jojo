# engine_incubation_manager.py

from typing import List, Dict


class IncubationManager:

    def __init__(self):
        self.incubated = []

    def store(self, opportunities: List[Dict]):
        self.incubated.extend(opportunities)

    def release(self):
        released = self.incubated
        self.incubated = []
        return released


INCUBATION_MANAGER = IncubationManager()
