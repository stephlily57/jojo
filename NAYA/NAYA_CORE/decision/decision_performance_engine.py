"""
Decision Performance Engine - Mesure la qualité des décisions NAYA

Responsabilité:
  - Mesurer accuracy (bonnes décisions vs résultats)
  - Mesurer speed (latence décisionnelle)
  - Mesurer efficiency (ROI des décisions)
  - Mesurer learning velocity (amélioration dans le temps)
  - Calculer adaptability score

Production: v1.0
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from enum import Enum


class PerformanceMetric(Enum):
    """Métriques de performance tracées."""
    ACCURACY = "accuracy"                    # % bonnes décisions
    SPEED = "speed"                          # Latence decision
    EFFICIENCY = "efficiency"                # ROI / value
    LEARNING_VELOCITY = "learning_velocity"  # Amélioration taux
    ADAPTABILITY = "adaptability"            # Capacité adapter
    CONFIDENCE_CALIBRATION = "confidence_calibration"  # Confiance vs réalité


@dataclass
class DecisionRecord:
    """Record d'une décision faite et son outcome."""
    decision_id: str
    timestamp: float                         # Unix timestamp
    opportunity: Dict[str, Any]
    
    # Decision metadata
    decision_payload: Dict[str, Any]
    predicted_outcome: float                 # Score attendu (0-1)
    confidence: float                        # Confiance initiale (0-1)
    decision_speed: float                    # Secondes pour décider
    
    # Actual outcome
    actual_outcome: Optional[float] = None   # Score réel (0-1)
    outcome_timestamp: Optional[float] = None
    status: str = "PENDING"                  # PENDING, COMPLETED, FAILED, LEARNING
    
    # Analysis
    accuracy_error: Optional[float] = None   # abs(predicted - actual)
    efficiency_score: Optional[float] = None # Valeur créée / effort
    adaptations_applied: Optional[int] = 0   # Nombre adaptations


@dataclass
class PerformanceMetrics:
    """Agrégation des performances."""
    period: str                              # "DAILY", "WEEKLY", "TOTAL"
    
    accuracy: float = 0.0                    # % bonnes décisions
    speed: float = 0.0                       # Vitesse vs référence
    efficiency: float = 0.0                  # ROI
    learning_velocity: float = 0.0           # Taux amélioration
    adaptability_score: float = 0.0          # Capacité adaptation
    confidence_calibration: float = 0.0      # Confiance vs réalité
    
    # Metadata
    decision_count: int = 0
    successful_count: int = 0
    failed_count: int = 0
    average_confidence: float = 0.0
    average_speed: float = 0.0
    
    # Trend
    trend_direction: str = "STABLE"          # UP, DOWN, STABLE
    improvement_percentage: float = 0.0      # % amélioration vs période précédente
    
    timestamp: float = field(default_factory=lambda: datetime.now().timestamp())


