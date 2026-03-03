"""
NAYA_CORE - ADVANCED DECISION OPTIMIZATION ENGINE

Améliorations du Super Brain Hybride:
1. Advanced Caching & Pattern Recognition
2. Machine Learning Models for Prediction
3. Semantic Understanding & Similarity Analysis
4. Confidence Scoring Optimization
5. Performance Tuning & Optimization
6. Feedback Learning Loop Acceleration
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from collections import defaultdict
from hashlib import md5
import json
import math


# ============================================================================
# TIER 1: INTELLIGENT CACHING SYSTEM
# ============================================================================

@dataclass
class CachedDecision:
    """Décision mise en cache avec métadonnées."""
    decision_id: str
    situation_hash: str
    situation: Dict[str, Any]
    result: Dict[str, Any]
    confidence: float
    outcome: Optional[Dict[str, Any]] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    last_accessed: datetime = field(default_factory=datetime.utcnow)
    access_count: int = 0
    accuracy_verified: bool = False


class AdvancedDecisionCache:
    """Cache intelligent avec LRU + Pattern Recognition."""

    def __init__(self, max_size: int = 10000):
        self.max_size = max_size
        self.cache: Dict[str, CachedDecision] = {}
        self.access_log: List[str] = []
        self.pattern_index: Dict[str, List[str]] = defaultdict(list)
        self.accuracy_history: Dict[str, float] = {}

    def _situation_hash(self, situation: Dict) -> str:
        """Crée un hash de la situation pour lookup rapide."""
        key_parts = [
            str(situation.get("name", "")),
            str(situation.get("type", "")),
            str(situation.get("value", "")),
            str(situation.get("market", ""))
        ]
        key_string = "|".join(key_parts)
        return md5(key_string.encode()).hexdigest()

    def get_cached(self, situation: Dict) -> Optional[CachedDecision]:
        """Récupère une décision en cache."""
        situation_hash = self._situation_hash(situation)
        
        if situation_hash in self.cache:
            cached = self.cache[situation_hash]
            cached.last_accessed = datetime.utcnow()
            cached.access_count += 1
            self.access_log.append(situation_hash)
            return cached
        
        return None

    def find_similar(self, situation: Dict, similarity_threshold: float = 0.85) -> List[CachedDecision]:
        """Trouve des décisions similaires passées."""
        similar_decisions = []
        situation_hash = self._situation_hash(situation)
        
        for cached_id, cached in self.cache.items():
            similarity = self._calculate_similarity(situation, cached.situation)
            
            if similarity >= similarity_threshold:
                similar_decisions.append(cached)
        
        # Sort by similarity score
        similar_decisions.sort(key=lambda x: self._calculate_similarity(situation, x.situation), reverse=True)
        
        return similar_decisions[:5]  # Top 5 similar

    def _calculate_similarity(self, sit1: Dict, sit2: Dict) -> float:
        """Calcule la similarité entre deux situations (0-1)."""
        scores = []
        
        # Type similarity
        if sit1.get("type") == sit2.get("type"):
            scores.append(1.0)
        else:
            scores.append(0.3)
        
        # Value similarity (within 20%)
        val1 = float(sit1.get("value", 0))
        val2 = float(sit2.get("value", 0))
        if val1 > 0 and val2 > 0:
            ratio = min(val1, val2) / max(val1, val2)
            if ratio > 0.8:
                scores.append(0.9)
            elif ratio > 0.5:
                scores.append(0.6)
            else:
                scores.append(0.3)
        
        # Market similarity
        if sit1.get("market") == sit2.get("market"):
            scores.append(0.8)
        else:
            scores.append(0.2)
        
        # Timeline similarity
        if sit1.get("timeline") == sit2.get("timeline"):
            scores.append(0.7)
        else:
            scores.append(0.3)
        
        return sum(scores) / len(scores) if scores else 0.0

    def cache_decision(self, situation: Dict, result: Dict, confidence: float) -> str:
        """Met en cache une nouvelle décision."""
        decision_id = f"D-{int(datetime.utcnow().timestamp() * 1000)}"
        situation_hash = self._situation_hash(situation)
        
        # If cache is full, remove LRU item
        if len(self.cache) >= self.max_size:
            self._evict_lru()
        
        cached = CachedDecision(
            decision_id=decision_id,
            situation_hash=situation_hash,
            situation=situation,
            result=result,
            confidence=confidence
        )
        
        self.cache[decision_id] = cached
        self.pattern_index[situation.get("type", "unknown")].append(decision_id)
        
        return decision_id

    def record_outcome(self, decision_id: str, outcome: Dict, success: bool) -> None:
        """Enregistre le résultat d'une décision."""
        if decision_id in self.cache:
            cached = self.cache[decision_id]
            cached.outcome = outcome
            cached.accuracy_verified = True
            
            accuracy = 1.0 if success else 0.0
            self.accuracy_history[decision_id] = accuracy

    def _evict_lru(self) -> None:
        """Supprime l'item le moins récemment utilisé."""
        if self.access_log:
            lru_id = self.access_log[0]
            if lru_id in self.cache:
                del self.cache[lru_id]
            self.access_log.pop(0)

    def get_accuracy_stats(self, decision_type: str = None) -> Dict[str, float]:
        """Retourne les stats de précision."""
        if decision_type:
            relevant_ids = self.pattern_index.get(decision_type, [])
            accuracies = [self.accuracy_history.get(id, 0) for id in relevant_ids if id in self.accuracy_history]
        else:
            accuracies = list(self.accuracy_history.values())
        
        if not accuracies:
            return {"average": 0.0, "count": 0}
        
        return {
            "average": sum(accuracies) / len(accuracies),
            "min": min(accuracies),
            "max": max(accuracies),
            "count": len(accuracies)
        }


