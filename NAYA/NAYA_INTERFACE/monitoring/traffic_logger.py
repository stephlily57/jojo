import json
from datetime import datetime

class TrafficLogger:

    def log(self, directive):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "directive_id": directive.get("directive_id"),
            "origin": directive.get("origin")
        }
        print(json.dumps(log_entry))