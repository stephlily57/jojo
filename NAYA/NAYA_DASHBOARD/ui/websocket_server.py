# ============================================================
# NAYA — APPSHELL WEBSOCKET SERVER
# UI / CORE EVENT BUS
# ============================================================

import asyncio
import json
import time
import websockets

HOST = "127.0.0.1"
PORT = 8766   # ⚠️ DIFFÉRENT du boot dashboard

CLIENTS = set()


async def broadcast(payload: dict):
    if not CLIENTS:
        return
    msg = json.dumps(payload)
    await asyncio.gather(
        *[ws.send(msg) for ws in CLIENTS],
        return_exceptions=True
    )


async def handler(websocket):
    print("[APPSHELL][WS] Client connected")
    CLIENTS.add(websocket)

    try:
        async for raw in websocket:
            try:
                data = json.loads(raw)
            except Exception:
                continue

            await broadcast(data)

    except websockets.exceptions.ConnectionClosed:
        print("[APPSHELL][WS] Client disconnected")

    finally:
        CLIENTS.discard(websocket)


async def main():
    async with websockets.serve(handler, HOST, PORT):
        print(f"[APPSHELL][WS] Listening on ws://{HOST}:{PORT}")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
