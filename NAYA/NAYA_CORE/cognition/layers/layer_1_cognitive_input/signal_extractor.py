"""
NAYA LLM INTEGRATION
LAYER 1 — SIGNAL EXTRACTOR

Rôle :
- Extraire les signaux exploitables à partir d'éléments textuels
- Distinguer signal fort / signal faible
- Préparer la cognition stratégique, la chasse et la précision
- Réduire le bruit sans supprimer l'information

Aucune décision finale.
Aucune dépendance externe.
"""

from typing import List, Dict


class SignalExtractor:
    """
    Extracteur de signaux cognitifs.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Métriques simples (maturation possible)
        self.total_items_seen = 0
        self.strong_signals_count = 0
        self.weak_signals_count = 0

    # ---------
    # PUBLIC API
    # ---------

    def extract(self, elements: List[str]) -> Dict[str, List[str]]:
        """
        Analyse une liste d'éléments textuels et extrait les signaux.

        Retourne :
        - 'strong' : signaux à fort potentiel (impact / action)
        - 'weak'   : signaux faibles (indices, tendances, latents)
        """
        strong = []
        weak = []

        for element in elements:
            self.total_items_seen += 1

            clean = self._clean(element)

            if not clean:
                continue

            strength = self._evaluate_strength(clean)

            if strength == "strong":
                strong.append(clean)
                self.strong_signals_count += 1
            else:
                weak.append(clean)
                self.weak_signals_count += 1

        return {
            "strong": strong,
            "weak": weak
        }

    # =========================
    # Internal logic
    # =========================

    def _clean(self, text: str) -> str:
        """
        Nettoyage basique et sécurisé.
        """
        if not isinstance(text, str):
            return ""

        return text.strip()

    def _evaluate_strength(self, text: str) -> str:
        """
        Évalue la force d'un signal.

        Heuristique simple et sûre :
        - longueur
        - présence d'indicateurs d'impact
        """
        lower = text.lower()

        # Indicateurs d'impact fort (extensibles)
        impact_markers = [
            "coût",
            "risque",
            "perte",
            "blocage",
            "urgent",
            "critique",
            "conformité",
            "sécurité",
            "temps perdu",
            "inefficace",
            "problème récurrent",
        ]

        for marker in impact_markers:
            if marker in lower:
                return "strong"

        # Longueur significative → signal potentiellement fort
        if len(text) >= 40:
            return "strong"

        return "weak"


# =========================
# Fonction utilitaire simple
# =========================

_signal_extractor_instance = SignalExtractor()


def extract_signals(elements: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour extraction directe des signaux.
    """
    return _signal_extractor_instance.extract(elements)
