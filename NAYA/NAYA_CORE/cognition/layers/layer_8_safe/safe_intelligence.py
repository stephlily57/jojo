"""
NAYA LLM INTEGRATION
LAYER 8 — SAFE INTELLIGENCE

Rôle :
- Renforcer la fiabilité cognitive
- Réduire les risques sans bloquer l’intelligence
- Identifier les zones sensibles ou fragiles
- Soutenir la robustesse globale dans le temps

Ce module ne décide pas.
Il évalue, signale et sécurise intelligemment.
"""

from typing import List, Dict


class SafeIntelligence:
    """
    Moteur de sécurité intelligente.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs internes pour maturation
        self.total_elements_checked = 0
        self.safe_elements = 0
        self.sensitive_elements = 0
        self.high_risk_elements = 0

    # ---------
    # PUBLIC API
    # ---------

    def assess(self, elements: List[str]) -> Dict[str, List[str]]:
        """
        Évalue les éléments sous l’angle de la sécurité et de la robustesse.

        Retourne :
        - 'safe'       : éléments sans risque notable
        - 'sensitive'  : éléments à surveiller
        - 'high_risk'  : éléments potentiellement dangereux
        """
        safe = []
        sensitive = []
        high_risk = []

        for element in elements:
            self.total_elements_checked += 1

            clean = self._clean(element)
            if not clean:
                continue

            risk_score = self._risk_score(clean)

            if risk_score >= 0.75:
                high_risk.append(clean)
                self.high_risk_elements += 1
            elif risk_score >= 0.4:
                sensitive.append(clean)
                self.sensitive_elements += 1
            else:
                safe.append(clean)
                self.safe_elements += 1

        return {
            "safe": safe,
            "sensitive": sensitive,
            "high_risk": high_risk
        }

    # =========================
    # Internal logic
    # =========================

    def _clean(self, text: str) -> str:
        """
        Nettoyage sûr et minimal.
        """
        if not isinstance(text, str):
            return ""

        return text.strip()

    def _risk_score(self, text: str) -> float:
        """
        Évalue le niveau de risque d’un élément.

        Heuristiques :
        - exposition
        - irréversibilité
        - impact potentiel
        """
        score = 0.0
        lower = text.lower()

        # Marqueurs de risque élevé
        high_risk_markers = [
            "irréversible",
            "perte majeure",
            "violation",
            "illégal",
            "non conforme",
            "faille",
            "exposition critique",
            "rupture",
        ]

        for marker in high_risk_markers:
            if marker in lower:
                score += 0.3

        # Marqueurs de sensibilité
        sensitive_markers = [
            "donnée sensible",
            "confidentiel",
            "accès limité",
            "dépendance",
            "zone grise",
            "instable",
        ]

        for marker in sensitive_markers:
            if marker in lower:
                score += 0.15

        # Longueur indicative (souvent plus détaillée = plus de surface de risque)
        if len(text) >= 50:
            score += 0.1

        # Normalisation
        if score > 1.0:
            score = 1.0
        if score < 0.0:
            score = 0.0

        return score


# =========================
# Fonction utilitaire simple
# =========================

_safe_intelligence_instance = SafeIntelligence()


def assess_safe_intelligence(elements: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour évaluation directe de la sécurité intelligente.
    """
    return _safe_intelligence_instance.assess(elements)
