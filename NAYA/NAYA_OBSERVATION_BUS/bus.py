
import asyncio
import json
import uuid
import time

class ObservationBus:
    def __init__(self):
        self.clients = set()

    async def register(self, ws):
        self.clients.add(ws)

    async def unregister(self, ws):
        self.clients.discard(ws)

    async def emit(self, message: dict):
        payload = json.dumps(message)
        for ws in list(self.clients):
            await ws.send(payload)

    @staticmethod
    def envelope(origin, channel, scope, target, payload, signature_required=False):
        return {
            "id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "origin": origin,
            "channel": channel,
            "scope": scope,
            "target": target,
            "payload": payload,
            "signature_required": signature_required,
            "signature_status": "none"
        }
