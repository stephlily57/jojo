
import asyncio
from collections import deque

class EventStream:
    def __init__(self, maxlen=5000):
        self.buffer = deque(maxlen=maxlen)
        self.subscribers = []
        self._seq = 0
        self._lock = asyncio.Lock()

    async def publish(self, event):
        async with self._lock:
            self._seq += 1
            event.seq = self._seq
            self.buffer.append(event)
            for cb in list(self.subscribers):
                await cb(event)

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def last(self, n=100):
        return list(self.buffer)[-n:]
