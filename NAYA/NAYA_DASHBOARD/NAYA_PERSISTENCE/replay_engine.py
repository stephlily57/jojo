
from NAYA_DASHBOARD.NAYA_PERSISTENCE.state_store import load_state

def replay_last_state() -> dict:
    return load_state()
