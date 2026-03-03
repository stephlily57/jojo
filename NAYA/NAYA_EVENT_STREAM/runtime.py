
import asyncio
from .event_stream import EventStream
from .absorber import StreamAbsorber
from .ws_server import WebSocketServer

async def main():
    stream = EventStream()
    absorber = StreamAbsorber(stream)
    ws = WebSocketServer(stream)
    await absorber.start()
    await ws.start()

if __name__ == "__main__":
    asyncio.run(main())
