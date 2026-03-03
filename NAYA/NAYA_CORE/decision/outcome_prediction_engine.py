"""
Outcome Prediction Engine - Prédit les résultats avant exécution

Responsabilité:
  - Prédit le score de succès (0-1) d'une opportunité
  - Estime la confiance dans la prédiction
  - Identifie les risques probables
  - Recommande les adaptations préventives
  - S'améliore avec chaque feedback

Production: v1.0
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
import math
from datetime import datetime


class RiskLevel(Enum):
    """Niveaux de risque identifiés."""
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    MINIMAL = "MINIMAL"


class RecommendationType(Enum):
    """Types de recommandation."""
    EXECUTE = "EXECUTE"
    EXECUTE_WITH_ADAPTATIONS = "EXECUTE_WITH_ADAPTATIONS"
    PILOT = "PILOT"
    HOLD = "HOLD"


@dataclass
class RiskFactor:
    """Facteur de risque identifié."""
    category: str                    # "MARKET", "CULTURAL", "ECONOMIC", "EXECUTION", "TIMING"
    description: str                 # Description du risque
    probability: float               # 0-1, likelihood
    impact: float                    # 0-1, severity
    level: RiskLevel = field(init=False)
    mitigation: Optional[str] = None # Action pour mitiger
    
    def __post_init__(self):
        """Calcule le level basé sur probability*impact."""
        score = self.probability * self.impact
        if score >= 0.7:
            self.level = RiskLevel.CRITICAL
        elif score >= 0.5:
            self.level = RiskLevel.HIGH
        elif score >= 0.3:
            self.level = RiskLevel.MEDIUM
        elif score >= 0.15:
            self.level = RiskLevel.LOW
        else:
            self.level = RiskLevel.MINIMAL


@dataclass
class OpportunityScoringFactors:
    """Facteurs utilisés pour scorer une opportunité."""
    
    # Facteurs primaires (0-1)
    market_attractiveness: float = 0.5      # Taille + croissance + demande
    competitive_differentiation: float = 0.5  # Avantage unique?
    execution_capability: float = 0.5       # Peut-on vraiment l'exécuter?
    financial_viability: float = 0.5        # Margarine + ROI positif?
    cultural_fit: float = 0.5               # Aligné avec valeurs locales?
    timing_readiness: float = 0.5           # C'est le bon moment?
    
    # Facteurs secondaires
    team_experience: float = 0.5            # Expertise du team?
    market_timing: float = 0.5              # Fenêtre d'opportunité?
    regulatory_environment: float = 0.5     # Cadre légal OK?
    stakeholder_alignment: float = 0.5      # Tout le monde d'accord?
    
    # Poids (somme = 1.0)
    weights: Dict[str, float] = field(default_factory=lambda: {
        "market_attractiveness": 0.20,
        "competitive_differentiation": 0.15,
        "execution_capability": 0.20,
        "financial_viability": 0.15,
        "cultural_fit": 0.12,
        "timing_readiness": 0.10,
        "team_experience": 0.03,
        "market_timing": 0.03,
        "regulatory_environment": 0.01,
        "stakeholder_alignment": 0.01
    })


@dataclass
class PredictionResult:
    """Résultat d'une prédiction."""
    decision_id: str
    opportunity_name: str
    predicted_outcome: float              # 0-1, score de succès attendu
    confidence: float                     # 0-1, certitude dans la prédiction
    
    # Détails
    scoring_factors: OpportunityScoringFactors
    risk_factors: List[RiskFactor] = field(default_factory=list)
    
    # Recommandation
    recommendation: RecommendationType = RecommendationType.HOLD
    recommendation_reason: str = "Initial hold"
    
    # Adaptations suggérées
    suggested_adaptations: List[str] = field(default_factory=list)
    
    # Failure modes
    failure_modes: List[str] = field(default_factory=list)
    
    # Métadata
    timestamp: float = field(default_factory=lambda: datetime.now().timestamp())
    
    def summary(self) -> str:
        """Résumé lisible de la prédiction."""
        return f"""
Prediction for {self.opportunity_name}:
  Predicted: {self.predicted_outcome:.1%} success
  Confidence: {self.confidence:.1%}
  Recommendation: {self.recommendation.value}
  
Top Risks: {len(self.risk_factors)} identified
  {[r.description[:40] for r in self.risk_factors[:3]]}
  
Suggested Adaptations: {len(self.suggested_adaptations)}
  {self.suggested_adaptations[:3]}
""".strip()


