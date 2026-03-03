from datetime import datetime

class InterfaceState:

    def __init__(self):
        self.started_at = datetime.utcnow()
        self.active_connections = 0

    def as_dict(self):
        return {
            "started_at": self.started_at.isoformat(),
            "active_connections": self.active_connections
        }