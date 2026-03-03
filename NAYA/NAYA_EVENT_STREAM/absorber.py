
from .event_envelope import EventEnvelope

class StreamAbsorber:
    def __init__(self, stream):
        self.stream = stream

    async def start(self):
        evt = EventEnvelope.create(
            source="SYSTEM",
            module="event_stream",
            kind="STATE",
            payload={"status": "online"}
        )
        await self.stream.publish(evt)
