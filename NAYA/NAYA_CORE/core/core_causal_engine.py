# NAYA_CORE / core_causal_engine.py

"""
Moteur causal de NAYA.

Transforme les tensions internes en décisions systémiques :
- Escalade cluster
- Mutation doctrinale
- Reconfiguration stratégique

Ne priorise pas.
Ne bloque pas.
Déclenche uniquement si un déséquilibre réel est détecté.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass(frozen=True)
class CausalSignal:
    source: str
    intensity: float
    description: str
    detected_at: str


@dataclass(frozen=True)
class CausalDecision:
    action: str
    reason: str
    decided_at: str


class CoreCausalEngine:
    """
    Coeur causal systémique.
    """

    CLUSTER_THRESHOLD = 0.75
    DOCTRINE_THRESHOLD = 0.65
    STRATEGIC_SHIFT_THRESHOLD = 0.85

    def analyze(self, signals: List[CausalSignal]) -> List[CausalDecision]:

        if not signals:
            return []

        avg_intensity = sum(s.intensity for s in signals) / len(signals)

        decisions = []

        if avg_intensity >= self.STRATEGIC_SHIFT_THRESHOLD:
            decisions.append(
                self._decision(
                    "STRATEGIC_RECONFIGURATION",
                    "High systemic tension detected"
                )
            )

        elif avg_intensity >= self.CLUSTER_THRESHOLD:
            decisions.append(
                self._decision(
                    "CLUSTER_ESCALATION",
                    "Sustained operational pressure"
                )
            )

        elif avg_intensity >= self.DOCTRINE_THRESHOLD:
            decisions.append(
                self._decision(
                    "DOCTRINAL_MUTATION",
                    "Emergent pattern misalignment"
                )
            )

        return decisions

    def _decision(self, action: str, reason: str) -> CausalDecision:
        return CausalDecision(
            action=action,
            reason=reason,
            decided_at=datetime.utcnow().isoformat()
        )


# Instance prête à l’usage
CORE_CAUSAL_ENGINE = CoreCausalEngine()
