"""
NAYA Business Model Engine

Crée et orchestre tous les modèles business:

1. CASH RAPIDE (€1k-150k, 24-72h)
   - Services bundlés: diagnostic, audit, chatbot
   - Premium floor: €1000 minimum
   - Deploy strategy: quick wins

2. HUNTING DISCRET (€10k-500k+)
   - Détecte les opportunités cachées
   - Services premium à haute valeur
   - Exécution confidentielle
   - Revenue sharing possible

3. PAIN & SILENCE (Market Intelligence)
   - Identifie problèmes explicites (PAIN)
   - Détecte opportunités non exploitées (SILENCE)
   - Score de marché et recommandations

Utilisé par EXECUTIVE_ARCHITECTURE pour validation & pricing.
"""

from .pain_silence_engine import (
    PainSilenceEngine,
    PainAnalyzer,
    SilenceAnalyzer,
    PainPoint,
    SilencePattern,
    PainLevel,
    SilenceType
)

from .business_hunter_engine import (
    BusinessHuntingOrchestrator,
    BusinessHunter,
    DiscreteOfferingBuilder,
    ExecutionExecutor,
    OpportunityScan,
    DiscreteService,
    OpportunitySignal,
    DiscreteServiceTier
)

__all__ = [
    # Pain & Silence
    'PainSilenceEngine',
    'PainAnalyzer',
    'SilenceAnalyzer',
    'PainPoint',
    'SilencePattern',
    'PainLevel',
    'SilenceType',

    # Business Hunting
    'BusinessHuntingOrchestrator',
    'BusinessHunter',
    'DiscreteOfferingBuilder',
    'ExecutionExecutor',
    'OpportunityScan',
    'DiscreteService',
    'OpportunitySignal',
    'DiscreteServiceTier'
]
