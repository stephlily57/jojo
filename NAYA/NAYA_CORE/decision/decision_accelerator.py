"""
Decision Accelerator - Accélère les décisions intelligemment

Responsabilité:
  - Détermine la vitesse optimale de décision basée sur confiance
  - Plus confiant = décide plus vite
  - Moins confiant = prend plus de temps
  - Jamais de compromise entre vitesse et qualité

Production: v1.0
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Any, Optional
from enum import Enum
from datetime import datetime


class DecisionSpeed(Enum):
    """Vitesse de prise de décision."""
    INSTANT = "INSTANT"            # < 0.5s, confiance très haute
    FAST = "FAST"                  # 1-2s, confiance haute
    NORMAL = "NORMAL"              # 3-5s, confiance modérée
    CAREFUL = "CAREFUL"            # 10-15s, confiance basse
    THOROUGH = "THOROUGH"          # 20-30s, confiance très basse
    BLOCKED = "BLOCKED"            # Pas de décision, attendre plus de contexte


@dataclass
class DecisionSpeedProfile:
    """Profil de vitesse pour une décision."""
    target_speed: DecisionSpeed
    time_budget: float                  # Secondes allouées
    confidence_threshold: float         # Confiance requise
    context_sources_needed: int         # Nombre sources à consulter
    parallelizable_work: int            # Nombre tâches parallèles
    
    def expected_total_time(self) -> float:
        """Temps total attendu (avec parallélisation)."""
        if self.parallelizable_work <= 1:
            return self.time_budget
        # Avec parallélisation
        return self.time_budget / (self.parallelizable_work ** 0.5)


@dataclass
class ContextSource:
    """Source de contexte pour enrichir la décision."""
    source_name: str
    priority: int                       # 1-5, 1=max priority
    expected_latency: float             # Secondes pour récupérer
    value_impact: float                 # 0-1, impact sur confiance
    availability: float = 1.0           # 0-1, % disponibilité


class DecisionAccelerator:
    """
    Accélérateur de décision intelligent.
    
    Principe:
      - Plus je suis confiant → décide plus vite
      - Moins je suis confiant → prends plus de temps
      - Jamais de faux choix entre vitesse et qualité
    
    Détermine:
      - Temps alloué à la décision
      - Sources de contexte à consulter
      - Que peut-on paralléliser
      - Où cut off les détails mineurs
    
    Usage:
      accelerator = DecisionAccelerator()
      
      profile = accelerator.plan_decision_speed(
          opportunity=opp,
          confidence=0.84
      )
      
      print(f"Target speed: {profile.target_speed.value}")
      print(f"Time budget: {profile.time_budget}s")
      print(f"Consult {profile.context_sources_needed} sources")
    
    Production: Ready
    """
    
    def __init__(self):
        # Contexte sources disponibles
        self.available_sources: Dict[str, ContextSource] = {
            "capital_reserve_check": ContextSource("Capital Check", 1, 0.1, 0.15),
            "market_context": ContextSource("Market Context", 1, 0.3, 0.20),
            "cognitive_hub_analysis": ContextSource("Cognitive Analysis", 2, 0.5, 0.25),
            "constitution_validation": ContextSource("Constitution Check", 1, 0.1, 0.10),
            "prediction_engine": ContextSource("Outcome Prediction", 2, 0.5, 0.25),
            "learning_patterns": ContextSource("Learning Patterns", 3, 0.5, 0.15),
            "team_consultation": ContextSource("Team Input", 4, 5.0, 0.10),
            "stakeholder_alignment": ContextSource("Stakeholder Check", 5, 10.0, 0.05),
        }
        
        self.speed_profiles: Dict[DecisionSpeed, DecisionSpeedProfile] = self._create_profiles()
        self.decision_history: List[Dict[str, Any]] = []
    
    def plan_decision_speed(
        self,
        opportunity: Dict[str, Any],
        confidence: float,
        time_constraint: Optional[float] = None,
        quality_requirement: str = "HIGH"
    ) -> DecisionSpeedProfile:
        """
        Planifie la vitesse optimale pour une décision.
        
        Args:
            opportunity: L'opportunité à évaluer
            confidence: Confiance initiale (0-1)
            time_constraint: Limite de temps (optionnel, en secondes)
            quality_requirement: "HIGH", "MEDIUM", "LOW"
        
        Returns:
            DecisionSpeedProfile avec vitesse et ressources allouées
        """
        
        # ÉTAPE 1: Détermine la vitesse basée sur confiance
        target_speed = self._determine_speed_from_confidence(confidence)
        
        # ÉTAPE 2: Ajuste pour contraintes de temps
        if time_constraint and time_constraint < 1.0:
            target_speed = DecisionSpeed.INSTANT
        elif time_constraint and time_constraint < 5.0:
            if target_speed == DecisionSpeed.THOROUGH:
                target_speed = DecisionSpeed.CAREFUL
        
        # ÉTAPE 3: Ajuste pour qualité requise
        if quality_requirement == "HIGH" and target_speed == DecisionSpeed.BLOCKED:
            target_speed = DecisionSpeed.THOROUGH
        elif quality_requirement == "LOW" and target_speed == DecisionSpeed.THOROUGH:
            target_speed = DecisionSpeed.CAREFUL
        
        # ÉTAPE 4: Crée le profile détaillé
        profile = self._create_profile_for_speed(target_speed, confidence)
        
        # ÉTAPE 5: Optimise les sources
        self._optimize_source_selection(profile)
        
        return profile
    
    def _determine_speed_from_confidence(self, confidence: float) -> DecisionSpeed:
        """Détermine la vitesse basée sur le niveau de confiance."""
        
        if confidence >= 0.95:
            return DecisionSpeed.INSTANT
        elif confidence >= 0.85:
            return DecisionSpeed.FAST
        elif confidence >= 0.70:
            return DecisionSpeed.NORMAL
        elif confidence >= 0.50:
            return DecisionSpeed.CAREFUL
        elif confidence >= 0.30:
            return DecisionSpeed.THOROUGH
        else:
            return DecisionSpeed.BLOCKED
    
    def _create_profiles(self) -> Dict[DecisionSpeed, DecisionSpeedProfile]:
        """Crée les profils de vitesse prédéfinis."""
        
        return {
            DecisionSpeed.INSTANT: DecisionSpeedProfile(
                target_speed=DecisionSpeed.INSTANT,
                time_budget=0.5,
                confidence_threshold=0.95,
                context_sources_needed=2,  # Juste essentiel
                parallelizable_work=3
            ),
            DecisionSpeed.FAST: DecisionSpeedProfile(
                target_speed=DecisionSpeed.FAST,
                time_budget=1.5,
                confidence_threshold=0.85,
                context_sources_needed=4,  # Sources clés
                parallelizable_work=6
            ),
            DecisionSpeed.NORMAL: DecisionSpeedProfile(
                target_speed=DecisionSpeed.NORMAL,
                time_budget=4.0,
                confidence_threshold=0.70,
                context_sources_needed=6,  # Sources importantes
                parallelizable_work=8
            ),
            DecisionSpeed.CAREFUL: DecisionSpeedProfile(
                target_speed=DecisionSpeed.CAREFUL,
                time_budget=12.0,
                confidence_threshold=0.50,
                context_sources_needed=7,  # Presque toutes
                parallelizable_work=5  # Moins de parallélisation
            ),
            DecisionSpeed.THOROUGH: DecisionSpeedProfile(
                target_speed=DecisionSpeed.THOROUGH,
                time_budget=25.0,
                confidence_threshold=0.30,
                context_sources_needed=8,  # Toutes les sources
                parallelizable_work=2  # Très sériel
            ),
            DecisionSpeed.BLOCKED: DecisionSpeedProfile(
                target_speed=DecisionSpeed.BLOCKED,
                time_budget=float('inf'),
                confidence_threshold=0.0,
                context_sources_needed=999,
                parallelizable_work=0
            )
        }
    
    def _create_profile_for_speed(
        self,
        speed: DecisionSpeed,
        confidence: float
    ) -> DecisionSpeedProfile:
        """Crée un profile détaillé pour une vitesse."""
        
        base = self.speed_profiles[speed]
        
        # Copie le profile
        profile = DecisionSpeedProfile(
            target_speed=base.target_speed,
            time_budget=base.time_budget,
            confidence_threshold=base.confidence_threshold,
            context_sources_needed=base.context_sources_needed,
            parallelizable_work=base.parallelizable_work
        )
        
        # Ajuste légèrement basé sur confiance
        if confidence > base.confidence_threshold:
            # Peut aller plus vite
            profile.time_budget *= 0.8
            profile.parallelizable_work = int(profile.parallelizable_work * 1.1)
        
        return profile
    
    def _optimize_source_selection(self, profile: DecisionSpeedProfile) -> None:
        """Choisit les meilleures sources à consulter."""
        
        # Tries les sources par ratio valeur/latence
        sources_ranked = sorted(
            self.available_sources.items(),
            key=lambda item: (item[1].value_impact / (item[1].expected_latency + 0.1)),
            reverse=True
        )
        
        # Sélectionne les N meilleures sources qu'on peut consulter en budget
        selected = []
        total_latency = 0.0
        
        for source_name, source in sources_ranked:
            if len(selected) >= profile.context_sources_needed:
                break
            
            if total_latency + source.expected_latency <= profile.time_budget * 0.7:
                selected.append((source_name, source))
                total_latency += source.expected_latency
        
        # Store pour utilisation
        profile.context_sources_needed = len(selected)
    
    def estimate_decision_quality(self, profile: DecisionSpeedProfile) -> float:
        """
        Estime la qualité de la décision pour ce profil.
        
        Basé sur:
          - Nombre de sources consultées
          - Temps disponible pour analyse
          - Parallélisation possible
        """
        
        # Score qualité = f(sources, time, parallelization)
        
        source_quality = min(1.0, profile.context_sources_needed / 8)  # 8 sources = max
        
        time_quality = min(1.0, profile.time_budget / 10)  # 10s = bon
        
        parallelization_quality = min(1.0, profile.parallelizable_work / 8)
        
        # Weighted average
        quality = (
            source_quality * 0.5 +
            time_quality * 0.3 +
            parallelization_quality * 0.2
        )
        
        return max(0.1, quality)  # Min 10% qualité
    
    def estimate_speed_performance(self, profile: DecisionSpeedProfile) -> Dict[str, Any]:
        """Estime les performance en vitesse et qualité."""
        
        if profile.target_speed == DecisionSpeed.INSTANT:
            speed_score = 1.0
            latency = 0.3
        elif profile.target_speed == DecisionSpeed.FAST:
            speed_score = 0.9
            latency = 1.2
        elif profile.target_speed == DecisionSpeed.NORMAL:
            speed_score = 0.7
            latency = 3.5
        elif profile.target_speed == DecisionSpeed.CAREFUL:
            speed_score = 0.4
            latency = 10.0
        elif profile.target_speed == DecisionSpeed.THOROUGH:
            speed_score = 0.1
            latency = 20.0
        else:
            speed_score = 0.0
            latency = float('inf')
        
        quality_score = self.estimate_decision_quality(profile)
        
        return {
            "speed_score": round(speed_score, 2),
            "quality_score": round(quality_score, 2),
            "estimated_latency": f"{latency:.1f}s",
            "tradeoff_ratio": round(speed_score / (quality_score + 0.1), 2),
            "recommendation": self._recommend_speed_choice(speed_score, quality_score)
        }
    
    def _recommend_speed_choice(self, speed_score: float, quality_score: float) -> str:
        """Recommande si ce choix de vitesse est bon."""
        
        if speed_score >= 0.8 and quality_score >= 0.8:
            return "✓ Optimal - Fast AND high quality"
        elif speed_score >= 0.7 and quality_score >= 0.7:
            return "✓ Good balance"
        elif speed_score > quality_score:
            return "⚠ Speed prioritized over quality"
        elif quality_score > speed_score:
            return "⚠ Quality prioritized over speed"
        else:
            return "? Unclear tradeoff"
    
    def record_decision(
        self,
        decision_id: str,
        profile: DecisionSpeedProfile,
        actual_time_taken: float,
        actual_quality: float
    ) -> Dict[str, Any]:
        """
        Enregistre une décision pour calibration future.
        
        Args:
            decision_id: ID de la décision
            profile: Le profile utilisé
            actual_time_taken: Temps réel utilisé
            actual_quality: Qualité réelle perçue (0-1)
        """
        
        record = {
            "decision_id": decision_id,
            "target_speed": profile.target_speed.value,
            "estimated_latency": profile.time_budget,
            "actual_time": actual_time_taken,
            "estimated_quality": self.estimate_decision_quality(profile),
            "actual_quality": actual_quality,
            "efficiency": (actual_quality / (actual_time_taken + 0.1)) if actual_time_taken > 0 else 0,
            "timestamp": datetime.now().timestamp()
        }
        
        self.decision_history.append(record)
        
        return {
            "speed_accuracy": f"{100 * (1 - abs(profile.time_budget - actual_time_taken) / profile.time_budget):.0f}%",
            "quality_achieved": f"{actual_quality:.0%}",
            "efficiency": f"{record['efficiency']:.3f} quality/second"
        }
    
    def get_acceleration_metrics(self) -> Dict[str, Any]:
        """Retourne les métriques d'accélération du système."""
        
        if not self.decision_history:
            return {"decisions_recorded": 0}
        
        recent = self.decision_history[-20:]  # Regarde les 20 dernières
        
        avg_time = sum(r["actual_time"] for r in recent) / len(recent)
        avg_quality = sum(r["actual_quality"] for r in recent) / len(recent)
        avg_efficiency = sum(r["efficiency"] for r in recent) / len(recent)
        
        # Amélioration au fil du temps
        improvement = 0.0
        if len(recent) >= 2:
            first_half = recent[:len(recent)//2]
            second_half = recent[len(recent)//2:]
            
            first_quality = sum(r["actual_quality"] for r in first_half) / len(first_half)
            second_quality = sum(r["actual_quality"] for r in second_half) / len(second_half)
            
            improvement = second_quality - first_quality
        
        return {
            "decisions_recorded": len(self.decision_history),
            "average_decision_time": f"{avg_time:.2f}s",
            "average_quality": f"{avg_quality:.0%}",
            "efficiency": f"{avg_efficiency:.3f}",
            "quality_improvement_trend": f"{improvement:+.1%}",
            "acceleration_factor": f"{1.0 / (avg_time / 10 + 0.1):.1f}x"
        }


# Singleton global
_accelerator: Optional[DecisionAccelerator] = None


def get_decision_accelerator() -> DecisionAccelerator:
    """Accès singleton à l'accélérateur de décision."""
    global _accelerator
    if _accelerator is None:
        _accelerator = DecisionAccelerator()
    return _accelerator


if __name__ == "__main__":
    # Test
    accelerator = DecisionAccelerator()
    
    # Test différents niveaux de confiance
    for conf in [0.95, 0.85, 0.70, 0.50, 0.30]:
        opp = {"name": f"Test {conf}", "value": 2_000_000}
        
        profile = accelerator.plan_decision_speed(opportunity=opp, confidence=conf)
        
        performance = accelerator.estimate_speed_performance(profile)
        
        print(f"\nConfidence {conf:.0%}:")
        print(f"  Speed: {profile.target_speed.value}")
        print(f"  Time budget: {profile.time_budget:.1f}s")
        print(f"  Performance: Speed {performance['speed_score']}, Quality {performance['quality_score']}")
