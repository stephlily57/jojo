"""
Strategic Adaptation Layer - Apprend des résultats et améliore les stratégies

Responsabilité:
  - Détecte les patterns d'amélioration
  - Adapte les stratégies décisionnelles
  - Crée de nouvelles heuristiques
  - Préserve ce qui marche, élimine ce qui ne marche pas
  - Apprentissage continu sans intervention

Production: v1.0
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Set, Tuple
from enum import Enum
from datetime import datetime
import math


class PatternType(Enum):
    """Type de pattern détecté."""
    SUCCESS_CORRELATION = "success_correlation"        # X correlé avec succès
    FAILURE_CORRELATION = "failure_correlation"        # X correlé avec échec
    CONTEXT_SENSITIVITY = "context_sensitivity"        # X sensible au contexte
    HUMANIZATION_BOOST = "humanization_boost"          # Humanisation aide
    CULTURAL_ALIGNMENT = "cultural_alignment"          # Alignement culturel aide
    TIMING_DEPENDENCY = "timing_dependency"            # Timing est important
    ADAPTATION_EFFECTIVENESS = "adaptation_effectiveness"  # Adaptations qui aident


@dataclass
class LearningPattern:
    """Pattern d'apprentissage détecté."""
    pattern_type: PatternType
    factor_name: str                     # e.g., "humanization_strength"
    factor_value: float                  # Valeur qui corrèle
    correlation_strength: float          # 0-1, force de la corrélation
    success_rate: float                  # % succès quand ce pattern présent
    sample_size: int                     # Nombre de cas
    confidence: float                    # 0-1, confiance dans le pattern
    
    description: str = ""                # Description lisible
    recommendation: str = ""             # Recommandation
    
    def apply_effect(self, base_score: float) -> float:
        """Applique l'effet du pattern au score."""
        if self.correlation_strength > 0.7:
            # Pattern fort
            effect = self.correlation_strength * 0.15  # Max +15%
        elif self.correlation_strength > 0.5:
            # Pattern modéré
            effect = self.correlation_strength * 0.10  # Max +10%
        else:
            # Pattern faible
            effect = self.correlation_strength * 0.05  # Max +5%
        
        if self.pattern_type == PatternType.FAILURE_CORRELATION:
            effect = -effect  # Inverser les effets négatifs
        
        return base_score + effect


@dataclass
class StrategyRule:
    """Règle stratégique apprise."""
    rule_id: str
    condition: str                       # e.g., "market_sensitivity > 0.7"
    action: str                          # e.g., "increase_humanization_by_20%"
    learning_pattern: LearningPattern
    
    success_count: int = 0               # Fois qu'elle a aidé
    failure_count: int = 0               # Fois qu'elle a mal performé
    
    def effectiveness(self) -> float:
        """Mesure l'efficacité de cette règle."""
        total = self.success_count + self.failure_count
        if total == 0:
            return 0.5  # Neutre si pas encore testée
        return self.success_count / total
    
    def should_apply(self, context: Dict[str, float]) -> bool:
        """Détermine si cette règle devrait s'appliquer."""
        # Simple évaluation de la condition
        # En production, utiliser un vrai parser
        return self.effectiveness() > 0.6


@dataclass
class ContextualAdaptation:
    """Adaptation suggérée pour un contexte."""
    adaptation_type: str                 # "HUMANIZATION", "CULTURAL", "TIMING", etc.
    priority: int                        # 1-5, 1=max priority
    description: str
    expected_improvement: float          # 0-1, amélioration attendue
    implementation_effort: float         # 0-1, effort pour implémenter
    
    def benefit_effort_ratio(self) -> float:
        """Retourne le ratio bénéfice/effort."""
        if self.implementation_effort == 0:
            return 10.0
        return self.expected_improvement / self.implementation_effort


