"""
NAYA LLM INTEGRATION
LAYER 9 — REPURSE EVOLUTION

Rôle :
- Renforcer la survie et la défense de Repurse
- Adapter la résilience aux contextes évolutifs
- Soutenir la continuité et la robustesse dans le temps
- Évoluer en parallèle de l’intelligence de Naya

Ce module ne bloque rien.
Il renforce, adapte et consolide.
"""

from typing import List, Dict


class RepurseEvolution:
    """
    Moteur d’évolution de Repurse.
    Autonome, stable, évolutif.
    """

    def __init__(self):
        # Indicateurs simples pour maturation
        self.total_events_observed = 0
        self.resilience_reinforced = 0
        self.vulnerabilities_identified = 0

    # ---------
    # PUBLIC API
    # ---------

    def evolve(self, events: List[str]) -> Dict[str, List[str]]:
        """
        Analyse des événements ou signaux liés à la sécurité / survie.

        Retourne :
        - 'reinforced'      : éléments renforçant la résilience
        - 'vulnerabilities' : zones à consolider
        - 'notes'           : observations générales
        """
        reinforced = []
        vulnerabilities = []
        notes = []

        for event in events:
            self.total_events_observed += 1

            clean = self._clean(event)
            if not clean:
                continue

            score = self._resilience_score(clean)

            if score >= 0.6:
                reinforced.append(clean)
                self.resilience_reinforced += 1
            else:
                vulnerabilities.append(clean)
                self.vulnerabilities_identified += 1

        if vulnerabilities:
            notes.append("Zones de résilience à renforcer identifiées")

        if reinforced and not vulnerabilities:
            notes.append("Résilience globale renforcée")

        return {
            "reinforced": reinforced,
            "vulnerabilities": vulnerabilities,
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

    def _resilience_score(self, text: str) -> float:
        """
        Évalue le potentiel de résilience d’un élément.

        Heuristiques :
        - adaptabilité
        - redondance
        - capacité de récupération
        """
        score = 0.0
        lower = text.lower()

        resilience_markers = [
            "redondance",
            "plan de secours",
            "résilience",
            "récupération",
            "adaptatif",
            "fallback",
            "continuité",
            "tolérance",
        ]

        for marker in resilience_markers:
            if marker in lower:
                score += 0.15

        # Marqueurs de fragilité
        fragility_markers = [
            "point unique",
            "fragile",
            "dépendance",
            "non redondant",
        ]

        for marker in fragility_markers:
            if marker in lower:
                score -= 0.2

        # Longueur indicative (souvent plus détaillée = meilleure analyse)
        if len(text) >= 40:
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

_repurse_evolution_instance = RepurseEvolution()


def evolve_repurse(events: List[str]) -> Dict[str, List[str]]:
    """
    Fonction utilitaire pour évolution directe de Repurse.
    """
    return _repurse_evolution_instance.evolve(events)
