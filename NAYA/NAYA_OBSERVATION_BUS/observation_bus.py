# NAYA_OBSERVATION_BUS/observation_bus.py

import asyncio
from typing import Callable, Dict, List


class ObservationBus:

    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, callback: Callable):
        self.subscribers.setdefault(event_type, []).append(callback)

    async def publish(self, event_type: str, payload: dict):

        if event_type not in self.subscribers:
            return

        for callback in self.subscribers[event_type]:
            await callback(payload)
