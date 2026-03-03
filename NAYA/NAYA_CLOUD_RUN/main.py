import os
import json
import asyncio
import threading
import time
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

# ==================================================
# APP
# ==================================================
app = FastAPI()

# ==================================================
# ÉTAT GLOBAL (UTILISÉ PAR TORIAPP)
# ==================================================
NAYA_STATE = {
    "status": "BOOTING",
    "source": "cloudrun",
    "events": []
}

# ==================================================
# HTTP ENDPOINT — CHECK
# ==================================================
@app.get("/")
def root():
    return {
        "status": "NAYA CloudRun OK",
        "websocket": "/ws",
        "state": NAYA_STATE["status"]
    }

# ==================================================
# >>> AJOUT — ACTIVATION UNIVERSELLE (NON BLOQUANTE)
# ==================================================

NAYA_ACTIVATED = False

def naya_activation_universelle():
    """
    Activation universelle NAYA (Cloud Run).
    Exécutée en arrière-plan.
    NE BLOQUE JAMAIS le serveur HTTP.
    """
    global NAYA_ACTIVATED

    if NAYA_ACTIVATED:
        return

    NAYA_ACTIVATED = True
    NAYA_STATE["status"] = "ACTIVATED"

    print("[NAYA] Activation universelle déclenchée sur Cloud Run.")

    try:
        # Boucle de vie Cloud (non bloquante pour Cloud Run)
        while True:
            time.sleep(30)
            # Ici pourront vivre :
            # - Observation Bus
            # - Event Stream
            # - Orchestration
            # - Signaux VM / autres supports
    except Exception as e:
        print(f"[NAYA][ERROR] {e}")

@app.post("/activate")
def activate():
    """
    Endpoint déclencheur universel.
    """
    threading.Thread(
        target=naya_activation_universelle,
        daemon=True
    ).start()

    return {
        "status": "OK",
        "message": "Naya Activation Universelle déclenchée (Cloud Run)"
    }

# ==================================================
# WEBSOCKET — TORIAPP (INCHANGÉ)
# ==================================================
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    NAYA_STATE["status"] = "CONNECTED"

    try:
        await websocket.send_text(json.dumps({
            "type": "boot",
            "state": NAYA_STATE
        }))

        while True:
            data = await websocket.receive_text()

            event = {
                "type": "event",
                "from": "tori",
                "payload": data
            }

            NAYA_STATE["events"].append(event)

            await websocket.send_text(json.dumps({
                "type": "ack",
                "message": "Event reçu par NAYA",
                "event": event
            }))

    except WebSocketDisconnect:
        NAYA_STATE["status"] = "DISCONNECTED"

# ==================================================
# CLOUD RUN ENTRYPOINT (INCHANGÉ)
# ==================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
