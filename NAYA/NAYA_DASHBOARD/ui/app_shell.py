# ============================================================
# NAYA — APP SHELL
# Core → AppShell WS Bus
# ============================================================

import asyncio
import json
import time
import websockets

WS_URL = "ws://127.0.0.1:8766"


def packet(kind, payload):
    return {
        "source": "app_shell",
        "type": kind,
        "payload": payload,
        "timestamp": time.time()
    }


async def run():
    while True:
        try:
            async with websockets.connect(WS_URL) as ws:
                print("[APP_SHELL] Connected to AppShell WS")

                await ws.send(json.dumps(packet("INIT", {
                    "system": "NAYA",
                    "mode": "standby",
                    "status": "idle"
                })))

                while True:
                    await ws.send(json.dumps(packet("HEARTBEAT", {
                        "status": "alive"
                    })))
                    await asyncio.sleep(1)

        except Exception as e:
            print("[APP_SHELL] WS unavailable, retrying…", e)
            await asyncio.sleep(2)


if __name__ == "__main__":
    launch()
