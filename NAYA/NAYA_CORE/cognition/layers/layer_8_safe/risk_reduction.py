"""
NAYA LLM INTEGRATION
LAYER 8 — RISK REDUCTION

Rôle :
- Réduire le risque sans bloquer l’action
- Proposer des ajustements intelligents
- Renforcer la continuité et la robustesse
- Préserver la liberté stratégique de Naya

Ce module ne bloque rien.
Il suggère, atténue et renforce.
"""

from typing import List, Dict


class RiskReductionEngine:
    """
    Moteur de réduction de risque non bloquant.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs internes pour maturation
        self.total_elements_processed = 0
        self.low_risk_items = 0
        self.mitigated_items = 0
        self.unmitigated_items = 0

    # ---------
    # PUBLIC API
    # ---------

    def reduce(self, elements: List[str]) -> Dict[str, List[str]]:
        """
        Analyse les éléments et propose une réduction de risque.

        Retourne :
        - 'low_risk'     : éléments naturellement robustes
        - 'mitigated'    : éléments renforcés par ajustement
        - 'unmitigated'  : éléments à risque non atténué (information uniquement)
        """
        low_risk = []
        mitigated = []
        unmitigated = []

        for element in elements:
            self.total_elements_processed += 1

            clean = self._clean(element)
            if not clean:
                continue

            risk = self._risk_level(clean)

            if risk < 0.3:
                low_risk.append(clean)
                self.low_risk_items += 1
            elif risk < 0.7:
                mitigated.append(self._mitigate(clean))
                self.mitigated_items += 1
            else:
                unmitigated.append(clean)
                self.unmitigated_items += 1

        return {
            "low_risk": low_risk,
            "mitigated": mitigated,
            "unmitigated": unmitigated
        }

    # =========================
    # Internal logic
    # =========================

    def _clean(self, text: str) -> str:
        """
        Nettoyage sûr.
        """
        if not isinstance(text, str):
            return ""

        return text.strip()

    def _risk_level(self, text: str) -> float:
        """
        Évalue le niveau de risque potentiel.

        Heuristiques simples :
        - dépendance
        - fragilité
        - manque de marge
        """
        score = 0.0
        lower = text.lower()

        risk_markers = [
            "unique point de défaillance",
            "sans alternative",
            "dépendance critique",
            "fragile",
            "aucune marge",
            "non testé",
        ]

        for marker in risk_markers:
            if marker in lower:
                score += 0.2

        if len(text) >= 60:
            score += 0.1

        if score > 1.0:
            score = 1.0
        if score < 0.0:
            score = 0.0

        return score

    def _mitigate(self, text: str) -> str:
        """
        Applique une atténuation non bloquante.

        Ici, l’atténuation est conceptuelle :
        - signaler implicitement qu’une alternative existe
        - renforcer la résilience par formulation
        """
        return f"{text} (robustesse renforcée par diversification ou marge de sécurité)"


# =========================
# Fonction utilitaire simple
# =========================

_risk_reduction_engine_instance = RiskReductionEngine()


def reduce_risk(elements: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour réduction de risque directe.
    """
    return _risk_reduction_engine_instance.reduce(elements)