# ============================================================================
# TIER 2: MACHINE LEARNING PREDICTION ENGINE
# ============================================================================

class PredictiveModel:
    """Modèle de prédiction basé sur l'historique."""

    def __init__(self):
        self.training_data: List[Tuple[Dict, Dict, float]] = []  # (situation, result, outcome)
        self.model_weights: Dict[str, float] = self._init_weights()
        self.last_training: Optional[datetime] = None

    def _init_weights(self) -> Dict[str, float]:
        """Initialise les poids du modèle."""
        return {
            "type_importance": 0.25,
            "value_importance": 0.20,
            "market_importance": 0.15,
            "timeline_importance": 0.15,
            "risk_importance": 0.25
        }

    def add_training_sample(self, situation: Dict, result: Dict, success: float) -> None:
        """Ajoute un exemple d'entraînement."""
        self.training_data.append((situation, result, success))
        
        # Re-train if we have 100+ samples
        if len(self.training_data) % 100 == 0:
            self._train()

    def predict(self, situation: Dict) -> Tuple[float, Dict[str, Any]]:
        """Prédit la probabilité de succès pour une situation."""
        
        # Base prediction from similar historical decisions
        similar_success_rate = self._get_similar_success_rate(situation)
        
        # Adjust based on situation characteristics
        adjustments = self._calculate_adjustments(situation)
        
        final_prediction = min(0.99, similar_success_rate * (1 + adjustments["total_adjustment"]))
        
        confidence_factors = {
            "similar_success_rate": similar_success_rate,
            "training_samples": len(self.training_data),
            "adjustment_factors": adjustments
        }
        
        return final_prediction, confidence_factors

    def _get_similar_success_rate(self, situation: Dict) -> float:
        """Calcule le taux de succès sur situations similaires."""
        if not self.training_data:
            return 0.75  # Default optimistic
        
        similar = []
        for train_sit, train_result, success in self.training_data:
            if self._is_similar(situation, train_sit):
                similar.append(success)
        
        if similar:
            return sum(similar) / len(similar)
        else:
            # Fall back to overall average
            return sum(s for _, _, s in self.training_data) / len(self.training_data)

    def _is_similar(self, sit1: Dict, sit2: Dict) -> bool:
        """Vérifie si deux situations sont similaires."""
        return (sit1.get("type") == sit2.get("type") and
                abs(float(sit1.get("value", 0)) - float(sit2.get("value", 0))) < 10000)

    def _calculate_adjustments(self, situation: Dict) -> Dict[str, float]:
        """Calcule les ajustements basés sur les caractéristiques."""
        adjustments = {
            "type_adjustment": 0.0,
            "risk_adjustment": 0.0,
            "market_adjustment": 0.0
        }
        
        # Type adjustment based on risk
        if situation.get("type") in ["market_expansion", "product_launch"]:
            adjustments["type_adjustment"] = 0.05
        elif situation.get("type") == "crisis":
            adjustments["type_adjustment"] = -0.10
        
        # Risk adjustment
        risk = situation.get("risk_level", "medium")
        if risk == "low":
            adjustments["risk_adjustment"] = 0.08
        elif risk == "high":
            adjustments["risk_adjustment"] = -0.15
        
        adjustments["total_adjustment"] = sum(adjustments.values())
        
        return adjustments

    def _train(self) -> None:
        """Entraîne le modèle sur les données disponibles."""
        # Simple weight adjustment based on performance
        if self.training_data:
            success_rate = sum(s for _, _, s in self.training_data) / len(self.training_data)
            
            # Adjust model confidence based on performance
            for key in self.model_weights:
                self.model_weights[key] *= (0.95 + success_rate * 0.1)
        
        self.last_training = datetime.utcnow()


