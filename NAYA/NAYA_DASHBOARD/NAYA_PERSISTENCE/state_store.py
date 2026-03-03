
import json
from pathlib import Path

BASE_DIR = Path("data")
BASE_DIR.mkdir(exist_ok=True)

STATE_FILE = BASE_DIR / "state.json"

def save_state(state: dict) -> None:
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def load_state() -> dict:
    if not STATE_FILE.exists():
        return {}
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
