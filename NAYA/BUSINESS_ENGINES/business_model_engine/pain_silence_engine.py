"""
Pain & Silence Engine

Analyzes market pain points and customer silence patterns.
Identifies unspoken needs and unfulfilled opportunities.

Key Concepts:
- PAIN: Explicit customer complaints and identified problems
- SILENCE: Absence of discussion = unexplored opportunity
- DELTA: Gap between voiced need and available solutions
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from datetime import datetime
import statistics


class PainLevel(Enum):
    """Severity of customer pain."""
    CRITICAL = 5   # Business-threatening problem
    HIGH = 4       # Significant operational issue
    MEDIUM = 3     # Noticeable problem
    LOW = 2        # Minor friction
    NONE = 1       # No pain detected


class SilenceType(Enum):
    """Type of market silence detected."""
    UNUSED_FEATURE = "unused_feature"          # Feature exists but unused
    UNADDRESSED_NEED = "unaddressed_need"      # Need never discussed
    EMERGING_TREND = "emerging_trend"          # Trend starting to appear
    COMPETITIVE_BLIND_SPOT = "competitive_gap"  # Competitors don't serve
    CULTURAL_BARRIER = "cultural_barrier"      # Taboo or uncomfortable topic


@dataclass
class PainPoint:
    """Represents a specific customer pain."""

    pain_id: str
    description: str
    affected_segment: str
    pain_level: PainLevel
    frequency: int              # How often mentioned
    intensity: float            # 0-1 scale
    supporting_evidence: List[str]
    potential_market_size: int
    potential_revenue: float

    def get_score(self) -> float:
        """Calculate pain point score (0-100)."""
        return (
            (self.pain_level.value / 5) * 40 +
            (min(self.frequency, 10) / 10) * 30 +
            (self.intensity) * 20 +
            (min(self.potential_revenue / 100000, 1)) * 10
        )


@dataclass
class SilencePattern:
    """Represents market silence (absence, unexplored territory)."""

    silence_id: str
    topic: str
    silence_type: SilenceType
    time_silent: int            # Days of silence
    affected_segment: str
    adjacent_market_size: int
    estimated_opportunity: float
    confidence_score: float     # 0-1, how confident this is real opportunity

    def get_opportunity_score(self) -> float:
        """Calculate opportunity score (0-100)."""
        return (
            (self.confidence_score) * 50 +
            (min(self.time_silent / 365, 1)) * 30 +
            (min(self.estimated_opportunity / 1000000, 1)) * 20
        )


class PainAnalyzer:
    """Analyzes explicit pain points from market feedback."""

    def __init__(self):
        self.pain_points: Dict[str, PainPoint] = {}
        self.pain_trends = []

    def detect_pain(
        self,
        description: str,
        segment: str,
        evidence: List[str],
        market_potential: int
    ) -> PainPoint:
        """Detect and register a pain point."""

        # Analyze severity from language
        level = self._assess_pain_level(description)
        intensity = self._estimate_intensity(evidence)
        frequency = len(evidence)

        pain = PainPoint(
            pain_id=f"pain:{segment}:{len(self.pain_points)}",
            description=description,
            affected_segment=segment,
            pain_level=level,
            frequency=frequency,
            intensity=intensity,
            supporting_evidence=evidence,
            potential_market_size=market_potential,
            potential_revenue=market_potential * (intensity * 0.7)  # revenue estimate
        )

        self.pain_points[pain.pain_id] = pain
        return pain

    def _assess_pain_level(self, description: str) -> PainLevel:
        """Assess pain severity from description language."""

        critical_words = ['critical', 'broken', 'failed', 'impossible', 'useless']
        high_words = ['difficult', 'frustrating', 'slow', 'complex', 'error']
        medium_words = ['confusing', 'annoying', 'slow', 'cumbersome']

        desc_lower = description.lower()

        if any(w in desc_lower for w in critical_words):
            return PainLevel.CRITICAL
        elif any(w in desc_lower for w in high_words):
            return PainLevel.HIGH
        elif any(w in desc_lower for w in medium_words):
            return PainLevel.MEDIUM
        elif any(w in desc_lower for w in ['issue', 'problem']):
            return PainLevel.LOW
        else:
            return PainLevel.NONE

    def _estimate_intensity(self, evidence: List[str]) -> float:
        """Estimate intensity from evidence quality."""
        # More evidence = more intense problem
        return min(1.0, len(evidence) / 10)

    def get_top_pain_points(self, limit: int = 10) -> List[PainPoint]:
        """Get highest-scoring pain points."""
        sorted_pain = sorted(
            self.pain_points.values(),
            key=lambda p: p.get_score(),
            reverse=True
        )
        return sorted_pain[:limit]

    def get_pain_by_segment(self, segment: str) -> List[PainPoint]:
        """Get pain points for specific segment."""
        return [
            p for p in self.pain_points.values()
            if p.affected_segment == segment
        ]

    def get_pain_statistics(self) -> Dict[str, Any]:
        """Get overall pain statistics."""
        if not self.pain_points:
            return {'total_pain_points': 0}

        scores = [p.get_score() for p in self.pain_points.values()]
        levels = [p.pain_level for p in self.pain_points.values()]

        return {
            'total_pain_points': len(self.pain_points),
            'avg_score': statistics.mean(scores),
            'max_score': max(scores),
            'critical_count': sum(1 for l in levels if l == PainLevel.CRITICAL),
            'total_market_impact': sum(p.potential_revenue for p in self.pain_points.values())
        }


class SilenceAnalyzer:
    """Identifies market silence (unexplored opportunities)."""

    def __init__(self):
        self.silence_patterns: Dict[str, SilencePattern] = {}
        self.emergence_signals = []

    def detect_silence(
        self,
        topic: str,
        silence_type: SilenceType,
        silence_age_days: int,
        segment: str,
        opportunity_estimate: float,
        confidence: float
    ) -> SilencePattern:
        """Detect market silence pattern."""

        silence = SilencePattern(
            silence_id=f"silence:{topic}:{len(self.silence_patterns)}",
            topic=topic,
            silence_type=silence_type,
            time_silent=silence_age_days,
            affected_segment=segment,
            adjacent_market_size=int(opportunity_estimate / 0.3),
            estimated_opportunity=opportunity_estimate,
            confidence_score=confidence
        )

        self.silence_patterns[silence.silence_id] = silence
        return silence

    def get_top_opportunities(self, limit: int = 10) -> List[SilencePattern]:
        """Get highest-potential unexplored opportunities."""
        sorted_silence = sorted(
            self.silence_patterns.values(),
            key=lambda s: s.get_opportunity_score(),
            reverse=True
        )
        return sorted_silence[:limit]

    def get_silence_statistics(self) -> Dict[str, Any]:
        """Get overall silence statistics."""
        if not self.silence_patterns:
            return {'total_silence_patterns': 0}

        scores = [s.get_opportunity_score() for s in self.silence_patterns.values()]

        return {
            'total_opportunities': len(self.silence_patterns),
            'avg_opportunity_score': statistics.mean(scores),
            'highest_opportunity': max(scores),
            'total_addressable_market': sum(s.estimated_opportunity for s in self.silence_patterns.values())
        }


class PainSilenceEngine:
    """
    Complete Pain & Silence Analysis Engine

    Identifies both explicit problems AND unexplored opportunities.
    """

    def __init__(self):
        self.pain_analyzer = PainAnalyzer()
        self.silence_analyzer = SilenceAnalyzer()
        self.recommendations = []

    def analyze_market(
        self,
        market_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Complete market analysis with pain and silence detection."""

        # Would integrate real market data sources

        pain_stats = self.pain_analyzer.get_pain_statistics()
        silence_stats = self.silence_analyzer.get_silence_statistics()

        return {
            'analysis_timestamp': datetime.utcnow().isoformat(),
            'pain_analysis': pain_stats,
            'silence_analysis': silence_stats,
            'top_pain_points': [
                {
                    'id': p.pain_id,
                    'description': p.description,
                    'score': p.get_score(),
                    'market_opportunity': p.potential_revenue
                }
                for p in self.pain_analyzer.get_top_pain_points(5)
            ],
            'top_opportunities': [
                {
                    'id': s.silence_id,
                    'topic': s.topic,
                    'score': s.get_opportunity_score(),
                    'addressable_market': s.estimated_opportunity
                }
                for s in self.silence_analyzer.get_top_opportunities(5)
            ]
        }

    def generate_solutions(
        self,
        pain_point: PainPoint
    ) -> List[Dict[str, Any]]:
        """Generate potential solutions for a pain point."""

        solutions = []

        # For each pain level, suggest different approaches
        if pain_point.pain_level == PainLevel.CRITICAL:
            solutions.append({
                'type': 'alternative',
                'description': 'Consider complete workflow redesign'
            })

        if pain_point.intensity > 0.7:
            solutions.append({
                'type': 'tooling',
                'description': 'Build specialized tools/automations'
            })

        solutions.append({
            'type': 'integration',
            'description': 'Integrate with complementary solutions'
        })

        return solutions


__all__ = [
    'PainSilenceEngine',
    'PainAnalyzer',
    'SilenceAnalyzer',
    'PainPoint',
    'SilencePattern',
    'PainLevel',
    'SilenceType'
]