class DecisionPerformanceEngine:
    """
    Moteur de mesure et d'analyse de performance décisionnelle.
    
    Responsabilité:
      ✓ Enregistre chaque décision et son outcome
      ✓ Calcule les métriques de performance
      ✓ Détecte les patterns et trends
      ✓ Fournit feedback pour amélioration
      ✓ Calibre la confiance
    
    Usage:
      engine = DecisionPerformanceEngine()
      
      # Enregistre une décision
      engine.record_decision(
          decision_id="PROJ_001",
          opportunity={...},
          decision_payload={...},
          predicted_outcome=0.78,
          confidence=0.84,
          decision_speed=2.1
      )
      
      # Plus tard, enregistre l'outcome réel
      engine.record_outcome("PROJ_001", actual_outcome=0.82)
      
      # Obtient performances
      metrics = engine.get_performance_metrics(period="TOTAL")
      print(f"Accuracy: {metrics.accuracy}")  # 0.87
    """
    
    def __init__(self):
        self.decisions: Dict[str, DecisionRecord] = {}
        self.performance_history: List[PerformanceMetrics] = []
        self.performance_cache: Optional[PerformanceMetrics] = None
        self._cache_valid = False
        
    def record_decision(
        self,
        decision_id: str,
        opportunity: Dict[str, Any],
        decision_payload: Dict[str, Any],
        predicted_outcome: float,
        confidence: float,
        decision_speed: float,
        adaptations_applied: int = 0
    ) -> DecisionRecord:
        """
        Enregistre une décision faite.
        
        Args:
            decision_id: ID unique de la décision
            opportunity: Opportunité évaluée
            decision_payload: Résultat de la décision
            predicted_outcome: Score attendu (0-1)
            confidence: Confiance dans la décision (0-1)
            decision_speed: Temps pour décider (secondes)
            adaptations_applied: Nombre d'adaptations appliquées
        
        Returns:
            DecisionRecord enregistrement créé
        """
        record = DecisionRecord(
            decision_id=decision_id,
            timestamp=datetime.now().timestamp(),
            opportunity=opportunity,
            decision_payload=decision_payload,
            predicted_outcome=predicted_outcome,
            confidence=confidence,
            decision_speed=decision_speed,
            adaptations_applied=adaptations_applied,
            status="PENDING"
        )
        
        self.decisions[decision_id] = record
        self._cache_valid = False
        return record
    
    def record_outcome(
        self,
        decision_id: str,
        actual_outcome: float,
        success: bool = True
    ) -> DecisionRecord:
        """
        Enregistre le résultat réel d'une décision.
        
        Args:
            decision_id: ID de la décision
            actual_outcome: Score réel (0-1)
            success: Succès ou échec?
        
        Returns:
            DecisionRecord mis à jour
        """
        if decision_id not in self.decisions:
            raise ValueError(f"Decision {decision_id} not found")
        
        record = self.decisions[decision_id]
        record.actual_outcome = actual_outcome
        record.outcome_timestamp = datetime.now().timestamp()
        record.status = "COMPLETED" if success else "FAILED"
        
        # Calcule l'erreur de prédiction
        record.accuracy_error = abs(record.predicted_outcome - actual_outcome)
        
        # Calcule efficiency
        value = record.opportunity.get("value", 1.0)
        if value > 0:
            record.efficiency_score = actual_outcome / (1 + record.decision_speed)
        
        self._cache_valid = False
        return record
    
    def get_performance_metrics(self, period: str = "TOTAL") -> PerformanceMetrics:
        """
        Calcule les métriques de performance.
        
        Args:
            period: "DAILY", "WEEKLY", "TOTAL"
        
        Returns:
            PerformanceMetrics agrégées
        """
        # Filtre les décisions selon la période
        decisions = self._filter_by_period(period)
        
        if not decisions:
            return PerformanceMetrics(period=period)
        
        # Décisions avec outcomes
        completed = [d for d in decisions if d.status == "COMPLETED"]
        failed = [d for d in decisions if d.status == "FAILED"]
        
        # Calcule accuracy
        accuracy = 0.0
        if completed:
            errors = [d.accuracy_error for d in completed if d.accuracy_error is not None]
            if errors:
                # Accuracy basée sur erreur moyenne
                mean_error = sum(errors) / len(errors)
                accuracy = max(0.0, 1.0 - mean_error)
        
        # Calcule speed (normalisé: 2s = référence 1.0)
        speed = 1.0
        if decisions:
            avg_speed = sum(d.decision_speed for d in decisions) / len(decisions)
            speed = max(0.1, 2.0 / avg_speed)  # Inverse: rapide = score élevé
            speed = min(1.0, speed)
        
        # Calcule efficiency
        efficiency = 0.0
        if completed:
            eff_scores = [d.efficiency_score for d in completed if d.efficiency_score]
            if eff_scores:
                efficiency = sum(eff_scores) / len(eff_scores)
        
        # Calcule learning velocity (amélioration dans le temps)
        learning_velocity = self._calculate_learning_velocity(decisions, period)
        
        # Calcule adaptability (% decisions avec adaptations appliquées)
        adaptability_score = 0.0
        if decisions:
            with_adaptations = sum(1 for d in decisions if d.adaptations_applied > 0)
            adaptability_score = with_adaptations / len(decisions)
        
        # Calcule confidence calibration
        confidence_calibration = self._calculate_confidence_calibration(completed)
        
        # Crée les métriques
        metrics = PerformanceMetrics(
            period=period,
            accuracy=accuracy,
            speed=speed,
            efficiency=efficiency,
            learning_velocity=learning_velocity,
            adaptability_score=adaptability_score,
            confidence_calibration=confidence_calibration,
            decision_count=len(decisions),
            successful_count=len(completed),
            failed_count=len(failed),
            average_confidence=sum(d.confidence for d in decisions) / len(decisions),
            average_speed=sum(d.decision_speed for d in decisions) / len(decisions)
        )
        
        # Détermine la tendance
        metrics.trend_direction = self._determine_trend(metrics)
        
        return metrics
    
    def _filter_by_period(self, period: str) -> List[DecisionRecord]:
        """Filtre les décisions par période."""
        now = datetime.now().timestamp()
        
        if period == "TOTAL":
            return list(self.decisions.values())
        elif period == "DAILY":
            cutoff = now - (24 * 3600)
        elif period == "WEEKLY":
            cutoff = now - (7 * 24 * 3600)
        else:
            return list(self.decisions.values())
        
        return [d for d in self.decisions.values() if d.timestamp >= cutoff]
    
    def _calculate_learning_velocity(
        self,
        decisions: List[DecisionRecord],
        period: str
    ) -> float:
        """Calcule la vitesse d'apprentissage (amélioration dans le temps)."""
        if len(decisions) < 2:
            return 0.0
        
        # Trie par timestamp
        sorted_decisions = sorted(decisions, key=lambda d: d.timestamp)
        
        # Divise en deux périodes
        mid = len(sorted_decisions) // 2
        first_half = sorted_decisions[:mid]
        second_half = sorted_decisions[mid:]
        
        if not first_half or not second_half:
            return 0.0
        
        # Calcule accuracy moyenne pour chaque moitié
        def calc_accuracy(batch):
            completed = [d for d in batch if d.status == "COMPLETED"]
            if not completed:
                return 0.0
            errors = [d.accuracy_error for d in completed if d.accuracy_error]
            if not errors:
                return 0.0
            return max(0.0, 1.0 - sum(errors) / len(errors))
        
        accuracy_1 = calc_accuracy(first_half)
        accuracy_2 = calc_accuracy(second_half)
        
        # Learning velocity = amélioration
        velocity = accuracy_2 - accuracy_1
        return max(-1.0, min(1.0, velocity))
    
    def _calculate_confidence_calibration(self, completed: List[DecisionRecord]) -> float:
        """
        Mesure si la confiance exprimée match la réalité.
        
        Si je dis "confiance 0.8" et j'ai 80% succès → calibration = 1.0
        """
        if not completed:
            return 0.0
        
        # Groupe par confidence buckets
        buckets = {}
        for d in completed:
            conf_bucket = round(d.confidence * 10) / 10  # 0.8 → bucket 0.8
            if conf_bucket not in buckets:
                buckets[conf_bucket] = []
            buckets[conf_bucket].append(d)
        
        # Pour chaque bucket, compare confidence avec actual success rate
        calibration_scores = []
        for conf_bucket, decisions_in_bucket in buckets.items():
            success_rate = sum(1 for d in decisions_in_bucket if d.status == "COMPLETED") / len(decisions_in_bucket)
            # Calibration = 1 - abs(confidence - reality)
            calibration = 1.0 - abs(conf_bucket - success_rate)
            calibration_scores.append(calibration)
        
        if calibration_scores:
            return sum(calibration_scores) / len(calibration_scores)
        return 0.0
    
    def _determine_trend(self, metrics: PerformanceMetrics) -> str:
        """Détermine la tendance générale (UP, DOWN, STABLE)."""
        if metrics.learning_velocity > 0.05:
            return "UP"
        elif metrics.learning_velocity < -0.05:
            return "DOWN"
        else:
            return "STABLE"
    
    def get_improvement_recommendations(self) -> Dict[str, Any]:
        """
        Génère des recommandations d'amélioration basées sur les métriques.
        
        Returns:
            Dict avec recommandations et actions prioritaires
        """
        metrics = self.get_performance_metrics("TOTAL")
        recommendations = {}
        
        # Accuracy
        if metrics.accuracy < 0.75:
            recommendations["accuracy"] = {
                "issue": "Low accuracy in decisions",
                "priority": "HIGH",
                "suggestions": [
                    "Review prediction model - may be oversimplifying",
                    "Check for contextual factors missing",
                    "Increase confidence threshold for borderline decisions"
                ]
            }
        
        # Speed
        if metrics.speed < 0.6:
            recommendations["speed"] = {
                "issue": "Decisions taking too long",
                "priority": "MEDIUM",
                "suggestions": [
                    "Pre-fetch common context",
                    "Use confidence-based decision shortcuts",
                    "Parallel evaluation of criteria"
                ]
            }
        
        # Confidence calibration
        if metrics.confidence_calibration < 0.7:
            recommendations["calibration"] = {
                "issue": "Confidence scores not matching reality",
                "priority": "HIGH",
                "suggestions": [
                    "Retrain confidence predictor",
                    "Add uncertainty quantification",
                    "Review edge cases"
                ]
            }
        
        # Adaptability
        if metrics.adaptability_score < 0.5:
            recommendations["adaptability"] = {
                "issue": "Not enough adaptation happening",
                "priority": "MEDIUM",
                "suggestions": [
                    "Lower adaptation threshold",
                    "Review when adaptations are trigger",
                    "Analyze successful adaptations"
                ]
            }
        
        # Learning velocity
        if metrics.learning_velocity < 0.02 and metrics.decision_count > 20:
            recommendations["learning"] = {
                "issue": "Not improving from feedback",
                "priority": "MEDIUM",
                "suggestions": [
                    "Check feedback loop connection",
                    "Verify outcome recording",
                    "Review learning mechanisms"
                ]
            }
        
        return recommendations
    
    def get_decision_history(
        self,
        limit: int = 10,
        only_completed: bool = False
    ) -> List[DecisionRecord]:
        """
        Retourne l'historique des décisions.
        
        Args:
            limit: Nombre max de décisions retournées
            only_completed: Seulement les décisions avec outcome?
        
        Returns:
            Liste de DecisionRecord triée par timestamp
        """
        decisions = list(self.decisions.values())
        
        if only_completed:
            decisions = [d for d in decisions if d.status == "COMPLETED"]
        
        # Trie par timestamp décroissant (récent d'abord)
        decisions.sort(key=lambda d: d.timestamp, reverse=True)
        
        return decisions[:limit]
    
    def export_metrics_json(self, period: str = "TOTAL") -> Dict[str, Any]:
        """Exporte les métriques en format JSON."""
        metrics = self.get_performance_metrics(period)
        return {
            "period": metrics.period,
            "timestamp": metrics.timestamp,
            "accuracy": round(metrics.accuracy, 3),
            "speed": round(metrics.speed, 3),
            "efficiency": round(metrics.efficiency, 3),
            "learning_velocity": round(metrics.learning_velocity, 3),
            "adaptability_score": round(metrics.adaptability_score, 3),
            "confidence_calibration": round(metrics.confidence_calibration, 3),
            "decision_count": metrics.decision_count,
            "successful_count": metrics.successful_count,
            "failed_count": metrics.failed_count,
            "average_confidence": round(metrics.average_confidence, 3),
            "average_speed": round(metrics.average_speed, 3),
            "trend": metrics.trend_direction,
            "improvement_percentage": round(metrics.improvement_percentage, 2)
        }