class OutcomePredictionEngine:
    """
    Moteur de prédiction des résultats.
    
    Prédit les résultats d'une opportunité AVANT exécution.
    
    Utilise:
      - Analyses des facteurs d'opportunité
      - Profils de marché
      - Historique de fermetures similaires
      - Modèles de risque
      - Données comportementales
    
    Usage:
      predictor = OutcomePredictionEngine()
      
      prediction = predictor.predict_outcome(
          opportunity={...},
          market_context={...},
          historical_similar=[] # Cas similaires passés
      )
      
      print(f"Will likely be {prediction.predicted_outcome:.0%} successful")
      print(f"But we're only {prediction.confidence:.0%} sure")
      print(f"Recommendation: {prediction.recommendation.value}")
    
    Production: Ready
    """
    
    def __init__(self):
        self.past_predictions: Dict[str, PredictionResult] = {}
        self.outcome_history: Dict[str, Tuple[float, float]] = {}  # id -> (predicted, actual)
        
    def predict_outcome(
        self,
        opportunity: Dict[str, Any],
        market_context: Optional[Dict[str, Any]] = None,
        historical_similar: Optional[List[Dict[str, Any]]] = None,
        decision_id: Optional[str] = None
    ) -> PredictionResult:
        """
        Prédit le résultat d'une opportunité.
        
        Args:
            opportunity: Définition de l'opportunité
            market_context: Contexte du marché
            historical_similar: Cas historiques similaires
            decision_id: ID de la décision (optionnel)
        
        Returns:
            PredictionResult avec prédiction + risques + recommandations
        """
        
        if decision_id is None:
            decision_id = f"PRED_{datetime.now().timestamp():.0f}"
        
        opportunity_name = opportunity.get("name", "Unknown")
        
        # ÉTAPE 1: Évalue les facteurs de l'opportunité
        factors = self._evaluate_factors(opportunity, market_context)
        
        # ÉTAPE 2: Calcule le score initial
        base_score = self._calculate_opportunity_score(factors)
        
        # ÉTAPE 3: Identifie les risques
        risk_factors = self._identify_risks(opportunity, market_context)
        
        # ÉTAPE 4: Ajuste pour les risques
        adjusted_score = self._adjust_for_risks(base_score, risk_factors)
        
        # ÉTAPE 5: Estime la confiance
        confidence = self._calculate_confidence(
            factors=factors,
            risk_count=len(risk_factors),
            data_available=market_context is not None
        )
        
        # ÉTAPE 6: Identifie les modes d'échec
        failure_modes = self._identify_failure_modes(risk_factors)
        
        # ÉTAPE 7: Recommande des adaptations
        adaptations = self._recommend_adaptations(risk_factors, factors)
        
        # ÉTAPE 8: Génère la recommandation
        recommendation = self._generate_recommendation(adjusted_score, confidence, risk_factors)
        recommendation_reason = self._generate_reason(adjusted_score, confidence, risk_factors)
        
        # Crée la prédiction
        prediction = PredictionResult(
            decision_id=decision_id,
            opportunity_name=opportunity_name,
            predicted_outcome=adjusted_score,
            confidence=confidence,
            scoring_factors=factors,
            risk_factors=risk_factors,
            recommendation=recommendation,
            recommendation_reason=recommendation_reason,
            suggested_adaptations=adaptations,
            failure_modes=failure_modes
        )
        
        # Cache la prédiction
        self.past_predictions[decision_id] = prediction
        
        return prediction
    
    def _evaluate_factors(
        self,
        opportunity: Dict[str, Any],
        market_context: Optional[Dict[str, Any]] = None
    ) -> OpportunityScoringFactors:
        """Évalue tous les facteurs d'opportunité."""
        
        factors = OpportunityScoringFactors()
        
        # MARKET ATTRACTIVENESS
        value = opportunity.get("value", 0)
        if value >= 10_000_000:
            factors.market_attractiveness = 0.85
        elif value >= 5_000_000:
            factors.market_attractiveness = 0.75
        elif value >= 1_000_000:
            factors.market_attractiveness = 0.65
        else:
            factors.market_attractiveness = 0.45
        
        # COMPETITIVE DIFFERENTIATION
        pain_points = len(opportunity.get("pain_points", []))
        if pain_points >= 3:
            factors.competitive_differentiation = 0.80
        elif pain_points >= 2:
            factors.competitive_differentiation = 0.65
        else:
            factors.competitive_differentiation = 0.40
        
        # EXECUTION CAPABILITY
        # Défaut: haute (on assume que l'équipe est capable)
        factors.execution_capability = 0.75
        
        # FINANCIAL VIABILITY
        # Si premium positioning, plus risqué mais potentiel plus haut
        if opportunity.get("premium_positioning", False):
            factors.financial_viability = 0.70
        else:
            factors.financial_viability = 0.75
        
        # CULTURAL FIT
        # Dépend du contexte de marché
        if market_context:
            cultural_sensitivity = market_context.get("cultural_sensitivity", 0.5)
            factors.cultural_fit = 0.80 if cultural_sensitivity > 0.6 else 0.50
        else:
            factors.cultural_fit = 0.60
        
        # TIMING READINESS
        # Si c'est une prise de décision active, on est prêt
        factors.timing_readiness = 0.75
        
        # TEAM EXPERIENCE
        team_exp = opportunity.get("team_experience_level", 0.5)
        factors.team_experience = min(1.0, team_exp + 0.3)
        
        # MARKET TIMING
        market_temperature = market_context.get("market_temperature", 0.5) if market_context else 0.5
        factors.market_timing = market_temperature
        
        # REGULATORY ENVIRONMENT
        regulatory_risk = market_context.get("regulatory_risk", 0.3) if market_context else 0.3
        factors.regulatory_environment = 1.0 - regulatory_risk
        
        # STAKEHOLDER ALIGNMENT
        factors.stakeholder_alignment = 0.75
        
        return factors
    
    def _calculate_opportunity_score(self, factors: OpportunityScoringFactors) -> float:
        """Calcule le score pondéré de l'opportunité."""
        
        factor_values = {
            "market_attractiveness": factors.market_attractiveness,
            "competitive_differentiation": factors.competitive_differentiation,
            "execution_capability": factors.execution_capability,
            "financial_viability": factors.financial_viability,
            "cultural_fit": factors.cultural_fit,
            "timing_readiness": factors.timing_readiness,
            "team_experience": factors.team_experience,
            "market_timing": factors.market_timing,
            "regulatory_environment": factors.regulatory_environment,
            "stakeholder_alignment": factors.stakeholder_alignment
        }
        
        # Calcul pondéré
        score = sum(
            factor_values[key] * factors.weights[key]
            for key in factors.weights.keys()
            if key in factor_values
        )
        
        return min(1.0, max(0.0, score))
    
    def _identify_risks(
        self,
        opportunity: Dict[str, Any],
        market_context: Optional[Dict[str, Any]] = None
    ) -> List[RiskFactor]:
        """Identifie les risques pour cette opportunité."""
        
        risks = []
        
        # MARKET RISKS
        value = opportunity.get("value", 0)
        if value < 1_000_000:
            risks.append(RiskFactor(
                category="MARKET",
                description="Low value opportunity - capital efficiency risk",
                probability=0.5,
                impact=0.6,
                mitigation="Combine with other opportunities for better ROI"
            ))
        
        # EXECUTION RISKS
        if len(opportunity.get("pain_points", [])) < 2:
            risks.append(RiskFactor(
                category="EXECUTION",
                description="Limited pain points - unclear value proposition",
                probability=0.6,
                impact=0.7,
                mitigation="Deep market research to identify real pain points"
            ))
        
        # CULTURAL RISKS
        if market_context:
            cultural_alignment = market_context.get("cultural_sensitivity", 0.5)
            if cultural_alignment < 0.5:
                risks.append(RiskFactor(
                    category="CULTURAL",
                    description="Poor cultural alignment - trust building required",
                    probability=0.7,
                    impact=0.6,
                    mitigation="Invest in humanization and local partnerships"
                ))
        
        # TIMING RISKS
        market_saturation = market_context.get("market_saturation", 0.5) if market_context else 0.5
        if market_saturation > 0.7:
            risks.append(RiskFactor(
                category="TIMING",
                description="Market saturation - late entry risk",
                probability=0.5,
                impact=0.8,
                mitigation="Find differentiated positioning or new segments"
            ))
        
        # ECONOMIC RISKS
        if value > 50_000_000:
            risks.append(RiskFactor(
                category="ECONOMIC",
                description="Very large capital allocation - execution risk scales with size",
                probability=0.4,
                impact=0.9,
                mitigation="Stage the capital deployment"
            ))
        
        return risks
    
    def _adjust_for_risks(self, base_score: float, risk_factors: List[RiskFactor]) -> float:
        """Ajuste le score en fonction des risques."""
        
        # Calcule l'ajustement de risque
        risk_adjustment = 1.0
        
        for risk in risk_factors:
            if risk.level == RiskLevel.CRITICAL:
                risk_adjustment *= 0.70  # -30%
            elif risk.level == RiskLevel.HIGH:
                risk_adjustment *= 0.85  # -15%
            elif risk.level == RiskLevel.MEDIUM:
                risk_adjustment *= 0.95  # -5%
        
        adjusted = base_score * risk_adjustment
        return min(1.0, max(0.0, adjusted))
    
    def _calculate_confidence(
        self,
        factors: OpportunityScoringFactors,
        risk_count: int,
        data_available: bool = True
    ) -> float:
        """Estime la confiance dans la prédiction."""
        
        # Base: moyenne des facteurs
        base_confidence = sum([
            factors.market_attractiveness,
            factors.execution_capability,
            factors.financial_viability
        ]) / 3
        
        # Ajustement pour donnees
        if data_available:
            confidence = base_confidence * 0.90  # +confiance si contexte
        else:
            confidence = base_confidence * 0.65  # -confiance si peu de données
        
        # Ajustement pour risques
        if risk_count == 0:
            confidence *= 1.10  # Aucun risque = plus confiant
        elif risk_count >= 3:
            confidence *= 0.85  # Trop de risques = moins confiant
        
        return min(1.0, max(0.2, confidence))  # Min 20% confiance minimum
    
    def _identify_failure_modes(self, risk_factors: List[RiskFactor]) -> List[str]:
        """Identifie les modes d'échec potentiels."""
        
        modes = []
        
        for risk in risk_factors:
            if risk.level in [RiskLevel.CRITICAL, RiskLevel.HIGH]:
                if risk.category == "MARKET":
                    modes.append(f"Market failure: {risk.description}")
                elif risk.category == "CULTURAL":
                    modes.append(f"Cultural rejection: {risk.description}")
                elif risk.category == "EXECUTION":
                    modes.append(f"Execution failure: {risk.description}")
                elif risk.category == "TIMING":
                    modes.append(f"Timing miss: {risk.description}")
                elif risk.category == "ECONOMIC":
                    modes.append(f"Economic loss: {risk.description}")
        
        return modes
    
    def _recommend_adaptations(
        self,
        risk_factors: List[RiskFactor],
        factors: OpportunityScoringFactors
    ) -> List[str]:
        """Recommande les adaptations pour réduire le risque."""
        
        adaptations = []
        
        # Basées sur les risques
        for risk in risk_factors:
            if risk.mitigation:
                adaptations.append(risk.mitigation)
        
        # Basées sur les facteurs faibles
        if factors.cultural_fit < 0.6:
            adaptations.append("Invest strongly in humanization and cultural messaging")
        
        if factors.competitive_differentiation < 0.5:
            adaptations.append("Develop stronger unique value proposition")
        
        if factors.team_experience < 0.5:
            adaptations.append("Bring in external expertise or partnerships")
        
        return adaptations[:5]  # Max 5 adaptations
    
    def _generate_recommendation(
        self,
        score: float,
        confidence: float,
        risk_factors: List[RiskFactor]
    ) -> RecommendationType:
        """Génère la recommandation."""
        
        # Heuristique basée sur score + confiance + risques critiques
        critical_risks = [r for r in risk_factors if r.level == RiskLevel.CRITICAL]
        
        if critical_risks and score < 0.6:
            return RecommendationType.HOLD
        
        if score >= 0.75 and confidence >= 0.75:
            return RecommendationType.EXECUTE
        elif score >= 0.65 and confidence >= 0.65:
            return RecommendationType.EXECUTE_WITH_ADAPTATIONS
        elif score >= 0.55 and confidence >= 0.50:
            return RecommendationType.PILOT
        else:
            return RecommendationType.HOLD
    
    def _generate_reason(
        self,
        score: float,
        confidence: float,
        risk_factors: List[RiskFactor]
    ) -> str:
        """Génère la raison de la recommandation."""
        
        if score < 0.5:
            return f"Low predicted success ({score:.0%}) - multiple concerns"
        elif score < 0.65:
            reason = f"Moderate success predicted ({score:.0%})"
            if risk_factors:
                reason += f" but {len(risk_factors)} risks identified"
            return reason
        elif confidence < 0.6:
            return f"Good potential ({score:.0%}) but low confidence ({confidence:.0%}) due to insufficient data"
        else:
            return f"Strong opportunity ({score:.0%}) with good confidence ({confidence:.0%})"
    
    def register_actual_outcome(
        self,
        decision_id: str,
        actual_outcome: float
    ) -> Optional[float]:
        """
        Enregistre le résultat réel d'une prédiction.
        
        Returns:
            Erreur de prédiction (predicted - actual)
        """
        if decision_id not in self.past_predictions:
            return None
        
        prediction = self.past_predictions[decision_id]
        predicted = prediction.predicted_outcome
        
        error = abs(predicted - actual_outcome)
        self.outcome_history[decision_id] = (predicted, actual_outcome)
        
        return error
    
    def get_prediction_accuracy(self) -> Optional[float]:
        """Retourne l'accuracy des prédictions passées."""
        if not self.outcome_history:
            return None
        
        errors = [
            abs(predicted - actual)
            for predicted, actual in self.outcome_history.values()
        ]
        
        return 1.0 - (sum(errors) / len(errors))


# Singleton global
_prediction_engine: Optional[OutcomePredictionEngine] = None


def get_prediction_engine() -> OutcomePredictionEngine:
    """Accès singleton au moteur de prédiction."""
    global _prediction_engine
    if _prediction_engine is None:
        _prediction_engine = OutcomePredictionEngine()
    return _prediction_engine


if __name__ == "__main__":
    # Test
    predictor = OutcomePredictionEngine()
    
    opportunity = {
        "name": "BOTANICA_EGYPT",
        "value": 3_000_000,
        "pain_points": ["affordability", "quality", "trust"],
        "premium_positioning": True,
        "team_experience_level": 0.8
    }
    
    market = {
        "cultural_sensitivity": 0.8,
        "market_temperature": 0.7,
        "regulatory_risk": 0.2,
        "market_saturation": 0.4
    }
    
    prediction = predictor.predict_outcome(opportunity, market)
    print(prediction.summary())
