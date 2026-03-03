"""
NAYA LLM INTEGRATION
LAYER 3 — COGNITIVE INTELLIGENCE

Rôle :
- Renforcer la compréhension cognitive
- Améliorer le discernement
- Détecter incohérences et fragilités
- Consolider une pensée plus solide et plus mature

Ce module ne décide pas.
Il éclaire, structure et renforce.
"""

from typing import List, Dict


class CognitiveIntelligence:
    """
    Moteur d’intelligence cognitive.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs simples pour maturation future
        self.total_items_processed = 0
        self.coherence_checks = 0
        self.fragility_detected = 0

    # ---------
    # PUBLIC API
    # ---------

    def analyze(self, elements: List[str]) -> Dict[str, List[str]]:
        """
        Analyse cognitive d’éléments textuels.

        Retourne :
        - 'solid'     : éléments cognitivement solides
        - 'fragile'   : éléments flous, incomplets ou incohérents
        - 'notes'     : observations cognitives générales
        """
        solid = []
        fragile = []
        notes = []

        for element in elements:
            self.total_items_processed += 1

            clean = self._clean(element)
            if not clean:
                continue

            self.coherence_checks += 1

            if self._is_solid(clean):
                solid.append(clean)
            else:
                fragile.append(clean)
                self.fragility_detected += 1

        if fragile:
            notes.append("Présence d’éléments cognitivement fragiles")

        if solid and not fragile:
            notes.append("Cohérence cognitive élevée")

        return {
            "solid": solid,
            "fragile": fragile,
            "notes": notes
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

    def _is_solid(self, text: str) -> bool:
        """
        Évalue la solidité cognitive d’un élément.

        Heuristique :
        - clarté
        - structure
        - absence de contradiction apparente
        """
        length = len(text)

        # Trop court → fragile
        if length < 15:
            return False

        lower = text.lower()

        contradiction_markers = [
            "mais",
            "cependant",
            "en même temps",
            "d'un côté",
            "d'un autre côté",
        ]

        contradiction_count = 0
        for marker in contradiction_markers:
            if marker in lower:
                contradiction_count += 1

        # Trop de contradictions → fragilité
        if contradiction_count >= 2:
            return False

        return True


# =========================
# Fonction utilitaire simple
# =========================

_cognitive_intelligence_instance = CognitiveIntelligence()


def analyze_cognitive_intelligence(elements: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour analyse cognitive directe.
    """
    return _cognitive_intelligence_instance.analyze(elements)
