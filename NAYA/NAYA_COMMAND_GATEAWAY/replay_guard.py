# replay_guard.py

PROCESSED = set()

def is_replay(intent_id: str) -> bool:
    return intent_id in PROCESSED

def mark(intent_id: str):
    PROCESSED.add(intent_id)
