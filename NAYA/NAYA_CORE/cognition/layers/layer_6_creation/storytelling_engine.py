"""
NAYA LLM INTEGRATION
LAYER 6 — STORYTELLING ENGINE

Rôle :
- Structurer une narration claire et stratégique
- Adapter le niveau de discours (standard → élite+)
- Réduire le bruit narratif
- Mettre en avant l’essentiel sans sur-expliquer

Ce module ne décide pas.
Il structure et calibre le récit.
"""

from typing import List, Dict


class StorytellingEngine:
    """
    Moteur de storytelling stratégique.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs simples pour maturation
        self.total_items_processed = 0
        self.high_impact_outputs = 0
        self.low_noise_outputs = 0

    # ---------
    # PUBLIC API
    # ---------

    def build(
        self,
        elements: List[str],
        level: str = "standard"
    ) -> Dict[str, List[str]]:
        """
        Construit une narration structurée à partir d’éléments fournis.

        level :
        - 'standard'
        - 'premium'
        - 'elite'
        - 'elite_plus'

        Retourne :
        - 'core'      : messages centraux
        - 'support'   : éléments de soutien
        - 'discarded' : éléments narrativement faibles
        """
        core = []
        support = []
        discarded = []

        for element in elements:
            self.total_items_processed += 1

            clean = self._clean(element)
            if not clean:
                discarded.append(element)
                continue

            score = self._narrative_score(clean, level)

            if score >= 0.75:
                core.append(clean)
                self.high_impact_outputs += 1
            elif score >= 0.4:
                support.append(clean)
            else:
                discarded.append(clean)
                self.low_noise_outputs += 1

        return {
            "core": core,
            "support": support,
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

    def _narrative_score(self, text: str, level: str) -> float:
        """
        Évalue la force narrative d’un élément.

        Heuristiques :
        - clarté
        - précision
        - adéquation au niveau de valeur
        """
        score = 0.0
        length = len(text)

        # Base de clarté narrative
        if length >= 25:
            score += 0.3
        if length >= 50:
            score += 0.2

        lower = text.lower()

        # Marqueurs de narration stratégique
        narrative_markers = [
            "problème",
            "enjeu",
            "impact",
            "solution",
            "valeur",
            "différenciation",
            "résultat",
        ]

        for marker in narrative_markers:
            if marker in lower:
                score += 0.1

        # Ajustement selon le niveau
        level_modifier = {
            "standard": 1.0,
            "premium": 1.1,
            "elite": 1.2,
            "elite_plus": 1.3,
        }

        modifier = level_modifier.get(level, 1.0)
        final_score = score * modifier

        # Normalisation
        if final_score > 1.0:
            final_score = 1.0
        if final_score < 0.0:
            final_score = 0.0

        return final_score


# =========================
# Fonction utilitaire simple
# =========================

_storytelling_engine_instance = StorytellingEngine()


def build_storytelling(
    elements: List[str],
    level: str = "standard"
) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour construction directe du storytelling.
    """
    return _storytelling_engine_instance.build(elements, level)
