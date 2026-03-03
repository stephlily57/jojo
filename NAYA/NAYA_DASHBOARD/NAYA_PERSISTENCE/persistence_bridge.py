
from NAYA_INTERFACE.bus.state_stream import state_stream
from NAYA_DASHBOARD.NAYA_PERSISTENCE.state_store import save_state
from NAYA_DASHBOARD.NAYA_PERSISTENCE.history_store import append_event
import json

def _on_state(state: dict):
    save_state(state)
    for k, v in state.items():
        append_event(k, json.dumps(v))

state_stream.subscribe(_on_state)
