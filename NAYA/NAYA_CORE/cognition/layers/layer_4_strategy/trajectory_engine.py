"""
NAYA LLM INTEGRATION
LAYER 4 — TRAJECTORY ENGINE

Rôle :
- Construire des trajectoires stratégiques
- Évaluer la cohérence des enchaînements
- Détecter les effets secondaires et ruptures
- Servir la stratégie long terme, le safe et Repurse

Ce module ne décide pas.
Il structure et évalue des trajectoires.
"""

from typing import List, Dict


class TrajectoryEngine:
    """
    Moteur de trajectoires stratégiques.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs simples pour maturation
        self.total_trajectories_evaluated = 0
        self.coherent_trajectories = 0
        self.fragile_trajectories = 0

    # ---------
    # PUBLIC API
    # ---------

    def build_and_evaluate(
        self,
        steps: List[str]
    ) -> Dict[str, List[str]]:
        """
        Évalue une trajectoire composée de plusieurs étapes.

        Retourne :
        - 'coherent' : étapes formant une trajectoire stable
        - 'fragile'  : étapes créant des ruptures ou incohérences
        - 'warnings' : alertes stratégiques générales
        """
        self.total_trajectories_evaluated += 1

        coherent = []
        fragile = []
        warnings = []

        previous_step = None

        for step in steps:
            clean = self._clean(step)
            if not clean:
                continue

            if previous_step is None:
                coherent.append(clean)
                previous_step = clean
                continue

            if self._is_coherent(previous_step, clean):
                coherent.append(clean)
            else:
                fragile.append(clean)

            previous_step = clean

        if fragile:
            self.fragile_trajectories += 1
            warnings.append("Ruptures détectées dans la trajectoire")

        if coherent and not fragile:
            self.coherent_trajectories += 1
            warnings.append("Trajectoire stratégique cohérente")

        return {
            "coherent": coherent,
            "fragile": fragile,
            "warnings": warnings
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

    def _is_coherent(self, previous: str, current: str) -> bool:
        """
        Vérifie la cohérence entre deux étapes consécutives.

        Heuristique :
        - continuité d’objectif
        - absence de contradiction temporelle
        """
        prev_lower = previous.lower()
        curr_lower = current.lower()

        # Marqueurs de rupture stratégique
        rupture_markers = [
            "abandon",
            "changement brutal",
            "sans continuité",
            "contradictoire",
            "retour en arrière",
        ]

        for marker in rupture_markers:
            if marker in curr_lower:
                return False

        # Continuité minimale : thème commun
        common_words = set(prev_lower.split()) & set(curr_lower.split())
        if len(common_words) >= 1:
            return True

        # Par défaut, cohérence prudente
        return True


# =========================
# Fonction utilitaire simple
# =========================

_trajectory_engine_instance = TrajectoryEngine()


def evaluate_trajectory(steps: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour évaluation directe d'une trajectoire stratégique.
    """
    return _trajectory_engine_instance.build_and_evaluate(steps)