class StrategicAdaptationLayer:
    """
    Moteur d'adaptation stratégique.
    
    Apprend de chaque décision + outcome et améliore les stratégies.
    
    Détecte:
      - Patterns qui corrèlent avec succès
      - Patterns qui corrèlent avec échec
      - Contexte où certain patterns sont plus forts
      - Adaptations qui aident le plus
      - Nouvelles heuristiques à créer
    
    Usage:
      adapter = StrategicAdaptationLayer()
      
      # Après chaque décision + outcome
      adaptation = adapter.adapt_from_outcome(
          decision_id="PROJ_001",
          opportunity=opp,
          predicted_result=0.78,
          actual_result=0.82,
          execution_context=context,
          adaptations_applied=["humanization"]
      )
      
      # Retourne les ajustements appliqués
      print(f"Predicted vs Actual: {adaptation['improvement']} better than expected")
    
    Production: Ready
    """
    
    def __init__(self):
        self.detected_patterns: Dict[str, LearningPattern] = {}
        self.strategy_rules: Dict[str, StrategyRule] = {}
        self.decision_history: List[Dict[str, Any]] = []
        self.context_patterns: Dict[str, List[LearningPattern]] = {}  # patterns par contexte
        
    def adapt_from_outcome(
        self,
        decision_id: str,
        opportunity: Dict[str, Any],
        predicted_result: float,
        actual_result: float,
        execution_context: Dict[str, Any],
        adaptations_applied: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Apprend d'un outcome et adapte les stratégies.
        
        Args:
            decision_id: ID de la décision
            opportunity: L'opportunité
            predicted_result: Score prédit avant exécution
            actual_result: Score réel après exécution
            execution_context: Contexte d'exécution
            adaptations_applied: Adaptations qui ont été appliquées
        
        Returns:
            Résultat d'adaptation avec améliorations appliquées
        """
        
        if adaptations_applied is None:
            adaptations_applied = []
        
        # Enregistre dans l'historique
        record = {
            "decision_id": decision_id,
            "opportunity": opportunity,
            "predicted": predicted_result,
            "actual": actual_result,
            "context": execution_context,
            "adaptations": adaptations_applied,
            "timestamp": datetime.now().timestamp(),
            "improvement": actual_result - predicted_result
        }
        self.decision_history.append(record)
        
        # ÉTAPE 1: Détecte les patterns
        detected = self._detect_patterns(record)
        
        # ÉTAPE 2: Crée/met à jour les règles
        self._update_strategy_rules(record, detected)
        
        # ÉTAPE 3: Génère des adaptations suggérées
        suggested_adaptations = self._generate_adaptation_suggestions(
            opportunity,
            execution_context,
            detected
        )
        
        # ÉTAPE 4: Calcule les améliorations
        confidence_improvement = self._calculate_confidence_improvement(
            detected,
            adaptations_applied
        )
        
        return {
            "decision_id": decision_id,
            "improvement": record["improvement"],
            "patterns_detected": len(detected),
            "patterns": {p: self.detected_patterns[p].description for p in detected},
            "confidence_improvement": confidence_improvement,
            "suggested_adaptations": self._format_adaptations(suggested_adaptations),
            "strategy_updates_applied": len(self.strategy_rules),
            "learning_velocity": self._calculate_learning_velocity()
        }
    
    def _detect_patterns(self, record: Dict[str, Any]) -> Set[str]:
        """Détecte les patterns dans ce outcome."""
        
        patterns_found = set()
        improvement = record["improvement"]
        context = record["context"]
        adaptations = record["adaptations"]
        
        # PATTERN 1: Improvement > 0 (prédiction était conservative)
        if improvement > 0.05:
            pattern_id = "conservative_prediction"
            if pattern_id not in self.detected_patterns:
                self.detected_patterns[pattern_id] = LearningPattern(
                    pattern_type=PatternType.SUCCESS_CORRELATION,
                    factor_name="prediction_conservatism",
                    factor_value=improvement,
                    correlation_strength=0.6,
                    success_rate=0.8,
                    sample_size=1,
                    confidence=0.3,
                    description="Prédictions trop conservatives - peut être plus agressif"
                )
            else:
                self.detected_patterns[pattern_id].sample_size += 1
                self.detected_patterns[pattern_id].correlation_strength = min(
                    0.95,
                    self.detected_patterns[pattern_id].correlation_strength + 0.02
                )
            patterns_found.add(pattern_id)
        
        # PATTERN 2: Humanization appliquée
        if "humanization" in adaptations:
            pattern_id = "humanization_effective"
            if pattern_id not in self.detected_patterns:
                self.detected_patterns[pattern_id] = LearningPattern(
                    pattern_type=PatternType.HUMANIZATION_BOOST,
                    factor_name="humanization_applied",
                    factor_value=1.0 if improvement > 0 else 0.0,
                    correlation_strength=0.7 if improvement > 0.03 else 0.3,
                    success_rate=0.75,
                    sample_size=1,
                    confidence=0.4,
                    description=f"Humanization boost: {improvement:+.1%} improvement when applied"
                )
            else:
                self.detected_patterns[pattern_id].sample_size += 1
                if improvement > 0.03:
                    self.detected_patterns[pattern_id].correlation_strength = min(0.95, 
                        self.detected_patterns[pattern_id].correlation_strength + 0.05)
                    self.detected_patterns[pattern_id].success_rate = min(1.0,
                        (self.detected_patterns[pattern_id].success_rate * 0.8 + 1.0 * 0.2))
            patterns_found.add(pattern_id)
        
        # PATTERN 3: Cultural sensitivity
        cultural_fit = context.get("cultural_fit", 0.5)
        if cultural_fit > 0.7 and improvement > 0.04:
            pattern_id = "cultural_fit_critical"
            if pattern_id not in self.detected_patterns:
                self.detected_patterns[pattern_id] = LearningPattern(
                    pattern_type=PatternType.CULTURAL_ALIGNMENT,
                    factor_name="cultural_fit",
                    factor_value=cultural_fit,
                    correlation_strength=0.75,
                    success_rate=0.85,
                    sample_size=1,
                    confidence=0.5,
                    description="Strong cultural fit significantly boosts success"
                )
            else:
                self.detected_patterns[pattern_id].sample_size += 1
                self.detected_patterns[pattern_id].correlation_strength = min(0.95,
                    self.detected_patterns[pattern_id].correlation_strength + 0.03)
            patterns_found.add(pattern_id)
        
        # PATTERN 4: Negative - grande dérivation negative
        if improvement < -0.08:
            pattern_id = "execution_gap"
            if pattern_id not in self.detected_patterns:
                self.detected_patterns[pattern_id] = LearningPattern(
                    pattern_type=PatternType.FAILURE_CORRELATION,
                    factor_name="execution_risk",
                    factor_value=abs(improvement),
                    correlation_strength=0.6,
                    success_rate=0.2,
                    sample_size=1,
                    confidence=0.4,
                    description=f"Large execution gap detected: {improvement:.1%}"
                )
            patterns_found.add(pattern_id)
        
        # PATTERN 5: Adaptation effectiveness
        for adaptation in adaptations:
            pattern_id = f"adaptation_worked_{adaptation}"
            if improvement > 0.05:  # Si adaptation a aidé
                if pattern_id not in self.detected_patterns:
                    self.detected_patterns[pattern_id] = LearningPattern(
                        pattern_type=PatternType.ADAPTATION_EFFECTIVENESS,
                        factor_name=adaptation,
                        factor_value=improvement,
                        correlation_strength=0.7,
                        success_rate=0.8,
                        sample_size=1,
                        confidence=0.4,
                        description=f"Adaptation '{adaptation}' showed +{improvement:.1%} improvement"
                    )
                patterns_found.add(pattern_id)
        
        return patterns_found
    
    def _update_strategy_rules(
        self,
        record: Dict[str, Any],
        patterns: Set[str]
    ) -> None:
        """Crée/met à jour les règles stratégiques basées sur patterns."""
        
        for pattern_id in patterns:
            if pattern_id not in self.strategy_rules:
                pattern = self.detected_patterns[pattern_id]
                
                # Crée une règle
                if "humanization" in pattern_id:
                    rule = StrategyRule(
                        rule_id=f"rule_{pattern_id}",
                        condition=f"{pattern.factor_name} > 0.6",
                        action="increase_humanization_strength",
                        learning_pattern=pattern
                    )
                elif "cultural" in pattern_id:
                    rule = StrategyRule(
                        rule_id=f"rule_{pattern_id}",
                        condition=f"cultural_sensitivity > 0.7",
                        action="focus_cultural_messaging",
                        learning_pattern=pattern
                    )
                else:
                    rule = StrategyRule(
                        rule_id=f"rule_{pattern_id}",
                        condition="true",  # Toujours appliquer
                        action=f"apply_{pattern_id}",
                        learning_pattern=pattern
                    )
                
                self.strategy_rules[rule.rule_id] = rule
            
            # Met à jour l'efficacité de la règle
            rule = self.strategy_rules[f"rule_{pattern_id}"]
            pattern = self.detected_patterns[pattern_id]
            
            if record["improvement"] > 0:
                rule.success_count += 1
            else:
                rule.failure_count += 1
    
    def _generate_adaptation_suggestions(
        self,
        opportunity: Dict[str, Any],
        context: Dict[str, Any],
        patterns: Set[str]
    ) -> List[ContextualAdaptation]:
        """Génère des adaptations suggérées pour cet opportunité."""
        
        suggestions = []
        
        # Basées sur patterns détectés
        for pattern_id in patterns:
            pattern = self.detected_patterns[pattern_id]
            
            if pattern.pattern_type == PatternType.HUMANIZATION_BOOST:
                suggestions.append(ContextualAdaptation(
                    adaptation_type="HUMANIZATION",
                    priority=1,
                    description="Apply humanization to boost success",
                    expected_improvement=0.08,
                    implementation_effort=0.3
                ))
            
            elif pattern.pattern_type == PatternType.CULTURAL_ALIGNMENT:
                suggestions.append(ContextualAdaptation(
                    adaptation_type="CULTURAL",
                    priority=1,
                    description="Invest in cultural messaging and local partnerships",
                    expected_improvement=0.10,
                    implementation_effort=0.4
                ))
        
        # Basées sur le contexte
        cultural_fit = context.get("cultural_fit", 0.5)
        if cultural_fit < 0.6:
            suggestions.append(ContextualAdaptation(
                adaptation_type="CULTURAL",
                priority=2,
                description="Improve cultural fit before launch",
                expected_improvement=0.12,
                implementation_effort=0.5
            ))
        
        # Tries par ratio bénéfice/effort
        suggestions.sort(
            key=lambda s: s.benefit_effort_ratio(),
            reverse=True
        )
        
        return suggestions[:5]
    
    def _calculate_confidence_improvement(
        self,
        patterns: Set[str],
        adaptations_applied: List[str]
    ) -> float:
        """Calcule l'amélioration de confiance."""
        
        improvement = 0.0
        
        # Patterns forts augmentent la confiance
        for pattern_id in patterns:
            pattern = self.detected_patterns[pattern_id]
            if pattern.confidence > 0.6:
                improvement += pattern.confidence * 0.05
        
        # Adaptations efficaces augmentent la confiance
        for adaptation in adaptations_applied:
            pattern_id = f"adaptation_worked_{adaptation}"
            if pattern_id in self.detected_patterns:
                pattern = self.detected_patterns[pattern_id]
                if pattern.success_rate > 0.7:
                    improvement += 0.05
        
        return min(0.20, improvement)  # Max +20% confiance par cycle
    
    def _calculate_learning_velocity(self) -> float:
        """Calcule la vitesse d'apprentissage."""
        
        if len(self.decision_history) < 2:
            return 0.0
        
        # Regarde les 10 dernières décisions
        recent = self.decision_history[-10:]
        
        improvements = [r["improvement"] for r in recent]
        avg_improvement = sum(improvements) / len(improvements)
        
        return min(1.0, max(-1.0, avg_improvement))
    
    def _format_adaptations(
        self,
        adaptations: List[ContextualAdaptation]
    ) -> List[Dict[str, Any]]:
        """Formate les adaptations pour retour à l'utilisateur."""
        
        return [
            {
                "type": a.adaptation_type,
                "priority": a.priority,
                "description": a.description,
                "expected_improvement": f"{a.expected_improvement:.0%}",
                "effort": f"{a.implementation_effort:.0%}",
                "ratio": f"{a.benefit_effort_ratio():.2f}"
            }
            for a in adaptations
        ]
    
    def get_current_strategy_rules(self) -> List[Dict[str, Any]]:
        """Retourne les règles stratégiques actuelles."""
        
        rules_info = []
        
        for rule_id, rule in self.strategy_rules.items():
            if rule.effectiveness() > 0.5:  # Seulement les règles efficaces
                rules_info.append({
                    "rule_id": rule_id,
                    "condition": rule.condition,
                    "action": rule.action,
                    "effectiveness": f"{rule.effectiveness():.0%}",
                    "pattern_type": rule.learning_pattern.pattern_type.value,
                    "confidence": f"{rule.learning_pattern.confidence:.0%}"
                })
        
        # Tries par effectivité
        rules_info.sort(key=lambda r: float(r["effectiveness"].rstrip("%")) / 100, reverse=True)
        
        return rules_info
    
    def get_learning_summary(self) -> Dict[str, Any]:
        """Retourne un résumé de l'apprentissage."""
        
        return {
            "decisions_processed": len(self.decision_history),
            "patterns_detected": len(self.detected_patterns),
            "strategy_rules_created": len(self.strategy_rules),
            "learning_velocity": f"{self._calculate_learning_velocity():.1%}",
            "top_patterns": [
                {
                    "name": pid,
                    "type": self.detected_patterns[pid].pattern_type.value,
                    "strength": f"{self.detected_patterns[pid].correlation_strength:.0%}",
                    "samples": self.detected_patterns[pid].sample_size
                }
                for pid in sorted(
                    self.detected_patterns.keys(),
                    key=lambda p: self.detected_patterns[p].correlation_strength,
                    reverse=True
                )[:5]
            ]
        }


# Singleton global
_adaptation_layer: Optional[StrategicAdaptationLayer] = None


def get_adaptation_layer() -> StrategicAdaptationLayer:
    """Accès singleton au moteur d'adaptation."""
    global _adaptation_layer
    if _adaptation_layer is None:
        _adaptation_layer = StrategicAdaptationLayer()
    return _adaptation_layer


if __name__ == "__main__":
    # Test
    adapter = StrategicAdaptationLayer()
    
    # Simule quelques outcomes
    for i in range(5):
        result = adapter.adapt_from_outcome(
            decision_id=f"TEST_{i:03d}",
            opportunity={"name": f"Opp {i}", "value": 2_000_000},
            predicted_result=0.75 + (i * 0.01),
            actual_result=0.78 + (i * 0.015),
            execution_context={"cultural_fit": 0.75},
            adaptations_applied=["humanization"] if i % 2 == 0 else []
        )
        print(f"\nOutcome {i}:")
        print(f"  Improvement: {result['improvement']:+.1%}")
        print(f"  Patterns: {result['patterns_detected']}")
    
    print("\n--- Learning Summary ---")
    summary = adapter.get_learning_summary()
    print(f"Decisions: {summary['decisions_processed']}")
    print(f"Patterns: {summary['patterns_detected']}")
    print(f"Learning Velocity: {summary['learning_velocity']}")
