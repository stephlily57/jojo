
import asyncio, json, os
import websockets
from .intent_schema import Intent
from .gateway import CommandGateway
from .journal import IntentJournal

BASE_DIR = os.path.dirname(__file__)

async def handler(websocket):
    journal = IntentJournal(
        key_path=os.path.join(BASE_DIR, "gateway.key"),
        log_path=os.path.join(BASE_DIR, "intent.log.enc")
    )
    gateway = CommandGateway(journal)

    async for msg in websocket:
        data = json.loads(msg)
        intent = Intent(**data)
        result = gateway.handle(intent)
        await websocket.send(json.dumps(result))

async def main():
    async with websockets.serve(handler, "127.0.0.1", 8766):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
