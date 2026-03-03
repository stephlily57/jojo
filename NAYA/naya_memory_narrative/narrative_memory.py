from collections import deque
from datetime import datetime

class NarrativeMemory:
    def __init__(self, max_entries=30):
        self.memory = deque(maxlen=max_entries)

    def add(self, text):
        entry = {
            "time": datetime.utcnow().isoformat(),
            "text": text
        }
        self.memory.append(entry)

    def get_all(self):
        return list(self.memory)
