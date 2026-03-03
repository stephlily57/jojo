# NAYA_CORE/decision/allocation_intelligence.py

from dataclasses import dataclass
from typing import Dict


@dataclass
class AllocationDecision:
    action: str  # execute | incubate | reject
    priority: float


class AllocationIntelligence:

    def decide(self, density_score: float, solvable: bool, sovereign_ok: bool) -> AllocationDecision:

        if not solvable or not sovereign_ok:
            return AllocationDecision(action="reject", priority=0)

        if density_score > 100000:
            return AllocationDecision(action="execute", priority=1.0)

        if density_score > 20000:
            return AllocationDecision(action="execute", priority=0.8)

        return AllocationDecision(action="incubate", priority=0.5)


ALLOCATION_INTELLIGENCE = AllocationIntelligence()
