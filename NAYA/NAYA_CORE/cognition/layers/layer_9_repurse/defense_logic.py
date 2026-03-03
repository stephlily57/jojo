"""
NAYA LLM INTEGRATION
LAYER 9 — DEFENSE LOGIC

Rôle :
- Qualifier les menaces potentielles
- Prioriser la vigilance défensive
- Préparer des réponses adaptatives
- Renforcer la survie sans rigidifier

Ce module ne bloque rien.
Il observe, classe et prépare.
"""

from typing import List, Dict


class DefenseLogic:
    """
    Moteur de logique défensive.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs simples pour maturation
        self.total_signals_analyzed = 0
        self.low_threat_count = 0
        self.medium_threat_count = 0
        self.high_threat_count = 0

    # ---------
    # PUBLIC API
    # ---------

    def analyze(self, signals: List[str]) -> Dict[str, List[str]]:
        """
        Analyse des signaux liés à la défense et à la survie.

        Retourne :
        - 'low_threat'    : signaux nécessitant vigilance légère
        - 'medium_threat' : signaux à surveiller activement
        - 'high_threat'   : signaux critiques (information uniquement)
        - 'notes'         : observations générales
        """
        low_threat = []
        medium_threat = []
        high_threat = []
        notes = []

        for signal in signals:
            self.total_signals_analyzed += 1

            clean = self._clean(signal)
            if not clean:
                continue

            score = self._threat_score(clean)

            if score >= 0.75:
                high_threat.append(clean)
                self.high_threat_count += 1
            elif score >= 0.4:
                medium_threat.append(clean)
                self.medium_threat_count += 1
            else:
                low_threat.append(clean)
                self.low_threat_count += 1

        if high_threat:
            notes.append("Présence de signaux à menace élevée (information)")

        if medium_threat and not high_threat:
            notes.append("Menaces modérées nécessitant vigilance renforcée")

        if low_threat and not medium_threat and not high_threat:
            notes.append("Environnement défensif stable")

        return {
            "low_threat": low_threat,
            "medium_threat": medium_threat,
            "high_threat": high_threat,
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

    def _threat_score(self, text: str) -> float:
        """
        Évalue le niveau de menace potentiel.

        Heuristiques :
        - intention hostile implicite
        - surface d’exposition
        - capacité d’impact
        """
        score = 0.0
        lower = text.lower()

        # Marqueurs de menace élevée
        high_threat_markers = [
            "attaque",
            "intrusion",
            "exploitation",
            "compromission",
            "sabotage",
            "extorsion",
            "escalade",
        ]

        for marker in high_threat_markers:
            if marker in lower:
                score += 0.3

        # Marqueurs de menace modérée
        medium_threat_markers = [
            "tentative",
            "scan",
            "accès non autorisé",
            "anomalie",
            "comportement suspect",
            "faille potentielle",
        ]

        for marker in medium_threat_markers:
            if marker in lower:
                score += 0.15

        # Détail souvent corrélé à une analyse plus sérieuse
        if len(text) >= 45:
            score += 0.1

        # Normalisation
        if score > 1.0:
            score = 1.0
        if score < 0.0:
            score = 0.0

        return score


# =========================
# Fonction utilitaire simple
# =========================

_defense_logic_instance = DefenseLogic()


def analyze_defense(signals: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour analyse défensive directe.
    """
    return _defense_logic_instance.analyze(signals)
