"""
NAYA LLM INTEGRATION
LAYER 5 — SIGNAL WEAKNESS

Rôle :
- Détecter et qualifier les signaux faibles
- Identifier les indices latents avant qu’ils deviennent visibles
- Distinguer émergence / bruit / répétition discrète
- Servir la chasse premium → élite+, la stratégie et le safe

Ce module ne décide pas.
Il observe, qualifie et prépare.
"""

from typing import List, Dict


class SignalWeaknessAnalyzer:
    """
    Analyseur de signaux faibles.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs simples pour maturation
        self.total_signals_seen = 0
        self.latent_detected = 0
        self.emerging_detected = 0
        self.noise_detected = 0

    # ---------
    # PUBLIC API
    # ---------

    def analyze(self, signals: List[str]) -> Dict[str, List[str]]:
        """
        Analyse des signaux textuels et les classe.

        Retourne :
        - 'latent'    : signaux faibles réels, encore cachés
        - 'emerging'  : signaux en phase d’émergence
        - 'noise'     : signaux faibles non exploitables
        """
        latent = []
        emerging = []
        noise = []

        for signal in signals:
            self.total_signals_seen += 1

            clean = self._clean(signal)
            if not clean:
                noise.append(signal)
                self.noise_detected += 1
                continue

            score = self._weak_signal_score(clean)

            if score >= 0.7:
                latent.append(clean)
                self.latent_detected += 1
            elif score >= 0.4:
                emerging.append(clean)
                self.emerging_detected += 1
            else:
                noise.append(clean)
                self.noise_detected += 1

        return {
            "latent": latent,
            "emerging": emerging,
            "noise": noise
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

    def _weak_signal_score(self, text: str) -> float:
        """
        Évalue la probabilité qu’un signal soit faible mais réel.

        Heuristiques :
        - absence de bruit public
        - répétition indirecte
        - inconfort latent
        - coût ou friction silencieuse
        """
        score = 0.0
        lower = text.lower()

        # Marqueurs de latence / non-dit
        latent_markers = [
            "difficile à mesurer",
            "peu visible",
            "rarement évoqué",
            "en interne",
            "officieux",
            "non priorisé",
            "contournement",
            "bricolage",
            "solution temporaire",
        ]

        for marker in latent_markers:
            if marker in lower:
                score += 0.15

        # Marqueurs d’émergence
        emerging_markers = [
            "commence à",
            "de plus en plus",
            "récemment",
            "nouvelle contrainte",
            "pression croissante",
        ]

        for marker in emerging_markers:
            if marker in lower:
                score += 0.1

        # Marqueurs de bruit faible (à ignorer)
        noise_markers = [
            "tendance",
            "buzz",
            "viral",
            "à la mode",
            "tout le monde en parle",
        ]

        for marker in noise_markers:
            if marker in lower:
                score -= 0.25

        # Longueur minimale pour crédibilité
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

_signal_weakness_analyzer_instance = SignalWeaknessAnalyzer()


def analyze_signal_weakness(signals: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour analyse directe des signaux faibles.
    """
    return _signal_weakness_analyzer_instance.analyze(signals)
