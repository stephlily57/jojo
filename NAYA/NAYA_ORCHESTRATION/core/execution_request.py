from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class ExecutionRequest:
    directive_id: str
    payload: Dict[str, Any]
    economic_weight: float