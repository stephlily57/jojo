# NAYA_PROJECT_ENGINE / ENGINES / engine_meta_strategy.py

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass(frozen=True)
class MetaSignal:
    projects_involved: List[str]
    synergy_score: float
    detected_at: str


class MetaStrategyEngine:

    def analyze(self, active_projects: List[str]) -> List[MetaSignal]:
        if len(active_projects) < 2:
            return []

        # Synergie simple non forcée
        return [
            MetaSignal(
                projects_involved=active_projects,
                synergy_score=0.75,
                detected_at=datetime.utcnow().isoformat()
            )
        ]


ENGINE_META_STRATEGY = MetaStrategyEngine()
