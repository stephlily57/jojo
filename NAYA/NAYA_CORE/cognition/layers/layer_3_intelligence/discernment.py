"""
NAYA LLM INTEGRATION
LAYER 3 — DISCERNMENT

Rôle :
- Affiner le jugement cognitif
- Distinguer le pertinent du trompeur
- Détecter les fausses évidences et les raccourcis faibles
- Renforcer la qualité des choix stratégiques

Ce module ne décide pas.
Il améliore la qualité du discernement.
"""

from typing import List, Dict


class DiscernmentEngine:
    """
    Moteur de discernement cognitif.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs internes pour maturation
        self.total_elements_analyzed = 0
        self.trustworthy_count = 0
        self.questionable_count = 0
        self.misleading_count = 0

    # ---------
    # PUBLIC API
    # ---------

    def assess(self, elements: List[str]) -> Dict[str, List[str]]:
        """
        Évalue le niveau de fiabilité cognitive des éléments.

        Retourne :
        - 'trustworthy' : éléments solides et fiables
        - 'questionable': éléments plausibles mais à vérifier
        - 'misleading'  : éléments trompeurs ou faibles
        """
        trustworthy = []
        questionable = []
        misleading = []

        for element in elements:
            self.total_elements_analyzed += 1

            clean = self._clean(element)
            if not clean:
                continue

            score = self._evaluate_discernment(clean)

            if score >= 0.75:
                trustworthy.append(clean)
                self.trustworthy_count += 1
            elif score >= 0.4:
                questionable.append(clean)
                self.questionable_count += 1
            else:
                misleading.append(clean)
                self.misleading_count += 1

        return {
            "trustworthy": trustworthy,
            "questionable": questionable,
            "misleading": misleading
        }

    # =========================
    # Internal logic
    # =========================

    def _clean(self, text: str) -> str:
        """
        Nettoyage simple et sûr.
        """
        if not isinstance(text, str):
            return ""

        return text.strip()

    def _evaluate_discernment(self, text: str) -> float:
        """
        Évalue la qualité de discernement d’un élément.

        Heuristiques simples :
        - clarté
        - structure
        - absence de généralisation abusive
        """
        score = 0.0
        length = len(text)

        # Longueur minimale pour crédibilité
        if length >= 20:
            score += 0.3
        if length >= 40:
            score += 0.2

        lower = text.lower()

        # Marqueurs de généralisation abusive
        misleading_markers = [
            "toujours",
            "jamais",
            "tout le monde",
            "évident",
            "forcément",
            "sans aucun doute",
        ]

        for marker in misleading_markers:
            if marker in lower:
                score -= 0.2

        # Marqueurs de rigueur
        rigor_markers = [
            "selon",
            "dans ce contexte",
            "en fonction de",
            "dépend de",
            "condition",
            "hypothèse",
        ]

        for marker in rigor_markers:
            if marker in lower:
                score += 0.15

        # Normalisation
        if score > 1.0:
            score = 1.0
        if score < 0.0:
            score = 0.0

        return score


# =========================
# Fonction utilitaire simple
# =========================

_discernment_engine_instance = DiscernmentEngine()


def assess_discernment(elements: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour évaluation directe du discernement.
    """
    return _discernment_engine_instance.assess(elements)
