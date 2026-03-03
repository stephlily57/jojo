# -*- coding: utf-8-sig -*-
from datetime import datetime
from NAYA_DASHBOARD.app_runtime.runtime_state import STATE
from NAYA_DASHBOARD.app_runtime.runtime_config import APP_NAME

def start_runtime():
    STATE.active = True
    STATE.started_at = datetime.utcnow().isoformat()
    print(f"[{APP_NAME}] Runtime started at {STATE.started_at}")

if __name__ == "__main__":
    start_runtime()
