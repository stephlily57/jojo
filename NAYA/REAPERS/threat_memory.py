# REAPERS/threat_memory.py

import json
from datetime import datetime
from pathlib import Path
from typing import Dict


class ThreatMemory:
    """
    Learns from past threats and escalates security accordingly.
    """

    def __init__(self, storage_file: str = "REAPERS/threat_memory.json"):
        self.storage_file = Path(storage_file)
        self.memory: Dict[str, int] = {}
        self._load()

    def _load(self):
        if self.storage_file.exists():
            with open(self.storage_file, "r") as f:
                self.memory = json.load(f)
        else:
            self.memory = {}

    def _save(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.memory, f, indent=2)

    # ---------------------------------------------------------
    # RECORD EVENT
    # ---------------------------------------------------------

    def record(self, event_type: str):
        self.memory[event_type] = self.memory.get(event_type, 0) + 1
        self._save()

    # ---------------------------------------------------------
    # GET THREAT SCORE
    # ---------------------------------------------------------

    def get_score(self) -> int:
        return sum(self.memory.values())

    def get_event_count(self, event_type: str) -> int:
        return self.memory.get(event_type, 0)

    def reset(self):
        self.memory = {}
        self._save()
