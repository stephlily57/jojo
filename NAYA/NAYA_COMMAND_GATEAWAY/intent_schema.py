
from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Intent:
    intent_id: str
    actor: dict
    category: str
    action: str
    target: dict
    context: dict
    constraints: dict
    timestamp: str

def create_intent(actor, category, action, target=None, context=None, constraints=None):
    return Intent(
        intent_id=str(uuid.uuid4()),
        actor=actor,
        category=category,
        action=action,
        target=target or {},
        context=context or {},
        constraints=constraints or {},
        timestamp=datetime.utcnow().isoformat()
    )
