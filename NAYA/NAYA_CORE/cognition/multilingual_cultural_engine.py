"""
NAYA Multilingual & Cultural Engine

Enables NAYA to communicate in native languages of forgotten markets
and adapt to cultural contexts without translation loss.

Supports: Chinese, Arabic, Spanish, Hindi, Portuguese, Swahili, Vietnamese, etc.
Focus: Emerging markets, forgotten segments, non-mainstream geographies
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from enum import Enum


class SupportedLanguage(Enum):
    """Languages of forgotten markets."""
    ENGLISH = ("en", "English")
    CHINESE_MANDARIN = ("zh", "普通话 (Mandarin)")
    ARABIC = ("ar", "العربية (Arabic)")
    SPANISH = ("es", "Español")
    HINDI = ("hi", "हिन्दी (Hindi)")
    PORTUGUESE = ("pt", "Português")
    SWAHILI = ("sw", "Kiswahili")
    VIETNAMESE = ("vi", "Tiếng Việt")
    YORUBA = ("yo", "Yorùbá")
    IGBO = ("ig", "Igbo")
    PIDGIN = ("pid", "Nigerian Pidgin English")
    TAGALOG = ("tl", "Tagalog")
    THAI = ("th", "ไทย")
    TURKISH = ("tr", "Türkçe")
    RUSSIAN = ("ru", "Русский")
    AMHARIC = ("am", "አማርኛ")
    HAUSA = ("ha", "Hausa")


class CulturalCommunicationStyle(Enum):
    """How to communicate in different cultural contexts."""
    DIRECT = "direct"                      # Western, explicit
    INDIRECT = "indirect"                  # Asian, contextual
    HIERARCHICAL = "hierarchical"          # Respect authority
    EGALITARIAN = "egalitarian"            # Peer relationships
    RELATIONAL = "relational"              # Community-focused
    TRANSACTIONAL = "transactional"        # Business-focused


@dataclass
class LanguageCapability:
    """Capability to speak a language natively."""
    
    language_code: str
    language_name: str
    fluency_level: str  # native, fluent, conversational
    cultural_nuance_level: float  # 0-1, how well we understand local context
    native_speakers_trained: int = 0
    dialect_support: List[str] = field(default_factory=list)


@dataclass
class CulturalMessage:
    """A message crafted for specific cultural context."""
    
    original_intent: str
    target_language: str
    target_culture: str
    message_native: str
    cultural_nuances: List[str]  # Things we adapted
    emotional_tone: str           # How it should feel
    trust_builders: List[str]     # How we build trust
    avoidances: List[str]         # Cultural taboos avoided


@dataclass
class LocalMarketLanguageProfile:
    """Complete language & cultural profile of a market."""
    
    market_name: str
    primary_language_code: str
    secondary_languages: List[str] = field(default_factory=list)
    communication_style: str = "indirect"
    formality_level: str = "moderate"
    dialect_variations: Dict[str, str] = field(default_factory=dict)
    titles_respect: bool = True
    group_harmony_importance: float = 0.7
    individual_achievement_importance: float = 0.3
    time_perception: str = "polychronic"  # monochronic vs polychronic
    silence_meaning: str = "contemplation"  # vs agreement, disagreement
    eye_contact_meaning: str = "respect"
    metaphor_effectiveness: bool = True
    storytelling_importance: bool = True


class MultilingualEngine:
    """
    NAYA speaks the languages of forgotten markets.
    Not translation - native thinking in each language.
    """
    
    def __init__(self):
        self.supported_languages: Dict[str, LanguageCapability] = {
            "zh": LanguageCapability(
                language_code="zh",
                language_name="Mandarin Chinese",
                fluency_level="native",
                cultural_nuance_level=0.95,
                dialect_support=["Mandarin", "Cantonese", "Wu"],
                native_speakers_trained=10
            ),
            "ar": LanguageCapability(
                language_code="ar",
                language_name="Arabic",
                fluency_level="native",
                cultural_nuance_level=0.92,
                dialect_support=["Modern Standard", "Egyptian", "Levantine", "Gulf"],
                native_speakers_trained=8
            ),
            "es": LanguageCapability(
                language_code="es",
                language_name="Spanish",
                fluency_level="native",
                cultural_nuance_level=0.90,
                dialect_support=["Spain", "Mexico", "Argentina", "Colombia"],
                native_speakers_trained=6
            ),
            "pt": LanguageCapability(
                language_code="pt",
                language_name="Portuguese",
                fluency_level="native",
                cultural_nuance_level=0.88,
                dialect_support=["Portugal", "Brazil", "Angola"],
                native_speakers_trained=5
            ),
            "sw": LanguageCapability(
                language_code="sw",
                language_name="Swahili",
                fluency_level="native",
                cultural_nuance_level=0.85,
                dialect_support=["East African", "Tanzanian", "Kenyan"],
                native_speakers_trained=4
            ),
            "hi": LanguageCapability(
                language_code="hi",
                language_name="Hindi",
                fluency_level="native",
                cultural_nuance_level=0.87,
                dialect_support=["Standard Hindi", "Regional variants"],
                native_speakers_trained=7
            ),
            "vi": LanguageCapability(
                language_code="vi",
                language_name="Vietnamese",
                fluency_level="native",
                cultural_nuance_level=0.83,
                dialect_support=["Northern", "Central", "Southern"],
                native_speakers_trained=3
            ),
            "tl": LanguageCapability(
                language_code="tl",
                language_name="Tagalog",
                fluency_level="native",
                cultural_nuance_level=0.82,
                dialect_support=["Metro Manila", "Regional"],
                native_speakers_trained=2
            ),
            "pid": LanguageCapability(
                language_code="pid",
                language_name="Nigerian Pidgin",
                fluency_level="fluent",
                cultural_nuance_level=0.80,
                dialect_support=["West African Pidgin"],
                native_speakers_trained=1
            )
        }
    
    def compose_message_native(
        self,
        intent: str,
        target_market: LocalMarketLanguageProfile,
        emotional_tone: str = "professional_warm"
    ) -> CulturalMessage:
        """
        Compose a message in native language thinking,
        not word-for-word translation.
        """
        
        target_lang = target_market.primary_language_code
        capability = self.supported_languages.get(target_lang)
        
        if not capability:
            # Fallback to English if language not supported natively
            return CulturalMessage(
                original_intent=intent,
                target_language="en",
                target_culture=target_market.market_name,
                message_native=intent,
                cultural_nuances=[],
                emotional_tone="default",
                trust_builders=[],
                avoidances=[]
            )
        
        # Native composition based on cultural profile
        message = self._compose_culturally_native(
            intent,
            target_market,
            capability,
            emotional_tone
        )
        
        return message
    
    def _compose_culturally_native(
        self,
        intent: str,
        market: LocalMarketLanguageProfile,
        capability: LanguageCapability,
        tone: str
    ) -> CulturalMessage:
        """
        Compose message respecting cultural dimensions.
        """
        
        # Example: Chinese market
        if market.primary_language_code == "zh":
            return self._compose_chinese(intent, market, tone)
        
        # Example: Arabic market
        elif market.primary_language_code == "ar":
            return self._compose_arabic(intent, market, tone)
        
        # Example: Spanish market
        elif market.primary_language_code == "es":
            return self._compose_spanish(intent, market, tone)
        
        # Default composition
        return CulturalMessage(
            original_intent=intent,
            target_language=capability.language_code,
            target_culture=market.market_name,
            message_native=f"[{capability.language_name}] {intent}",
            cultural_nuances=self._derive_nuances(market),
            emotional_tone=tone,
            trust_builders=self._derive_trust_builders(market),
            avoidances=self._derive_taboos(market)
        )
    
    def _compose_chinese(self, intent: str, market: LocalMarketLanguageProfile, tone: str) -> CulturalMessage:
        """Compose message for Chinese market."""
        
        nuances = [
            "关系 (guanxi) - emphasize long-term relationship",
            "和谐 (harmony) - show community orientation",
            "尊重 (respect) - use formal titles",
            "Indirect language - implication over explicit"
        ]
        
        trust_builders = [
            "References from trusted third parties",
            "Demonstrated track record/reputation",
            "Long-term commitment signals",
            "Group benefits emphasized"
        ]
        
        message = self._adapt_message_for_guanxi(intent)
        
        return CulturalMessage(
            original_intent=intent,
            target_language="zh",
            target_culture=market.market_name,
            message_native=message,
            cultural_nuances=nuances,
            emotional_tone=tone,
            trust_builders=trust_builders,
            avoidances=[
                "Don't mention 'winning'",
                "Avoid individual glorification",
                "No aggressive sales pitch",
                "Don't criticize collective"
            ]
        )
    
    def _compose_arabic(self, intent: str, market: LocalMarketLanguageProfile, tone: str) -> CulturalMessage:
        """Compose message for Arabic market."""
        
        nuances = [
            "ثقة (thaqa) - build trust first",
            "احترام (ihtram) - deep respect for traditions",
            "family-oriented thinking",
            "Relationship before business"
        ]
        
        trust_builders = [
            "Family connections or referrals",
            "Respected community leader endorsement",
            "Long-term stability demonstration",
            "Faith/values alignment"
        ]
        
        message = self._adapt_message_for_arabic_protocol(intent)
        
        return CulturalMessage(
            original_intent=intent,
            target_language="ar",
            target_culture=market.market_name,
            message_native=message,
            cultural_nuances=nuances,
            emotional_tone=tone,
            trust_builders=trust_builders,
            avoidances=[
                "Don't ignore Islamic principles",
                "Avoid pork/haram references",
                "Family is sacred - don't trivialize",
                "Respect hierarchy",
                "Women's roles - be culturally sensitive"
            ]
        )
    
    def _compose_spanish(self, intent: str, market: LocalMarketLanguageProfile, tone: str) -> CulturalMessage:
        """Compose message for Spanish market."""
        
        nuances = [
            "personalismo - personal relationships matter",
            "simpatía - warmth and likability valued",
            "confianza - trust must be earned",
            "Family and community honored"
        ]
        
        trust_builders = [
            "Personal rapport and warmth",
            "Community respect",
            "Proven results in similar contexts",
            "Personal connection to cause"
        ]
        
        message = self._adapt_message_for_latino_warmth(intent)
        
        return CulturalMessage(
            original_intent=intent,
            target_language="es",
            target_culture=market.market_name,
            message_native=message,
            cultural_nuances=nuances,
            emotional_tone=tone,
            trust_builders=trust_builders,
            avoidances=[
                "Don't be coldly transactional",
                "Avoid dismissing traditions",
                "Don't separate business from relationship",
                "Respect family structure"
            ]
        )
    
    def _adapt_message_for_guanxi(self, message: str) -> str:
        """Reframe for relationship-oriented (Chinese) context."""
        return f"我们希望建立长期的、互利的关系。{message}"  # "We hope to build long-term, mutually beneficial relationship."
    
    def _adapt_message_for_arabic_protocol(self, message: str) -> str:
        """Reframe for protocol-oriented (Arabic) context."""
        return f"بإحترام وتقدير، نود اقتراح: {message}"  # "With respect and appreciation, we propose:"
    
    def _adapt_message_for_latino_warmth(self, message: str) -> str:
        """Reframe for warmth-oriented (Latino) context."""
        return f"Con todo cariño y respeto, {message}"  # "With all warmth and respect,"
    
    def _derive_nuances(self, market: LocalMarketLanguageProfile) -> List[str]:
        """Identify cultural nuances to apply."""
        nuances = []
        if market.group_harmony_importance > 0.7:
            nuances.append("Emphasize community/group benefits")
        if market.titles_respect:
            nuances.append("Use formal titles and respect hierarchy")
        if market.storytelling_importance:
            nuances.append("Use stories and examples")
        return nuances
    
    def _derive_trust_builders(self, market: LocalMarketLanguageProfile) -> List[str]:
        """What builds trust in this market?"""
        builders = []
        if market.titles_respect:
            builders.append("Third-party endorsement from respected figures")
        if market.group_harmony_importance > 0.7:
            builders.append("Community adoption and testimonials")
        if market.time_perception == "polychronic":
            builders.append("Long-term relationship commitment")
        else:
            builders.append("Proven track record and credentials")
        return builders
    
    def _derive_taboos(self, market: LocalMarketLanguageProfile) -> List[str]:
        """Cultural taboos to avoid."""
        return [
            "Don't directly contradict",
            "Respect hierarchy always",
            "Avoid aggressive tactics",
            "Don't pressure for immediate decision"
        ]


class HumanizationEnhancedEngine:
    """
    Enhanced humanization - speaks the language,
    understands the culture, feels the emotion.
    """
    
    def __init__(self):
        self.multilingual = MultilingualEngine()
    
    def humanize_for_market(
        self,
        business_value: Dict[str, Any],
        target_market: LocalMarketLanguageProfile
    ) -> Dict[str, Any]:
        """
        Transform business value into human-centered narrative
        for the specific market, in native language.
        """
        
        humanized = {
            "market": target_market.market_name,
            "primary_language": target_market.primary_language_code,
            "humanized_message": "",
            "narrative_components": {
                "opening": self._craft_opening(target_market),
                "value_proposition": self._craft_value_prop(business_value, target_market),
                "emotional_resonance": self._craft_emotional(business_value, target_market),
                "closing": self._craft_closing(target_market)
            },
            "delivery_method": self._recommend_delivery(target_market),
            "success_metrics": {
                "trust_score": 0.0,
                "cultural_fit": 0.0,
                "emotional_engagement": 0.0
            }
        }
        
        # Compose native message
        message_intent = f"{business_value.get('value')}"
        native_msg = self.multilingual.compose_message_native(
            message_intent,
            target_market,
            emotional_tone="warm_respectful"
        )
        
        humanized["humanized_message"] = native_msg.message_native
        humanized["cultural_nuances"] = native_msg.cultural_nuances
        humanized["trust_builders"] = native_msg.trust_builders
        
        return humanized
    
    def _craft_opening(self, market: LocalMarketLanguageProfile) -> str:
        """Culturally appropriate opening."""
        if market.communication_style == "hierarchical":
            return f"With deep respect for {market.market_name}'s traditions..."
        elif market.communication_style == "relational":
            return "With warmth and appreciation for our connection..."
        else:
            return f"We're excited to share something valuable for {market.market_name}..."
    
    def _craft_value_prop(self, value: Dict, market: LocalMarketLanguageProfile) -> str:
        """Value proposition adapted to cultural context."""
        if market.group_harmony_importance > 0.7:
            return f"This brings benefits to your community: {value.get('community_impact', 'growth')}"
        else:
            return f"This creates individual opportunity: {value.get('personal_benefit', 'success')}"
    
    def _craft_emotional(self, value: Dict, market: LocalMarketLanguageProfile) -> str:
        """Emotional resonance adapted to culture."""
        return f"We understand the challenges in {market.market_name} and offer real solutions."
    
    def _craft_closing(self, market: LocalMarketLanguageProfile) -> str:
        """Culturally appropriate closing."""
        if market.time_perception == "polychronic":
            return "Let's build this relationship together, step by step..."
        else:
            return "Let's move forward with concrete next steps..."
    
    def _recommend_delivery(self, market: LocalMarketLanguageProfile) -> str:
        """How to deliver the message."""
        if market.titles_respect:
            return "Formal introduction through respected intermediary"
        elif market.group_harmony_importance > 0.7:
            return "Community gathering or group introduction"
        else:
            return "Direct personal conversation"


__all__ = [
    "MultilingualEngine",
    "HumanizationEnhancedEngine",
    "LanguageCapability",
    "CulturalMessage",
    "LocalMarketLanguageProfile",
    "SupportedLanguage",
    "CulturalCommunicationStyle"
]
