from NAYA_CORE.core.engine_master import EngineMaster
from SYSTEM_REGISTRY.registry_bootstrap import SystemRegistry

import json
from datetime import datetime


def log(message, level="INFO"):
    print(json.dumps({
        "time": datetime.utcnow().isoformat(),
        "level": level,
        "message": message
    }))


if __name__ == "__main__":

    log("Boot initialization started")

    # =========================
    # CORE INITIALIZATION
    # =========================
    core = EngineMaster()

    # =========================
    # SYSTEM REGISTRY
    # =========================
    registry = SystemRegistry()
    registry.initialize(core)

    # =========================
    # CORE ACTIVATION
    # =========================
    if hasattr(core, "activate"):
        core.activate()

    print("=== NAYA SYSTEM READY - PRODUCTION LOCKED ===")
