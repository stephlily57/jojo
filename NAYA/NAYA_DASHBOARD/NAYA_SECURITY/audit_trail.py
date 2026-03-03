
import json
from pathlib import Path

AUDIT_DIR = Path("data/audit")
AUDIT_DIR.mkdir(parents=True, exist_ok=True)

def record(event: dict) -> None:
    path = AUDIT_DIR / f"{event['request_id']}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(event, f, indent=2)
