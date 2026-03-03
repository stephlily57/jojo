# NAYA_EVENT_STREAM/ws_server.py

import asyncio
import json
import websockets


class EventStreamServer:

    def __init__(self):
        self.clients = set()

    async def handler(self, websocket):
        self.clients.add(websocket)
        try:
            async for _ in websocket:
                pass
        finally:
            self.clients.remove(websocket)

    async def broadcast(self, event: dict):

        if not self.clients:
            return

        message = json.dumps(event)
        await asyncio.gather(
            *[client.send(message) for client in self.clients]
        )

    async def start(self, host="0.0.0.0", port=8765):

        server = await websockets.serve(self.handler, host, port)
        print(f"[EVENT STREAM] Running on ws://{host}:{port}")
        return server
