"""
NAYA LLM INTEGRATION
LAYER 1 — NOISE FILTER

Rôle :
- Identifier et qualifier le bruit cognitif
- Ignorer activement ce qui est non pertinent
- Préserver le signal réel et exploitable
- Servir la justesse, la précision, la stratégie, le safe et Repurse

Ce module ne supprime rien.
Il classe, isole et met hors champ.
"""

from typing import List, Dict


class NoiseFilter:
    """
    Filtre de bruit cognitif.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Métriques internes simples
        self.total_elements_seen = 0
        self.noise_classified = 0

    # ---------
    # PUBLIC API
    # ---------

    def filter(self, elements: List[str]) -> Dict[str, List[str]]:
        """
        Analyse une liste d'éléments textuels et les classe.

        Retourne un dictionnaire avec :
        - 'relevant' : éléments à conserver
        - 'ignored'  : bruit mis hors champ
        """
        relevant = []
        ignored = []

        for element in elements:
            self.total_elements_seen += 1

            clean = self._clean(element)

            if not clean:
                ignored.append(element)
                self.noise_classified += 1
                continue

            if self._is_noise(clean):
                ignored.append(clean)
                self.noise_classified += 1
            else:
                relevant.append(clean)

        return {
            "relevant": relevant,
            "ignored": ignored
        }

    # =========================
    # Internal logic
    # =========================

    def _clean(self, text: str) -> str:
        """
        Nettoyage basique :
        - strip
        - normalisation simple
        """
        if not isinstance(text, str):
            return ""

        return text.strip()

    def _is_noise(self, text: str) -> bool:
        """
        Détection simple du bruit.
        Le bruit est défini comme :
        - trop court
        - trop vague
        - sans impact décisionnel apparent
        """
        # Trop court → probablement décoratif
        if len(text) < 4:
            return True

        # Expressions vagues fréquentes (extensible)
        vague_markers = [
            "on verra",
            "peut-être",
            "en général",
            "globalement",
            "pas sûr",
            "à voir",
        ]

        lower = text.lower()

        for marker in vague_markers:
            if marker in lower:
                return True

        return False


# =========================
# Fonction utilitaire simple
# =========================

_noise_filter_instance = NoiseFilter()


def filter_noise(elements: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour filtrage direct du bruit.
    """
    return _noise_filter_instance.filter(elements)
