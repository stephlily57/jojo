"""
NAYA LLM INTEGRATION
LAYER 10 — MATURATION ENGINE

Rôle :
- Renforcer les capacités dans le temps
- Capitaliser les apprentissages
- Augmenter robustesse, intelligence et stratégie
- Soutenir l’évolution continue sans rigidité

Ce module ne bloque rien.
Il accumule, consolide et renforce.
"""

from typing import Dict, List


class MaturationEngine:
    """
    Moteur de maturation cognitive.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Capitalisation simple et explicite
        self.total_cycles = 0
        self.reinforced_patterns = []
        self.observed_weaknesses = []

    # ---------
    # PUBLIC API
    # ---------

    def mature(
        self,
        reinforced: List[str],
        weaknesses: List[str]
    ) -> Dict[str, List[str]]:
        """
        Capitalise sur ce qui fonctionne et ce qui doit être renforcé.

        Retourne :
        - 'capitalized' : éléments consolidés
        - 'to_reinforce': éléments à renforcer dans le temps
        - 'notes'       : observations générales
        """
        self.total_cycles += 1

        capitalized = []
        to_reinforce = []
        notes = []

        for item in reinforced:
            clean = self._clean(item)
            if not clean:
                continue
            capitalized.append(clean)
            if clean not in self.reinforced_patterns:
                self.reinforced_patterns.append(clean)

        for weakness in weaknesses:
            clean = self._clean(weakness)
            if not clean:
                continue
            to_reinforce.append(clean)
            if clean not in self.observed_weaknesses:
                self.observed_weaknesses.append(clean)

        if capitalized:
            notes.append("Capitalisation active des éléments solides")

        if to_reinforce:
            notes.append("Renforcement progressif requis sur certains points")

        if self.total_cycles > 5:
            notes.append("Maturation cumulative significative")

        return {
            "capitalized": capitalized,
            "to_reinforce": to_reinforce,
            "notes": notes
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


# =========================
# Fonction utilitaire simple
# =========================

_maturation_engine_instance = MaturationEngine()


def mature_system(
    reinforced: List[str],
    weaknesses: List[str]
) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour maturation directe du système.
    """
    return _maturation_engine_instance.mature(reinforced, weaknesses)
