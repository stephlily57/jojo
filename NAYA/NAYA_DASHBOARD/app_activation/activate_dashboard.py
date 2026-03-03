# -*- coding: utf-8-sig -*-
from NAYA_DASHBOARD.app_runtime.runtime_entry import start_runtime

def activate():
    print("[ACTIVATION] Activating NAYA Dashboard Application")
    start_runtime()
    print("[ACTIVATION] Activation complete")

if __name__ == "__main__":
    activate()
