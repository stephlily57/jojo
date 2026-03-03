"""
Executive Performance Core - Master Orchestrator

Cerveau décisionnel naturellement exécutif, intelligent et auto-optimisant.

Responsabilité:
  - Orchestre l'ensemble du système décisionnel
  - Intègre: prédiction + performance + adaptation + accélération
  - Boucle de feedback natural feedback loop automatique
  - Auto-optimisation sans intervention
  - Apprentissage continu

Production: v1.0
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from enum import Enum

# Importe les moteurs
from decision_core import DecisionCore
from decision_performance_engine import get_performance_engine, DecisionPerformanceEngine
from outcome_prediction_engine import get_prediction_engine, OutcomePredictionEngine
from strategic_adaptation_layer import get_adaptation_layer, StrategicAdaptationLayer
from decision_accelerator import get_decision_accelerator, DecisionAccelerator


class ExecutiveDecisionStatus(Enum):
    """État d'une décision exécutive."""
    DECISION_MADE = "DECISION_MADE"
    EXECUTING = "EXECUTING"
    OUTCOME_PENDING = "OUTCOME_PENDING"
    COMPLETED = "COMPLETED"
    LEARNING = "LEARNING"


@dataclass
class ExecutiveDecisionRecord:
    """Record complet d'une décision exécutive."""
    decision_id: str
    timestamp: float
    opportunity: Dict[str, Any]
    market_context: Optional[Dict[str, Any]] = None
    
    # Étapes du processus
    decision_payload: Optional[Dict[str, Any]] = None
    predicted_outcome: Optional[float] = None
    confidence_initial: float = 0.0
    confidence_final: float = 0.0
    
    # Accélération
    target_speed: Optional[str] = None
    estimated_time: float = 0.0
    actual_time: float = 0.0
    
    # Adaptations
    adaptations_applied: List[str] = field(default_factory=list)
    
    # Exécution
    status: ExecutiveDecisionStatus = ExecutiveDecisionStatus.DECISION_MADE
    actual_outcome: Optional[float] = None
    
    # Apprentissage
    learning_applied: Optional[Dict[str, Any]] = None
    
    # Performance
    overall_quality_score: Optional[float] = None
    
    def is_completed(self) -> bool:
        """La décision est-elle complète (avec outcome)?"""
        return self.status == ExecutiveDecisionStatus.COMPLETED


@dataclass
class ExecutivePerformanceSummary:
    """Résumé de la performance du cœur exécutif."""
    decisions_count: int
    decisions_completed: int
    
    accuracy: float                 # % bonnes décisions
    speed_vs_baseline: float        # Vitesse vs référence
    efficiency: float               # ROI moyen
    learning_velocity: float        # Amélioration dans le temps
    confidence_calibration: float   # Confiance vs réalité
    
    average_confidence: float
    average_execution_time: float
    
    patterns_learned: int
    strategy_rules: int
    
    timestamp: float = field(default_factory=lambda: datetime.now().timestamp())


