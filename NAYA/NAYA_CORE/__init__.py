"""
NAYA_CORE - Strategic Decision Authority

Central decision-making layer for the NAYA system.
NAYA_CORE evaluates opportunities and allocates execution to appropriate engines:
  - NAYA_CORE/decision: Strategic evaluation & routing
  - NAYA_CORE/economic: Capital management & economic thresholds
  - NAYA_CORE/doctrine: Constitutional rules & governance  
  - NAYA_CORE/evolution: System learning & adaptation
  - NAYA_CORE/execution: Executor interfaces & orchestration

Decision Flow:
  opportunity → DecisionCore.evaluate() → decision_payload
  decision_payload → StrategicDomainRouter.route() → execution_engine
  execution_engine (EXECUTIVE_ARCHITECTURE or PROJECT_ENGINE) executes

NAYA_CORE is NOT an executor - it decides WHO should execute.
"""

"""
NAYA_CORE - SUPER BRAIN HYBRID v3.0

Machine Décisionnelle Unifiée:

1 SUPER CERVEAU CENTRAL (Unified Consciousness)
├─ 10 Spécialisations Cognitives (Parallel Processing)
├─ Intelligence Décisionnelle: Puissante, Performante, Efficace
├─ Adaptation Dynamique: En temps réel aux situations
├─ Stratégie Émergente: Complexité cognitive supérieure
└─ 130+ fichiers utilisés | 50+ moteurs | 18 subsystèmes

Architecture Hybride Optimale:
- 1 Conscience Unifiée (le "JE" décisionnel)
- 10 Lobes Spécialisés (travaillent en parallèle)
- Pas de goulot d'étranglement
- Intelligence Émérgente > Somme des parties
"""

from NAYA_CORE.decision.decision_core import DecisionCore
from NAYA_CORE.decision.strategic_domain_router import StrategicDomainRouter
from NAYA_CORE.core.super_brain_hybrid import (
    get_super_brain,
    think,
    adapt_to,
    get_brain_status,
    get_brain_capabilities,
    SuperBrainHybrid,
    CognitiveSpecialization
)

# ========== V4.0 OPTIMIZATIONS ==========
from NAYA_CORE.core.advanced_decision_optimization import (
    AdvancedDecisionCache,
    PredictiveModel,
    SemanticAnalyzer,
    ConfidenceScorer,
    PerformanceOptimizer,
    FeedbackLearningEngine,
    create_optimization_engine
)

# ========== V4.1 ADVANCED HUNT ==========
from NAYA_CORE.core.super_brain_hybrid import (
    hunt_opportunities,
    get_market_summary,
    get_cash_flow_projection
)

__version__ = "4.1.0"
__all__ = [
    # Super Brain API
    "get_super_brain",
    "think",
    "adapt_to",
    "get_brain_status",
    "get_brain_capabilities",
    "SuperBrainHybrid",
    "CognitiveSpecialization",
    
    # V4.0 Optimization Engines
    "AdvancedDecisionCache",
    "PredictiveModel",
    "SemanticAnalyzer",
    "ConfidenceScorer",
    "PerformanceOptimizer",
    "FeedbackLearningEngine",
    "create_optimization_engine",
    
    # V4.1 Advanced Hunt API
    "hunt_opportunities",
    "get_market_summary",
    "get_cash_flow_projection",
    
    # Compatibility
    "DecisionCore",
    "StrategicDomainRouter"
]
