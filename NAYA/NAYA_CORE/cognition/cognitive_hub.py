"""
NAYA Cognition Module - Integrated Master Controller

Orchestrates all cognitive capabilities:
- Intelligence (Advanced Reasoning)
- Perception (Multi-dimensional Sensing)
- Adaptation (Context-aware Evolution)
- Humanization (Human-centric Communication)
- Multilingual (Native Language Support across Forgotten Markets)

This is the COGNITIVE BRAIN of NAYA.
"""

from dataclasses import dataclass
from typing import Dict, List, Any, Optional
from datetime import datetime

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

from NAYA_CORE.cognition.multilingual_cultural_engine import (
    MultilingualEngine,
    HumanizationEnhancedEngine,
    LocalMarketLanguageProfile,
    CulturalMessage
)


@dataclass
class CognitiveCapability:
    """A cognitive capability of NAYA."""
    name: str
    description: str
    maturity_level: str  # prototype, alpha, beta, production
    languages_supported: List[str]
    markets_optimized_for: List[str]


class CognitiveHubNAYA:
    """
    Master controller integrating all cognitive systems.
    
    This is what makes NAYA intelligent and human-compatible.
    """
    
    def __init__(self):
        """Initialize all cognitive subsystems."""
        
        # Core cognitive frameworks
        self.framework = CognitiveFramework()
        self.intelligence = AdvancedIntelligenceEngine()
        self.perception = PerceptionEngine()
        self.adaptability = AdaptabilityEngine()
        
        # Multilingual & humanization
        self.multilingual = MultilingualEngine()
        self.humanization = HumanizationEnhancedEngine()
        
        # Tracking
        self.processing_log: List[Dict] = []
        self.capability_registry: Dict[str, CognitiveCapability] = self._register_capabilities()
    
    def _register_capabilities(self) -> Dict[str, CognitiveCapability]:
        """Register all cognitive capabilities."""
        return {
            "advanced_reasoning": CognitiveCapability(
                name="Advanced Intelligence Engine",
                description="Multi-dimensional reasoning about opportunities",
                maturity_level="production",
                languages_supported=["logic", "mathematics"],
                markets_optimized_for=["all"]
            ),
            "perception": CognitiveCapability(
                name="Perception Engine",
                description="Multi-dimensional market perception",
                maturity_level="production",
                languages_supported=["signals", "context"],
                markets_optimized_for=["all"]
            ),
            "adaptability": CognitiveCapability(
                name="Adaptability Engine",
                description="Context and culture-aware adaptation",
                maturity_level="production",
                languages_supported=["cultural", "linguistic"],
                markets_optimized_for=["all"]
            ),
            "multilingual": CognitiveCapability(
                name="Multilingual Engine",
                description="Native language support for forgotten markets",
                maturity_level="production",
                languages_supported=[
                    "Mandarin", "Arabic", "Spanish", "Portuguese",
                    "Hindi", "Swahili", "Vietnamese", "Tagalog",
                    "Nigerian Pidgin", "Thai", "Turkish", "Russian"
                ],
                markets_optimized_for=[
                    "China", "Middle East", "Latin America", "Africa",
                    "Southeast Asia", "India", "Turkey", "Russia"
                ]
            ),
            "humanization": CognitiveCapability(
                name="Humanization Engine",
                description="Human-centric communication and narrative",
                maturity_level="production",
                languages_supported=["narrative", "emotion", "trust"],
                markets_optimized_for=["all"]
            )
        }
    
    def analyze_opportunity_for_market(
        self,
        opportunity: Dict[str, Any],
        market_profile: LocalMarketLanguageProfile
    ) -> Dict[str, Any]:
        """
        FULL COGNITIVE ANALYSIS:
        Intelligence + Perception + Adaptation + Humanization + Multilingual
        
        This is the master function that uses all 5 cognitive dimensions.
        """
        
        analysis_id = self._generate_analysis_id()
        
        analysis = {
            "analysis_id": analysis_id,
            "timestamp": datetime.utcnow().isoformat(),
            "opportunity": opportunity.get("id", "unknown"),
            "market": market_profile.market_name,
            "market_language": market_profile.primary_language_code,
            "cognitive_dimensions": {}
        }
        
        # Create cultural market profile for intelligence engine
        cultural_profile = CulturalMarketProfile(
            market_id=market_profile.market_name,
            market_name=market_profile.market_name,
            primary_language=market_profile.primary_language_code,
            cultural_values=self._extract_cultural_values(market_profile),
            communication_style=market_profile.communication_style,
            trust_drivers=self._extract_trust_drivers(market_profile),
            pain_points=opportunity.get("addresses", []),
            opportunity_patterns=opportunity.get("patterns", []),
            native_languages=market_profile.secondary_languages,
            adaptation_rules=market_profile.communication_style if isinstance(market_profile.communication_style, dict) else {}
        )
        
        # Dimension 1: Intelligence (Advanced Reasoning)
        print(f"[COGNITION] Analyzing opportunity {opportunity.get('id')} with INTELLIGENCE engine...")
        analysis["cognitive_dimensions"]["intelligence"] = \
            self.intelligence.reason_about_opportunity(
                opportunity,
                cultural_profile,
                CognitionLevel.STRATEGIC
            )
        
        # Dimension 2: Perception (Multi-sensory)
        print(f"[COGNITION] Perceiving market {market_profile.market_name} with PERCEPTION engine...")
        analysis["cognitive_dimensions"]["perception"] = \
            self.perception.perceive_market(cultural_profile)
        
        # Dimension 3: Adaptability (Context-adaptation)
        print(f"[COGNITION] Generating ADAPTATION plan for {market_profile.market_name}...")
        analysis["cognitive_dimensions"]["adaptability"] = \
            self.adaptability.generate_adaptation_plan(
                opportunity,
                cultural_profile,
                self.intelligence
            )
        
        # Dimension 4: Humanization (Human-centric)
        print(f"[COGNITION] HUMANIZING message for {market_profile.market_name}...")
        analysis["cognitive_dimensions"]["humanization"] = \
            self.humanization.humanize_for_market(opportunity, market_profile)
        
        # Dimension 5: Multilingual (Native languages)
        print(f"[COGNITION] Composing native message in {market_profile.primary_language_code}...")
        intent_message = f"Market opportunity: {opportunity.get('description', 'undefined')}"
        native_msg = self.multilingual.compose_message_native(
            intent_message,
            market_profile,
            emotional_tone="professional_warm"
        )
        analysis["cognitive_dimensions"]["multilingual"] = {
            "primary_language": market_profile.primary_language_code,
            "native_message": native_msg.message_native,
            "cultural_nuances_applied": native_msg.cultural_nuances,
            "trust_builders": native_msg.trust_builders,
            "cultural_taboos_avoided": native_msg.avoidances,
            "secondary_languages": market_profile.secondary_languages
        }
        
        # Synthesize: Final Recommendation
        analysis["final_recommendation"] = self._synthesize_recommendation(analysis)
        
        # Log
        self.processing_log.append(analysis)
        
        return analysis
    
    def _extract_cultural_values(self, market: LocalMarketLanguageProfile) -> List[str]:
        """Extract cultural values from market profile."""
        # Map market characteristics to cultural values
        values = []
        
        if market.group_harmony_importance > 0.7:
            values.append("community_oriented")
        if market.individual_achievement_importance > 0.6:
            values.append("achievement_driven")
        if market.titles_respect:
            values.append("hierarchy_respectful")
        if market.storytelling_importance:
            values.append("narrative_valued")
        
        return values
    
    def _extract_trust_drivers(self, market: LocalMarketLanguageProfile) -> List[str]:
        """Extract what drives trust in this market."""
        drivers = []
        
        if market.titles_respect:
            drivers.append("authority_endorsement")
        if market.group_harmony_importance > 0.7:
            drivers.append("community_adoption")
        if market.time_perception == "polychronic":
            drivers.append("long_term_commitment")
        else:
            drivers.append("proven_credentials")
        
        if market.primary_language_code in ["zh", "ar", "es"]:
            drivers.append("cultural_understanding")
        
        return drivers
    
    def _synthesize_recommendation(self, analysis: Dict) -> Dict[str, Any]:
        """Synthesize all cognitive dimensions into actionable recommendation."""
        
        intel = analysis["cognitive_dimensions"]["intelligence"]["holistic_assessment"]
        human = analysis["cognitive_dimensions"]["humanization"]
        multi = analysis["cognitive_dimensions"]["multilingual"]
        
        viability = intel.get("viability_score", 0.5)
        
        recommendation = {
            "timestamp": datetime.utcnow().isoformat(),
            "overall_viability_score": viability,
            "market_fit_score": intel["reasoning_dimensions"]["cultural"]["cultural_sensitivity_score"],
            "linguistic_readiness": 1.0 if multi["cultural_taboos_avoided"] else 0.6,
            "humanization_quality": "high" if human.get("trust_builders") else "medium",
            "final_verdict": "",
            "reasoning": [],
            "next_steps": [],
            "risk_factors": [],
            "cultural_opportunities": []
        }
        
        # Determine verdict
        if viability > 0.75 and recommendation["market_fit_score"] > 0.7:
            recommendation["final_verdict"] = "STRONG GO"
            recommendation["reasoning"].append("High viability meets excellent cultural fit")
        elif viability > 0.6 and recommendation["market_fit_score"] > 0.5:
            recommendation["final_verdict"] = "GO WITH CULTURAL OPTIMIZATION"
            recommendation["reasoning"].append("Good opportunity with cultural adaptation needed")
        elif viability > 0.4:
            recommendation["final_verdict"] = "PILOT - BUILD UNDERSTANDING FIRST"
            recommendation["reasoning"].append("Significant market/cultural factors to discover")
        else:
            recommendation["final_verdict"] = "HOLD"
            recommendation["reasoning"].append("Viability or fit concerns require resolution")
        
        # Add risk factors
        recommendation["risk_factors"] = intel["holistic_assessment"].get("primary_risks", [])
        
        # Add cultural opportunities
        if recommendation["market_fit_score"] > 0.7:
            recommendation["cultural_opportunities"].append("Leverage cultural alignment in messaging")
        if multi["cultural_taboos_avoided"]:
            recommendation["cultural_opportunities"].append("Cultural respect is strong advantage")
        if human.get("trust_builders"):
            recommendation["cultural_opportunities"].append("Trust-building levers identified")
        
        # Next steps
        recommendation["next_steps"] = [
            f"1. Engage native speakers of {multi['primary_language']}",
            f"2. Apply cultural nuances: {', '.join(multi['cultural_nuances_applied'][:2])}",
            f"3. Build trust through: {', '.join(human.get('trust_builders', ['credibility'])[:2])}",
            f"4. Avoid misconceptions: {', '.join(multi['cultural_taboos_avoided'][:2])}"
        ]
        
        return recommendation
    
    def _generate_analysis_id(self) -> str:
        """Generate unique analysis ID."""
        import hashlib
        timestamp = datetime.utcnow().isoformat()
        return hashlib.md5(timestamp.encode()).hexdigest()[:12]
    
    def get_capability_status(self) -> Dict[str, Any]:
        """Get status of all cognitive capabilities."""
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "total_capabilities": len(self.capability_registry),
            "capabilities": {
                name: {
                    "status": cap.maturity_level,
                    "languages": len(cap.languages_supported),
                    "markets": len(cap.markets_optimized_for)
                }
                for name, cap in self.capability_registry.items()
            },
            "processing_history": len(self.processing_log),
            "system_health": "operational"
        }
    
    def explain_reasoning(self, analysis_id: str) -> Optional[Dict]:
        """Retrieve and explain reasoning for a past analysis."""
        for log_entry in self.processing_log:
            if log_entry.get("analysis_id") == analysis_id:
                return {
                    "analysis_id": analysis_id,
                    "opportunity": log_entry["opportunity"],
                    "market": log_entry["market"],
                    "reasoning_chain": log_entry["cognitive_dimensions"]["intelligence"].get("reasoning_dimensions", {}),
                    "recommendation": log_entry.get("final_recommendation"),
                    "timestamp": log_entry["timestamp"]
                }
        return None


# Global singleton
_cognitive_hub = None

def get_cognitive_hub() -> CognitiveHubNAYA:
    """Get or create the global cognitive hub."""
    global _cognitive_hub
    if _cognitive_hub is None:
        _cognitive_hub = CognitiveHubNAYA()
    return _cognitive_hub


__all__ = [
    "CognitiveHubNAYA",
    "get_cognitive_hub",
    "CognitiveCapability",
    # Re-export from frameworks
    "CognitiveFramework",
    "AdvancedIntelligenceEngine",
    "PerceptionEngine",
    "AdaptabilityEngine",
    "MultilingualEngine",
    "HumanizationEnhancedEngine",
    "CognitionLevel",
    "PerceptionDomain",
    "AdaptationStrategy"
]
