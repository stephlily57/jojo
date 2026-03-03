"""
NAYA LLM INTEGRATION
LAYER 2 — PRECISION & JUSTESSE

Rôle :
- Focaliser l’attention de Naya
- Réduire la dispersion cognitive
- Ajuster le niveau de précision selon le contexte
- Aider à viser juste sans rigidifier la pensée

Ce module ne décide pas.
Il affine, hiérarchise et clarifie.
"""

from typing import List, Dict


class PrecisionLayer:
    """
    Couche de précision cognitive.
    Autonome, stable, évolutive.
    """

    def __init__(self):
        # Indicateurs simples pour maturation future
        self.total_elements_processed = 0
        self.focused_elements_count = 0

    # ---------
    # PUBLIC API
    # ---------

    def apply(
        self,
        elements: List[str],
        context_level: str = "standard"
    ) -> Dict[str, List[str]]:
        """
        Applique une focalisation intelligente sur les éléments fournis.

        context_level :
        - 'standard'
        - 'premium'
        - 'elite'
        - 'elite_plus'

        Retourne :
        - 'focused' : éléments prioritaires
        - 'secondary' : éléments utiles mais non centraux
        """
        focused = []
        secondary = []

        for element in elements:
            self.total_elements_processed += 1

            clean = self._clean(element)

            if not clean:
                continue

            precision_score = self._evaluate_precision(clean, context_level)

            if precision_score >= 0.7:
                focused.append(clean)
                self.focused_elements_count += 1
            else:
                secondary.append(clean)

        return {
            "focused": focused,
            "secondary": secondary
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

    def _evaluate_precision(self, text: str, level: str) -> float:
        """
        Évalue la pertinence d’un élément selon le niveau visé.

        Plus le niveau est élevé, plus l’exigence de précision augmente.
        """
        score = 0.0
        length = len(text)

        # Base de pertinence
        if length >= 20:
            score += 0.4
        if length >= 40:
            score += 0.2

        lower = text.lower()

        # Indicateurs de précision stratégique
        precision_markers = [
            "objectif",
            "impact",
            "valeur",
            "priorité",
            "risque",
            "levier",
            "optimisation",
            "efficacité",
        ]

        for marker in precision_markers:
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

        # Normalisation entre 0.0 et 1.0
        if final_score > 1.0:
            final_score = 1.0
        if final_score < 0.0:
            final_score = 0.0

        return final_score


# =========================
# Fonction utilitaire simple
# =========================

_precision_layer_instance = PrecisionLayer()


def apply_precision(
    elements: List[str],
    context_level: str = "standard"
) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour application directe de la précision.
    """
    return _precision_layer_instance.apply(elements, context_level)
