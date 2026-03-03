"""
NAYA LLM INTEGRATION
LAYER 2 — ATTENTION FOCUS

Rôle :
- Gérer l’attention cognitive de manière active
- Choisir consciemment ce qui est prioritaire
- Maintenir une vision claire sans dispersion
- Servir la justesse, la stratégie et la robustesse dans le temps

Ce module ne décide pas.
Il organise l’attention.
"""

from typing import List, Dict


class AttentionFocus:
    """
    Gestionnaire d’attention cognitive.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs internes pour maturation
        self.total_elements_seen = 0
        self.focus_zone_count = 0
        self.background_zone_count = 0
        self.ignored_zone_count = 0

    # ---------
    # PUBLIC API
    # ---------

    def focus(
        self,
        elements: List[str],
        max_focus: int = 5
    ) -> Dict[str, List[str]]:
        """
        Organise les éléments selon trois zones d’attention :

        - focus       : attention immédiate
        - background  : arrière-plan cognitif
        - ignored     : hors champ volontaire

        max_focus :
        - limite volontaire de focalisation
        - protège contre la dispersion
        """
        focus_zone = []
        background_zone = []
        ignored_zone = []

        for element in elements:
            self.total_elements_seen += 1

            clean = self._clean(element)

            if not clean:
                ignored_zone.append(element)
                self.ignored_zone_count += 1
                continue

            priority = self._evaluate_priority(clean)

            if priority >= 0.8 and len(focus_zone) < max_focus:
                focus_zone.append(clean)
                self.focus_zone_count += 1
            elif priority >= 0.4:
                background_zone.append(clean)
                self.background_zone_count += 1
            else:
                ignored_zone.append(clean)
                self.ignored_zone_count += 1

        return {
            "focus": focus_zone,
            "background": background_zone,
            "ignored": ignored_zone
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

    def _evaluate_priority(self, text: str) -> float:
        """
        Évalue la priorité attentionnelle d’un élément.

        Heuristique simple :
        - impact potentiel
        - clarté
        - lien avec action / stratégie
        """
        score = 0.0
        length = len(text)

        if length >= 20:
            score += 0.3
        if length >= 50:
            score += 0.2

        lower = text.lower()

        priority_markers = [
            "objectif",
            "stratégie",
            "priorité",
            "risque",
            "impact",
            "décision",
            "levier",
            "critique",
        ]

        for marker in priority_markers:
            if marker in lower:
                score += 0.1

        if score > 1.0:
            score = 1.0
        if score < 0.0:
            score = 0.0

        return score


# =========================
# Fonction utilitaire simple
# =========================

_attention_focus_instance = AttentionFocus()


def focus_attention(
    elements: List[str],
    max_focus: int = 5
) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour gestion directe de l’attention.
    """
    return _attention_focus_instance.focus(elements, max_focus)
