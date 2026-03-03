"""
NAYA_CORE Cognition Module

Integrated cognitive system with:
- Advanced Intelligence (Multi-dimensional Reasoning)
- Perception Engine (Multi-domain Sensing)
- Adaptability (Context & Culture-aware Evolution)
- Humanization (Human-centric Communication)
- Multilingual Support (Native languages for forgotten markets)

This is the BRAIN of NAYA - intelligent, adaptive, culturally aware.
"""

# Core cognitive infrastructure
from NAYA_CORE.cognition.cognitive_intelligence_framework import (
    CognitiveFramework,
    AdvancedIntelligenceEngine,
    PerceptionEngine,
    AdaptabilityEngine,
    CognitiveState,
    ContextualInsight,
    CulturalMarketProfile,
    CognitionLevel,
    PerceptionDomain,
    AdaptationStrategy
)

# Multilingual & cultural capabilities
from NAYA_CORE.cognition.multilingual_cultural_engine import (
    MultilingualEngine,
    HumanizationEnhancedEngine,
    LanguageCapability,
    CulturalMessage,
    LocalMarketLanguageProfile,
    SupportedLanguage,
    CulturalCommunicationStyle
)

# Master cognitive hub
from NAYA_CORE.cognition.cognitive_hub import (
    CognitiveHubNAYA,
    get_cognitive_hub,
    CognitiveCapability
)

__version__ = "2.0.0"  # Enhanced cognitive framework

__all__ = [
    # Cognitive frameworks
    "CognitiveFramework",
    "AdvancedIntelligenceEngine",
    "PerceptionEngine",
    "AdaptabilityEngine",
    
    # Cognitive state
    "CognitiveState",
    "ContextualInsight",
    "CulturalMarketProfile",
    
    # Enums
    "CognitionLevel",
    "PerceptionDomain",
    "AdaptationStrategy",
    
    # Multilingual & humanization
    "MultilingualEngine",
    "HumanizationEnhancedEngine",
    "LanguageCapability",
    "CulturalMessage",
    "LocalMarketLanguageProfile",
    "SupportedLanguage",
    "CulturalCommunicationStyle",
    
    # Master hub
    "CognitiveHubNAYA",
    "get_cognitive_hub",
    "CognitiveCapability"
]

# Initialize cognitive hub on import
_HUB = get_cognitive_hub()
