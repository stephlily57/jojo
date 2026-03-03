
import asyncio
import websockets
from bus import ObservationBus

bus = ObservationBus()

async def handler(ws):
    await bus.register(ws)
    try:
        async for _ in ws:
            pass
    finally:
        await bus.unregister(ws)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8899):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
