"""
NAYA LLM INTEGRATION
LAYER 7 — HYBRID COGNITION

Rôle :
- Gérer une cognition parallèle (multi-axes)
- Maintenir la cohérence inter-axes
- Éviter la dispersion et les conflits internes
- Stabiliser la pensée sous charge cognitive

Ce module ne décide pas.
Il coordonne et harmonise.
"""

from typing import List, Dict


class HybridCognition:
    """
    Moteur de cognition hybride (parallèle).
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs simples pour maturation
        self.total_axes_processed = 0
        self.coherent_axes = 0
        self.conflicting_axes = 0

    # ---------
    # PUBLIC API
    # ---------

    def harmonize(self, axes: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """
        Harmonise plusieurs axes cognitifs.

        axes :
        - dictionnaire { nom_axe: [éléments] }

        Retourne :
        - 'harmonized' : éléments cohérents entre axes
        - 'conflicts'  : éléments en tension inter-axes
        - 'notes'      : observations générales
        """
        harmonized = []
        conflicts = []
        notes = []

        all_elements = []

        for axis_name, elements in axes.items():
            self.total_axes_processed += 1

            for element in elements:
                clean = self._clean(element)
                if not clean:
                    continue
                all_elements.append((axis_name, clean))

        seen = {}
        for axis_name, element in all_elements:
            key = element.lower()
            if key not in seen:
                seen[key] = [axis_name]
            else:
                seen[key].append(axis_name)

        for element_key, axis_list in seen.items():
            if len(axis_list) >= 2:
                harmonized.append(element_key)
                self.coherent_axes += 1
            else:
                conflicts.append(element_key)
                self.conflicting_axes += 1

        if conflicts:
            notes.append("Présence de tensions entre axes cognitifs")

        if harmonized and not conflicts:
            notes.append("Cognition hybride cohérente")

        return {
            "harmonized": harmonized,
            "conflicts": conflicts,
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

_hybrid_cognition_instance = HybridCognition()


def harmonize_cognition(axes: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour harmonisation directe
    de la cognition parallèle.
    """
    return _hybrid_cognition_instance.harmonize(axes)
