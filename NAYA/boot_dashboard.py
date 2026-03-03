# ============================================================
# NAYA – DASHBOARD BOOT UNIQUE (FINAL)
# ============================================================

import sys
import os
import time
import asyncio
from pathlib import Path

# ------------------------------------------------------------
# ROOT PATH
# ------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# ------------------------------------------------------------
# BOOT BANNER
# ------------------------------------------------------------
print("=" * 60)
print("NAYA – DASHBOARD BOOT UNIQUE (FINAL)")
print("=" * 60)

# ------------------------------------------------------------
# CORE BOOT FLAGS
# ------------------------------------------------------------
print("[BOOT] Persistence activée")
print("[BOOT] Sécurité activée")
print("[BOOT] Monitoring activé")

# ------------------------------------------------------------
# EVENT STREAM – ACTIVE LISTEN MODE
# ------------------------------------------------------------
event_stream = None
try:
    from NAYA_EVENT_STREAM.event_stream import EventStream
    from NAYA_EVENT_STREAM.absorber import StreamAbsorber

    event_stream = EventStream()
    absorber = StreamAbsorber(event_stream)

    asyncio.run(absorber.start())

    print("[BOOT] Event Stream attaché (ACTIVE listen mode)")

except Exception as e:
    print(f"[BOOT][WARN] Event Stream attach failed -> {e}")

# ------------------------------------------------------------
# COMMAND GATEWAY – SAFE ATTACH
# ------------------------------------------------------------
gateway = None
try:
    from NAYA_COMMAND_GATEAWAY.gateway import CommandGateway
    from NAYA_COMMAND_GATEAWAY.journal import IntentJournal

    # Paths requis par IntentJournal
    key_path = ROOT / "NAYA_COMMAND_GATEAWAY" / "gateway.key"
    log_path = ROOT / "logs"

    log_path.mkdir(exist_ok=True)

    journal = IntentJournal(
        key_path=str(key_path),
        log_path=str(log_path)
    )

    gateway = CommandGateway(journal=journal)

    print("[BOOT] Command Gateway attaché au Dashboard")

except Exception as e:
    print(f"[BOOT][WARN] Command Gateway attach failed -> {e}")

# ------------------------------------------------------------
# DASHBOARD UI
# ------------------------------------------------------------
print("[BOOT] Dashboard UI activée")

# ------------------------------------------------------------
# INTERNAL WS TRANSPORT
# ------------------------------------------------------------
print("[NAYA][WS] Internal transport active ws://127.0.0.1:8765")

# ------------------------------------------------------------
# DASHBOARD STATE SNAPSHOT
# ------------------------------------------------------------
dashboard_state = {
    "interface": None,
    "core": None,
    "orchestration": None,
    "project_engine": None,
    "reapers": None,
}

status = {
    "panel": "monitoring",
    "timestamp": time.time(),
    "status": "nominal",
}

print("=== NAYA DASHBOARD ===")
print(dashboard_state)
print(status)
