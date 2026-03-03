"""
NAYA LLM INTEGRATION
LAYER 4 — STRATEGIC COGNITION

Rôle :
- Penser en trajectoires (pas en actions isolées)
- Évaluer des options sur la durée
- Anticiper effets secondaires et coûts différés
- Préparer des arbitrages stratégiques

Ce module ne décide pas.
Il structure la pensée stratégique.
"""

from typing import List, Dict


class StrategicCognition:
    """
    Moteur de cognition stratégique.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs simples pour maturation
        self.total_items_analyzed = 0
        self.trajectories_built = 0
        self.risk_flags_raised = 0

    # ---------
    # PUBLIC API
    # ---------

    def evaluate(self, options: List[str]) -> Dict[str, List[str]]:
        """
        Évalue des options sous un angle stratégique.

        Retourne :
        - 'viable'     : options cohérentes sur la durée
        - 'risky'      : options avec risques stratégiques
        - 'notes'      : observations stratégiques générales
        """
        viable = []
        risky = []
        notes = []

        for option in options:
            self.total_items_analyzed += 1

            clean = self._clean(option)
            if not clean:
                continue

            score = self._strategic_score(clean)

            if score >= 0.7:
                viable.append(clean)
                self.trajectories_built += 1
            else:
                risky.append(clean)
                self.risk_flags_raised += 1

        if risky:
            notes.append("Présence d’options à risque stratégique")

        if viable and not risky:
            notes.append("Trajectoires stratégiques cohérentes")

        return {
            "viable": viable,
            "risky": risky,
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

    def _strategic_score(self, text: str) -> float:
        """
        Évalue la solidité stratégique d’une option.

        Heuristiques simples :
        - horizon temporel
        - anticipation des risques
        - alignement long terme
        """
        score = 0.0
        lower = text.lower()

        # Indicateurs de vision long terme
        long_term_markers = [
            "long terme",
            "durable",
            "trajectoire",
            "positionnement",
            "avantage",
            "évolution",
            "scalable",
        ]

        for marker in long_term_markers:
            if marker in lower:
                score += 0.15

        # Indicateurs de risque stratégique
        risk_markers = [
            "court terme",
            "rapide mais",
            "sans vision",
            "dépendance",
            "fragile",
        ]

        for marker in risk_markers:
            if marker in lower:
                score -= 0.2

        # Longueur minimale pour réflexion stratégique
        if len(text) >= 30:
            score += 0.2

        # Normalisation
        if score > 1.0:
            score = 1.0
        if score < 0.0:
            score = 0.0

        return score


# =========================
# Fonction utilitaire simple
# =========================

_strategic_cognition_instance = StrategicCognition()


def evaluate_strategic_options(options: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour évaluation stratégique directe.
    """
    return _strategic_cognition_instance.evaluate(options)
