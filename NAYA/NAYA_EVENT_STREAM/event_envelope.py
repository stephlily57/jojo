
from dataclasses import dataclass, asdict
from datetime import datetime
import uuid

@dataclass
class EventEnvelope:
    id: str
    ts: str
    source: str
    module: str
    kind: str
    level: str
    payload: dict
    tags: list
    seq: int = 0

    @staticmethod
    def create(source, module, kind, level="INFO", payload=None, tags=None):
        return EventEnvelope(
            id=str(uuid.uuid4()),
            ts=datetime.utcnow().isoformat(),
            source=source,
            module=module,
            kind=kind,
            level=level,
            payload=payload or {},
            tags=tags or [],
        )

    def to_dict(self):
        return asdict(self)