class ExecutivePerformanceCore:
    """
    Cœur exécutif performance du système NAYA.
    
    Le cerveau décisionnel NATURELLEMENT:
      ✓ INTELLIGENT - Utilise cognition enrichie
      ✓ PERFORMANT - Mesure tout en continu
      ✓ RAPIDE - Accélère intelligemment
      ✓ APPRENTI - Apprend de chaque feedback
      ✓ ADAPTATIF - Améliore continuellement
      ✓ SANS FORCER - C'est naturel, émergent
    
    Flux naturel:
      1. CONTEXTE & CONFIANCE
         ├─ Lit le contexte
         ├─ Consulte l'historique
         └─ Calcule confiance initiale
      
      2. PRÉDICTION
         ├─ Prédit le résultat si on décide
         ├─ Identifie les risques
         └─ Recommande adaptations
      
      3. ACCÉLÉRATION
         ├─ Détermine vitesse optimale
         ├─ Alloue ressources
         └─ Lance décision
      
      4. DÉCISION
         ├─ Enrichit avec contexte
         ├─ Applique adaptations
         └─ Approuve avec haute confiance
      
      5. EXÉCUTION
         ├─ Mesure en temps réel
         ├─ Capture outcomes
         └─ Signale déviations
      
      6. FEEDBACK
         ├─ Outcome vs prédiction
         ├─ Erreur calculée
         └─ Patterns détectés
      
      7. APPRENTISSAGE
         ├─ Améliore les modèles
         ├─ Ajuste confiance
         ├─ Crée nouvelles heuristiques
         └─ Retour à l'étape 1 (meilleur)
    
    Usage:
      executive = ExecutivePerformanceCore()
      
      decision = executive.decide_and_execute(
          opportunity={...},
          market_context={...}
      )
      
      print(f"Decision: {decision['status']}")
      print(f"Confidence: {decision['confidence_final']:.0%}")
      print(f"Speed: {decision['target_speed']}")
      
      # Plus tard, enregistre l'outcome
      executive.record_outcome(
          decision_id=decision['decision_id'],
          actual_outcome=0.82
      )
    
    Production: Ready
    Maturity: Production
    """
    
    def __init__(self):
        # Moteurs intégrés
        self.decision_core = DecisionCore()
        self.performance_engine = get_performance_engine()
        self.prediction_engine = get_prediction_engine()
        self.adaptation_layer = get_adaptation_layer()
        self.accelerator = get_decision_accelerator()
        
        # Historique des décisions
        self.decisions: Dict[str, ExecutiveDecisionRecord] = {}
        self.decision_counter = 0
    
    def decide_and_execute(
        self,
        opportunity: Dict[str, Any],
        market_context: Optional[Dict[str, Any]] = None,
        force_speed: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        DÉCISION COMPLÈTE NATURELLEMENT INTELLIGENTE ET RAPIDE.
        
        Flux complet:
          ✓ Évalue contexte & historique
          ✓ Prédit résultat
          ✓ Accélère intelligemment
          ✓ Enrichit décision
          ✓ Retourne résultat riche
        
        Args:
            opportunity: Opportunité à évaluer
            market_context: Contexte du marché (optionnel)
            force_speed: Force une vitesse spécifique (optionnel)
        
        Returns:
            Décision complète enrichie avec:
              - decision_id, status, decision payload
              - predicted_outcome, confidence
              - target_speed, estimated_time
              - adaptations_applied
              - recommendation + reasoning
        """
        
        decision_id = f"EXEC_{self.decision_counter:06d}"
        self.decision_counter += 1
        
        # Crée le record
        record = ExecutiveDecisionRecord(
            decision_id=decision_id,
            timestamp=datetime.now().timestamp(),
            opportunity=opportunity,
            market_context=market_context
        )
        
        # ════════════════════════════════════════════════════════════════════
        # ÉTAPE 1: CONTEXTE & CONFIANCE INITIALE
        # ════════════════════════════════════════════════════════════════════
        
        # Consulte la performance historique
        past_performance = self.performance_engine.get_performance_metrics("TOTAL")
        
        # Confiance initiale basée sur historique
        base_confidence = self._calculate_initial_confidence(
            opportunity,
            past_performance
        )
        record.confidence_initial = base_confidence
        
        # ════════════════════════════════════════════════════════════════════
        # ÉTAPE 2: PRÉDICTION
        # ════════════════════════════════════════════════════════════════════
        
        prediction = self.prediction_engine.predict_outcome(
            opportunity=opportunity,
            market_context=market_context,
            decision_id=decision_id
        )
        
        record.predicted_outcome = prediction.predicted_outcome
        record.confidence_initial = max(
            base_confidence,
            prediction.confidence * 0.9  # Prédit confiance est indicatif
        )
        
        # ════════════════════════════════════════════════════════════════════
        # ÉTAPE 3: ACCÉLÉRATION INTELLIGENTE
        # ════════════════════════════════════════════════════════════════════
        
        if force_speed:
            # Override manuel si fourni
            target_speed = force_speed
        else:
            # Détermine vitesse basée sur confiance
            acceleration_profile = self.accelerator.plan_decision_speed(
                opportunity=opportunity,
                confidence=record.confidence_initial
            )
            record.target_speed = acceleration_profile.target_speed.value
            record.estimated_time = acceleration_profile.time_budget
        
        # ════════════════════════════════════════════════════════════════════
        # ÉTAPE 4: RECOMMANDATIONS D'ADAPTATION
        # ════════════════════════════════════════════════════════════════════
        
        suggested_adaptations = prediction.suggested_adaptations
        record.adaptations_applied = suggested_adaptations[:3]  # Top 3
        
        # ════════════════════════════════════════════════════════════════════
        # ÉTAPE 5: DÉCISION DE BASE
        # ════════════════════════════════════════════════════════════════════
        
        decision_payload = self.decision_core.evaluate(opportunity)
        
        # Si rejet, signale early
        if decision_payload.get("status") == "REJECTED":
            record.status = ExecutiveDecisionStatus.COMPLETED
            record.decision_payload = decision_payload
            record.overall_quality_score = 0.0
            
            self.decisions[decision_id] = record
            
            return {
                "decision_id": decision_id,
                "status": "REJECTED",
                "reason": decision_payload.get("reason"),
                "confidence": record.confidence_initial,
                "prediction": prediction.predicted_outcome,
                "recommendation": "DO_NOT_PROCEED"
            }
        
        record.decision_payload = decision_payload.get("decision", {})
        record.status = ExecutiveDecisionStatus.EXECUTING
        
        # ════════════════════════════════════════════════════════════════════
        # ÉTAPE 6: ENRICHISSEMENT FINAL
        # ════════════════════════════════════════════════════════════════════
        
        # Confiance finale = base + prédiction + pas de risques critiques
        critical_risks = [r for r in prediction.risk_factors if str(r.level) == "RiskLevel.CRITICAL"]
        
        confidence_final = record.confidence_initial
        if critical_risks:
            confidence_final *= 0.85  # Réduit par risques critiques
        
        if prediction.recommendation.value == "EXECUTE":
            confidence_final = min(1.0, confidence_final + 0.05)
        
        record.confidence_final = confidence_final
        
        # ════════════════════════════════════════════════════════════════════
        # ÉTAPE 7: RÉSULTAT FINAL ENRICHI
        # ════════════════════════════════════════════════════════════════════
        
        result = {
            "decision_id": decision_id,
            "status": "APPROVED",
            "confidence_initial": round(record.confidence_initial, 3),
            "confidence_final": round(confidence_final, 3),
            "prediction": round(prediction.predicted_outcome, 3),
            "target_speed": record.target_speed,
            "estimated_time": f"{record.estimated_time:.1f}s",
            "recommendation": prediction.recommendation.value,
            "adaptations": record.adaptations_applied,
            "decision": record.decision_payload,
            "risk_factors": [
                {
                    "description": r.description,
                    "level": str(r.level),
                    "mitigation": r.mitigation
                }
                for r in prediction.risk_factors[:3]
            ],
            "failure_modes": prediction.failure_modes[:2]
        }
        
        # Enregistre dans le moteur de performance
        self.performance_engine.record_decision(
            decision_id=decision_id,
            opportunity=opportunity,
            decision_payload=record.decision_payload,
            predicted_outcome=prediction.predicted_outcome,
            confidence=confidence_final,
            decision_speed=record.estimated_time,
            adaptations_applied=len(record.adaptations_applied)
        )
        
        # Sauvegarde le record
        self.decisions[decision_id] = record
        
        return result
    
    def record_outcome(
        self,
        decision_id: str,
        actual_outcome: float,
        was_successful: bool = True
    ) -> Dict[str, Any]:
        """
        Enregistre le résultat RÉEL d'une décision.
        
        Lance automatiquement:
          ✓ Enregistrement de l'outcome (performance engine)
          ✓ Enregistrement de la prédiction (prediction engine)
          ✓ Adaptation et apprentissage (adaptation layer)
          ✓ Recalibration du modèle
        
        Args:
            decision_id: ID de la décision
            actual_outcome: Score réel obtenu (0-1)
            was_successful: Succès ou échec?
        
        Returns:
            Résumé de l'apprentissage appliqué
        """
        
        if decision_id not in self.decisions:
            return {"error": f"Decision {decision_id} not found"}
        
        record = self.decisions[decision_id]
        record.actual_outcome = actual_outcome
        record.status = ExecutiveDecisionStatus.OUTCOME_PENDING
        
        # ════════════════════════════════════════════════════════════════════
        # ENREGISTREMENT DANS TOUS LES MOTEURS
        # ════════════════════════════════════════════════════════════════════
        
        # 1. Performance Engine
        self.performance_engine.record_outcome(
            decision_id=decision_id,
            actual_outcome=actual_outcome,
            success=was_successful
        )
        
        # 2. Prediction Engine
        prediction_error = self.prediction_engine.register_actual_outcome(
            decision_id=decision_id,
            actual_outcome=actual_outcome
        )
        
        # 3. Adaptation Layer (apprentissage)
        adaptation_result = self.adaptation_layer.adapt_from_outcome(
            decision_id=decision_id,
            opportunity=record.opportunity,
            predicted_result=record.predicted_outcome or 0,
            actual_result=actual_outcome,
            execution_context=record.market_context or {},
            adaptations_applied=record.adaptations_applied
        )
        
        record.learning_applied = adaptation_result
        record.status = ExecutiveDecisionStatus.COMPLETED
        
        # ════════════════════════════════════════════════════════════════════
        # RÉSULTAT FINAL AVEC APPRENTISSAGE
        # ════════════════════════════════════════════════════════════════════
        
        return {
            "decision_id": decision_id,
            "prediction_error": round(prediction_error or 0, 3),
            "improvement": round(actual_outcome - (record.predicted_outcome or 0), 3),
            "patterns_detected": adaptation_result.get("patterns_detected", 0),
            "confidence_improvement": f"+{adaptation_result.get('confidence_improvement', 0):.1%}",
            "learning_velocity": adaptation_result.get("learning_velocity"),
            "status": "LEARNING_COMPLETE"
        }
    
    def _calculate_initial_confidence(
        self,
        opportunity: Dict[str, Any],
        past_performance: Any
    ) -> float:
        """Calcule la confiance initiale basée sur l'historique."""
        
        # Confiance de base de l'historique
        base = getattr(past_performance, 'accuracy', 0.65)
        
        # Ajustes basé sur l'opportunité
        value = opportunity.get("value", 0)
        if value >= 10_000_000:
            base += 0.10  # Grandes opportunités plus prévisibles
        elif value < 500_000:
            base -= 0.10  # Petites sont moins prévisibles
        
        pain_points = len(opportunity.get("pain_points", []))
        if pain_points >= 3:
            base += 0.05  # Opportunité bien définie
        
        return min(0.95, max(0.30, base))
    
    def get_performance_summary(self) -> ExecutivePerformanceSummary:
        """Retourne un résumé complet de la performance."""
        
        perf = self.performance_engine.get_performance_metrics("TOTAL")
        adaptation = self.adaptation_layer.get_learning_summary()
        
        completed = [d for d in self.decisions.values() if d.is_completed()]
        
        avg_time = sum(d.actual_time or 0 for d in completed) / len(completed) if completed else 0
        
        return ExecutivePerformanceSummary(
            decisions_count=len(self.decisions),
            decisions_completed=len(completed),
            accuracy=perf.accuracy,
            speed_vs_baseline=perf.speed,
            efficiency=perf.efficiency,
            learning_velocity=perf.learning_velocity,
            confidence_calibration=perf.confidence_calibration,
            average_confidence=perf.average_confidence,
            average_execution_time=avg_time,
            patterns_learned=adaptation.get("patterns_detected", 0),
            strategy_rules=adaptation.get("strategy_rules_created", 0)
        )
    
    def get_decision_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Retourne l'historique des décisions récentes."""
        
        sorted_decisions = sorted(
            self.decisions.values(),
            key=lambda d: d.timestamp,
            reverse=True
        )
        
        return [
            {
                "decision_id": d.decision_id,
                "status": d.status.value,
                "opportunity": d.opportunity.get("name", "Unknown"),
                "predicted": round(d.predicted_outcome or 0, 2),
                "actual": round(d.actual_outcome or 0, 2),
                "confidence": round(d.confidence_final, 2),
                "speed": d.target_speed
            }
            for d in sorted_decisions[:limit]
        ]


# Singleton global
_executive_core: Optional[ExecutivePerformanceCore] = None


def get_executive_core() -> ExecutivePerformanceCore:
    """Accès singleton au cœur exécutif."""
    global _executive_core
    if _executive_core is None:
        _executive_core = ExecutivePerformanceCore()
    return _executive_core


if __name__ == "__main__":
    # Test
    executive = ExecutivePerformanceCore()
    
    # Simule 5 décisions complètes
    for i in range(5):
        opp = {
            "name": f"Project {i}",
            "value": 2_000_000 * (i + 1),
            "pain_points": ["affordability", "quality"],
            "premium_positioning": i % 2 == 0
        }
        
        market = {
            "cultural_fit": 0.7 + (i * 0.05),
            "market_temperature": 0.6,
            "regulatory_risk": 0.2
        }
        
        # Décision
        decision = executive.decide_and_execute(opp, market)
        print(f"\n✓ Decision {decision['decision_id']}:")
        print(f"  Confidence: {decision['confidence_final']:.0%}")
        print(f"  Prediction: {decision['prediction']:.0%}")
        print(f"  Speed: {decision['target_speed']}")
        
        # Simule l'outcome
        actual = decision['prediction'] * (0.95 + i * 0.02)
        feedback = executive.record_outcome(decision['decision_id'], actual)
        print(f"  Outcome: {actual:.0%}")
        print(f"  Learning: {feedback['learning_velocity']}")
    
    # Résumé final
    print("\n════════════════════════════════════════════")
    summary = executive.get_performance_summary()
    print(f"\n✓ EXECUTIVE PERFORMANCE CORE SUMMARY:")
    print(f"  Decisions: {summary.decisions_count}")
    print(f"  Accuracy: {summary.accuracy:.0%}")
    print(f"  Efficiency: {summary.efficiency:.2f}")
    print(f"  Learning Velocity: {summary.learning_velocity:+.1%}")
    print(f"  Patterns Learned: {summary.patterns_learned}")