# ============================================================================
# TIER 3: SEMANTIC SIMILARITY ENGINE
# ============================================================================

class SemanticAnalyzer:
    """Analyse sémantique pour mieux comprendre les situations."""

    def __init__(self):
        self.semantic_vectors: Dict[str, List[float]] = {}
        self.concept_mappings: Dict[str, List[str]] = self._init_concepts()

    def _init_concepts(self) -> Dict[str, List[str]]:
        """Initialise les mappings conceptuels."""
        return {
            "growth": ["expansion", "launch", "scaling", "market_entry"],
            "defense": ["protection", "risk_mitigation", "hedge", "consolidation"],
            "operations": ["optimization", "efficiency", "automation", "process"],
            "innovation": ["R&D", "new_product", "technology", "disruption"],
            "crisis": ["emergency", "loss", "failure", "threat"]
        }

    def get_semantic_category(self, situation: Dict) -> str:
        """Détermine la catégorie sémantique d'une situation."""
        situation_str = json.dumps(situation).lower()
        
        for category, keywords in self.concept_mappings.items():
            for keyword in keywords:
                if keyword in situation_str:
                    return category
        
        return "unknown"

    def measure_semantic_distance(self, sit1: Dict, sit2: Dict) -> float:
        """Mesure la distance sémantique entre deux situations (0-1)."""
        cat1 = self.get_semantic_category(sit1)
        cat2 = self.get_semantic_category(sit2)
        
        if cat1 == cat2:
            return 0.1  # Very close semantically
        elif cat1 in ["growth", "defense"] or cat2 in ["growth", "defense"]:
            return 0.3
        else:
            return 0.7  # Far apart semantically

    def get_context_awareness(self, situation: Dict) -> Dict[str, Any]:
        """Retourne la conscience de contexte pour une situation."""
        return {
            "semantic_category": self.get_semantic_category(situation),
            "urgency": "high" if "crisis" in situation.get("type", "").lower() else "normal",
            "strategic_importance": situation.get("value", 0) > 50000,
            "market_exposure": situation.get("market") is not None
        }


# ============================================================================
# TIER 4: ADVANCED CONFIDENCE SCORING
# ============================================================================

