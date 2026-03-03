"""
NAYA LLM INTEGRATION
LAYER 5 — ELITE DETECTION

Rôle :
- Détecter des opportunités premium → élite+
- Identifier des douleurs discrètes et solvables
- Ignorer le bruit public et les signaux déjà saturés
- Préparer la chasse stratégique haute valeur

Ce module ne décide pas.
Il détecte et classe.
"""

from typing import List, Dict


class EliteDetection:
    """
    Moteur de détection élite.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs simples pour maturation
        self.total_items_scanned = 0
        self.elite_candidates_found = 0
        self.rejected_noise = 0

    # ---------
    # PUBLIC API
    # ---------

    def detect(self, signals: List[str]) -> Dict[str, List[str]]:
        """
        Analyse des signaux et détecte les opportunités élite.

        Retourne :
        - 'elite'   : signaux à très haute valeur potentielle
        - 'premium' : signaux intéressants mais non exclusifs
        - 'ignored' : bruit ou signaux saturés
        """
        elite = []
        premium = []
        ignored = []

        for signal in signals:
            self.total_items_scanned += 1

            clean = self._clean(signal)
            if not clean:
                ignored.append(signal)
                self.rejected_noise += 1
                continue

            score = self._elite_score(clean)

            if score >= 0.75:
                elite.append(clean)
                self.elite_candidates_found += 1
            elif score >= 0.45:
                premium.append(clean)
            else:
                ignored.append(clean)
                self.rejected_noise += 1

        return {
            "elite": elite,
            "premium": premium,
            "ignored": ignored
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

    def _elite_score(self, text: str) -> float:
        """
        Évalue le potentiel élite d’un signal.

        Heuristiques :
        - discrétion
        - coût caché
        - complexité
        - solvabilité implicite
        """
        score = 0.0
        lower = text.lower()

        # Marqueurs de douleur discrète / élite
        elite_markers = [
            "coût caché",
            "processus interne",
            "risque réputationnel",
            "conformité",
            "audit",
            "inefficience",
            "temps perdu",
            "blocage silencieux",
            "complexité",
        ]

        for marker in elite_markers:
            if marker in lower:
                score += 0.15

        # Marqueurs de saturation (bruit public)
        saturation_markers = [
            "solution grand public",
            "outil générique",
            "tendance",
            "à la mode",
            "tout le monde",
        ]

        for marker in saturation_markers:
            if marker in lower:
                score -= 0.25

        # Longueur minimale pour signal sérieux
        if len(text) >= 35:
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

_elite_detection_instance = EliteDetection()


def detect_elite(signals: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour détection élite directe.
    """
    return _elite_detection_instance.detect(signals)