# Singleton global
_performance_engine: Optional[DecisionPerformanceEngine] = None


def get_performance_engine() -> DecisionPerformanceEngine:
    """Accès singleton au moteur de performance."""
    global _performance_engine
    if _performance_engine is None:
        _performance_engine = DecisionPerformanceEngine()
    return _performance_engine


if __name__ == "__main__":
    # Test d'usage
    engine = DecisionPerformanceEngine()
    
    # Simule 10 décisions
    for i in range(10):
        engine.record_decision(
            decision_id=f"PROJ_{i:03d}",
            opportunity={"value": 1_000_000 * (i + 1), "name": f"Project {i}"},
            decision_payload={"status": "APPROVED", "mode": "INDUSTRIAL"},
            predicted_outcome=0.75 + (i * 0.02),
            confidence=0.70 + (i * 0.02),
            decision_speed=2.0 - (i * 0.1),
            adaptations_applied=i % 3
        )
        
        # La moitié ont des outcomes
        if i < 5:
            engine.record_outcome(f"PROJ_{i:03d}", 0.76 + (i * 0.015))
    
    # Affiche les métriques
    metrics = engine.get_performance_metrics("TOTAL")
    print(f"\n✓ Performance Metrics:")
    print(f"  Accuracy: {metrics.accuracy:.3f}")
    print(f"  Speed: {metrics.speed:.3f}")
    print(f"  Efficiency: {metrics.efficiency:.3f}")
    print(f"  Learning Velocity: {metrics.learning_velocity:.3f}")
    print(f"  Adaptability: {metrics.adaptability_score:.3f}")
    print(f"  Trend: {metrics.trend_direction}")