class ConfidenceScorer:
    """Scoring avancé de confiance pour les décisions."""

    def __init__(self, predictive_model: Optional[PredictiveModel] = None):
        self.predictive_model = predictive_model
        self.confidence_history: List[Tuple[float, bool]] = []

    def calculate_confidence(self, 
                            prediction: float,
                            similar_decisions: List[CachedDecision],
                            semantic_context: Dict[str, Any],
                            specialization_scores: Dict[str, float]) -> Tuple[float, Dict[str, Any]]:
        """Calcule un score de confiance holistique.
        
        Facteurs:
        - Prédiction ML (30%)
        - Historique similaire (25%)
        - Contexte sémantique (20%)
        - Scores des spécialisations (25%)
        """
        
        scores = {}
        
        # 1. ML Prediction component (0-1)
        scores["prediction"] = prediction * 0.30
        
        # 2. Similar decisions component
        if similar_decisions:
            similar_avg_confidence = sum(d.confidence for d in similar_decisions) / len(similar_decisions)
            similar_accuracy = sum(1 for d in similar_decisions if d.accuracy_verified and d.outcome) / len(similar_decisions)
            scores["similarity"] = (similar_avg_confidence * 0.5 + similar_accuracy * 0.5) * 0.25
        else:
            scores["similarity"] = 0.75 * 0.25  # Default neutral
        
        # 3. Semantic context component
        penalty = 0.0
        if semantic_context.get("urgency") == "high":
            penalty += 0.1  # Higher urgency = lower confidence
        
        scores["semantic"] = (0.8 - penalty) * 0.20
        
        # 4. Specialization scores
        if specialization_scores:
            avg_spec_score = sum(specialization_scores.values()) / len(specialization_scores)
            scores["specializations"] = avg_spec_score * 0.25
        else:
            scores["specializations"] = 0.80 * 0.25
        
        # Calculate final confidence
        final_confidence = sum(scores.values())
        
        # Apply bounds
        final_confidence = max(0.45, min(0.99, final_confidence))  # 45-99% range
        
        breakdown = {
            "prediction_score": scores["prediction"],
            "similarity_score": scores["similarity"],
            "semantic_score": scores["semantic"],
            "specialization_score": scores["specializations"],
            "factors": {
                "has_similar_history": len(similar_decisions) > 0,
                "semantic_category": semantic_context.get("semantic_category"),
                "urgency_level": semantic_context.get("urgency")
            }
        }
        
        return final_confidence, breakdown

    def record_outcome(self, confidence: float, success: bool) -> None:
        """Enregistre l'issue pour calibration."""
        self.confidence_history.append((confidence, success))


# ============================================================================
# TIER 5: PERFORMANCE OPTIMIZATION
# ============================================================================

class PerformanceOptimizer:
    """Optimiseur de performance pour réduire latency."""

    def __init__(self, target_latency_ms: float = 100.0):
        self.target_latency_ms = target_latency_ms
        self.operation_timings: Dict[str, List[float]] = defaultdict(list)
        self.optimization_enabled = True

    def record_operation(self, operation_name: str, duration_ms: float) -> None:
        """Enregistre la durée d'une opération."""
        self.operation_timings[operation_name].append(duration_ms)
        
        # Keep only last 1000 measurements
        if len(self.operation_timings[operation_name]) > 1000:
            self.operation_timings[operation_name] = self.operation_timings[operation_name][-1000:]

    def get_optimization_recommendations(self) -> Dict[str, Any]:
        """Retourne les recommandations d'optimisation."""
        recommendations = {
            "bottlenecks": [],
            "optimizations": [],
            "current_performance": {}
        }
        
        for op_name, timings in self.operation_timings.items():
            avg_time = sum(timings) / len(timings)
            recommendations["current_performance"][op_name] = f"{avg_time:.1f}ms"
            
            if avg_time > self.target_latency_ms * 0.3:
                recommendations["bottlenecks"].append(f"{op_name}: {avg_time:.1f}ms")
                
                if op_name == "specializations_parallel":
                    recommendations["optimizations"].append("Consider reducing specialization count for crisis mode")
                elif "memory" in op_name:
                    recommendations["optimizations"].append("Increase cache size or use caching layer")
        
        return recommendations

    def estimate_processing_time(self, num_specializations: int = 10) -> float:
        """Estime le temps de processing total."""
        base_time = 15.0  # Setup overhead
        
        spec_time = self.operation_timings.get("specializations_parallel", [100.0])
        avg_spec_time = sum(spec_time) / len(spec_time)
        
        synthesis_time = self.operation_timings.get("synthesis", [5.0])
        avg_synthesis = sum(synthesis_time) / len(synthesis_time)
        
        total = base_time + avg_spec_time + avg_synthesis
        
        return total


