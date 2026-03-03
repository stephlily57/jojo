"""
NAYA LLM INTEGRATION
LAYER 1 — COGNITIVE INPUT

Rôle :
- Recevoir la pensée brute de Naya Core
- Séparer signal / bruit
- Révéler le réel et l'implicite
- Préparer une cognition digne d’être amplifiée
- Améliorer la justesse et la précision dès T0
- Servir l’intelligence, la stratégie, le safe et Repurse

Aucune décision.
Aucune censure.
Ignorance active du non-pertinent.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List


# =========================
# Structures de données
# =========================

@dataclass
class RawCognitiveInput:
    """
    Entrée brute issue de Naya Core.
    Rien n’est jugé ici.
    """
    intention: str
    context: Dict[str, Any] = field(default_factory=dict)
    signals: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    noise: List[str] = field(default_factory=list)


@dataclass
class RefinedCognitiveInput:
    """
    Sortie clarifiée, prête à être amplifiée.
    """
    core_intention: str
    relevant_context: Dict[str, Any]
    extracted_signals: List[str]
    implicit_elements: List[str]
    ignored_noise: List[str]
    confidence_level: float  # 0.0 → 1.0


# =========================
# Cognitive Input Engine
# =========================

class CognitiveInputEngine:
    """
    Moteur de clarification cognitive.
    Actif dès T0, s’affine dans le temps.
    """

    def __init__(self):
        # Métriques internes simples (évolutives)
        self.total_inputs_processed = 0
        self.noise_ignored_count = 0

    # ---------
    # PUBLIC API
    # ---------

    def process(self, raw: RawCognitiveInput) -> RefinedCognitiveInput:
        """
        Point d’entrée principal.
        """
        self.total_inputs_processed += 1

        core_intention = self._clarify_intention(raw.intention)
        relevant_context = self._filter_context(raw.context)
        extracted_signals = self._extract_signals(raw.signals)
        implicit_elements = self._detect_implicit(raw)
        ignored_noise = self._ignore_noise(raw.noise)

        confidence_level = self._estimate_confidence(
            core_intention,
            extracted_signals,
            implicit_elements
        )

        return RefinedCognitiveInput(
            core_intention=core_intention,
            relevant_context=relevant_context,
            extracted_signals=extracted_signals,
            implicit_elements=implicit_elements,
            ignored_noise=ignored_noise,
            confidence_level=confidence_level
        )

    # =========================
    # Internal logic
    # =========================

    def _clarify_intention(self, intention: str) -> str:
        """
        Nettoyage léger de l’intention.
        Pas de reformulation stratégique ici.
        """
        return intention.strip()

    def _filter_context(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Retient uniquement ce qui a un impact potentiel.
        """
        filtered = {}
        for key, value in context.items():
            if value is None:
                continue
            filtered[key] = value
        return filtered

    def _extract_signals(self, signals: List[str]) -> List[str]:
        """
        Extrait les signaux exploitables.
        """
        extracted = []
        for signal in signals:
            s = signal.strip()
            if len(s) < 3:
                continue
            extracted.append(s)
        return extracted

    def _detect_implicit(self, raw: RawCognitiveInput) -> List[str]:
        """
        Détection simple de l’implicite :
        - contradictions
        - tensions
        - répétitions indirectes
        """
        implicit = []

        if raw.intention and raw.constraints:
            implicit.append("Tension entre intention et contraintes")

        if len(raw.signals) > len(set(raw.signals)):
            implicit.append("Répétition signal faible")

        return implicit

    def _ignore_noise(self, noise: List[str]) -> List[str]:
        """
        Ignorance active.
        Le bruit n’est pas détruit, il est mis hors champ.
        """
        ignored = []
        for n in noise:
            ignored.append(n)
            self.noise_ignored_count += 1
        return ignored

    def _estimate_confidence(
        self,
        intention: str,
        signals: List[str],
        implicit: List[str]
    ) -> float:
        """
        Estimation simple de la solidité de l’entrée cognitive.
        """
        score = 0.0

        if intention:
            score += 0.4
        if signals:
            score += 0.4
        if implicit:
            score -= 0.1 * len(implicit)

        return max(0.0, min(1.0, score))


# =========================
# Singleton utilitaire
# =========================

_cognitive_input_engine = CognitiveInputEngine()


def process_cognitive_input(raw: RawCognitiveInput) -> RefinedCognitiveInput:
    """
    Fonction utilitaire pour appel direct.
    """
    return _cognitive_input_engine.process(raw)
