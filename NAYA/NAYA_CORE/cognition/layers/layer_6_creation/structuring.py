"""
NAYA LLM INTEGRATION
LAYER 6 — STRUCTURING

Rôle :
- Structurer une matière cognitive ou narrative
- Hiérarchiser sans rigidifier
- Clarifier la lecture et la compréhension
- Servir la stratégie, la création et la précision

Ce module ne décide pas.
Il organise et met en forme.
"""

from typing import List, Dict


class StructuringEngine:
    """
    Moteur de structuration logique.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs internes pour maturation
        self.total_items_structured = 0
        self.primary_blocks = 0
        self.secondary_blocks = 0

    # ---------
    # PUBLIC API
    # ---------

    def structure(self, elements: List[str]) -> Dict[str, List[str]]:
        """
        Structure des éléments textuels en blocs logiques.

        Retourne :
        - 'primary'   : blocs centraux
        - 'secondary' : blocs de soutien
        - 'discarded' : éléments trop faibles ou redondants
        """
        primary = []
        secondary = []
        discarded = []

        for element in elements:
            self.total_items_structured += 1

            clean = self._clean(element)
            if not clean:
                discarded.append(element)
                continue

            weight = self._structure_weight(clean)

            if weight >= 0.7:
                primary.append(clean)
                self.primary_blocks += 1
            elif weight >= 0.4:
                secondary.append(clean)
                self.secondary_blocks += 1
            else:
                discarded.append(clean)

        return {
            "primary": primary,
            "secondary": secondary,
            "discarded": discarded
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

    def _structure_weight(self, text: str) -> float:
        """
        Évalue le poids structurel d’un élément.

        Heuristiques :
        - clarté
        - complétude
        - potentiel d’ancrage
        """
        score = 0.0
        length = len(text)

        if length >= 20:
            score += 0.3
        if length >= 45:
            score += 0.2

        lower = text.lower()

        anchoring_markers = [
            "objectif",
            "problème",
            "solution",
            "enjeu",
            "résultat",
            "structure",
            "cadre",
        ]

        for marker in anchoring_markers:
            if marker in lower:
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

_structuring_engine_instance = StructuringEngine()


def structure_elements(elements: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour structuration directe.
    """
    return _structuring_engine_instance.structure(elements)