# ============================================================================
# TIER 6: FEEDBACK LEARNING ACCELERATION
# ============================================================================

class FeedbackLearningEngine:
    """Accélère l'apprentissage avec retour d'expérience."""

    def __init__(self):
        self.feedback_buffer: List[Dict[str, Any]] = []
        self.learning_progress: Dict[str, float] = defaultdict(float)
        self.doctrine_mutations: List[Dict[str, Any]] = []

    def process_feedback(self, decision_id: str, outcome: Dict, success: bool) -> None:
        """Traite un retour d'expérience."""
        feedback = {
            "decision_id": decision_id,
            "outcome": outcome,
            "success": success,
            "timestamp": datetime.utcnow(),
            "processed": False
        }
        self.feedback_buffer.append(feedback)
        
        # Process if buffer reaches size 10
        if len(self.feedback_buffer) >= 10:
            self._batch_process_feedback()

    def _batch_process_feedback(self) -> None:
        """Traite un batch de feedback."""
        success_count = sum(1 for f in self.feedback_buffer if f["success"])
        success_rate = success_count / len(self.feedback_buffer) if self.feedback_buffer else 0
        
        # Extract patterns
        for feedback in self.feedback_buffer:
            decision_type = feedback.get("outcome", {}).get("type", "unknown")
            
            if feedback["success"]:
                self.learning_progress[decision_type] += 0.005
            else:
                self.learning_progress[decision_type] -= 0.002
        
        # Propose doctrine mutation if pattern emerges
        if success_rate > 0.92:  # Consistently good
            self._propose_doctrine_mutation(success_rate)
        
        self.feedback_buffer = []

    def _propose_doctrine_mutation(self, success_rate: float) -> None:
        """Propose une mutation de doctrine basée sur le succès."""
        mutation = {
            "type": "performance_based_optimization",
            "success_rate": success_rate,
            "timestamp": datetime.utcnow(),
            "recommended_changes": {
                "increase_confidence_threshold": success_rate > 0.95,
                "accelerate_specializations": success_rate > 0.90,
                "expand_risk_tolerance": success_rate > 0.92
            }
        }
        self.doctrine_mutations.append(mutation)

    def get_learning_status(self) -> Dict[str, Any]:
        """Retourne le status d'apprentissage."""
        return {
            "learning_progress": dict(self.learning_progress),
            "pending_feedback": len(self.feedback_buffer),
            "doctrine_mutations_proposed": len(self.doctrine_mutations),
            "learning_rate_acceleration": sum(self.learning_progress.values()) / max(len(self.learning_progress), 1)
        }


# ============================================================================
# PUBLIC API - ADVANCED OPTIMIZATION
# ============================================================================

def create_optimization_engine() -> Dict[str, Any]:
    """Crée un moteur complet d'optimisation."""
    return {
        "cache": AdvancedDecisionCache(),
        "predictor": PredictiveModel(),
        "semantic": SemanticAnalyzer(),
        "confidence": ConfidenceScorer(),
        "performance": PerformanceOptimizer(),
        "learning": FeedbackLearningEngine()
    }
