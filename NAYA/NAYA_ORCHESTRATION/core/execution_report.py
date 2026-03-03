from dataclasses import dataclass
from typing import Dict, Any
from datetime import datetime

@dataclass
class ExecutionReport:
    directive_id: str
    environment: str
    status: str
    metrics: Dict[str, Any]
    timestamp: datetime = datetime.utcnow()