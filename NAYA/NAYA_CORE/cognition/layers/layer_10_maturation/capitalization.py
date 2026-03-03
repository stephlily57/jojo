"""
NAYA LLM INTEGRATION
LAYER 10 — CAPITALIZATION

Rôle :
- Capitaliser les éléments à forte valeur éprouvée
- Construire une mémoire stratégique exploitable
- Soutenir la continuité et la transmission interne
- Renforcer la cohérence dans le temps

Ce module ne bloque rien.
Il mémorise, consolide et transmet.
"""

from typing import Dict, List


class CapitalizationEngine:
    """
    Moteur de capitalisation stratégique.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Mémoire interne explicite
        self.total_entries = 0
        self.knowledge_base = {}
        self.high_value_items = []

    # ---------
    # PUBLIC API
    # ---------

    def capitalize(
        self,
        elements: List[str],
        context: str = "general"
    ) -> Dict[str, List[str]]:
        """
        Capitalise des éléments jugés utiles dans un contexte donné.

        Retourne :
        - 'stored'     : éléments mémorisés
        - 'reinforced' : éléments à haute valeur confirmée
        - 'notes'      : observations générales
        """
        stored = []
        reinforced = []
        notes = []

        if context not in self.knowledge_base:
            self.knowledge_base[context] = []

        for element in elements:
            clean = self._clean(element)
            if not clean:
                continue

            self.total_entries += 1
            stored.append(clean)
            self.knowledge_base[context].append(clean)

            if clean not in self.high_value_items:
                self.high_value_items.append(clean)
                reinforced.append(clean)

        if stored:
            notes.append("Capitalisation effectuée pour le contexte : " + context)

        if reinforced:
            notes.append("Nouveaux éléments à haute valeur capitalisés")

        return {
            "stored": stored,
            "reinforced": reinforced,
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

_capitalization_engine_instance = CapitalizationEngine()


def capitalize_knowledge(
    elements: List[str],
    context: str = "general"
) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour capitalisation directe.
    """
    return _capitalization_engine_instance.capitalize(elements, context)
