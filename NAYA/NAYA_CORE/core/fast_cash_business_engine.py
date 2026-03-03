"""
NAYA_CORE v4.2 - Fast Cash Business Engine

Génération rapide de cash: 24h, 48h, 72h, 3 jours
Montants: €10K, €25K, €50K, €80K par jour
Aucune limite de montant total

Modèle: Opportunités solvables + Capital rapide = Cash flows
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
import asyncio
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json


class CashHorizon(Enum):
    """Horizons temporels de cash rapide"""
    HOUR_24 = "24h"
    HOUR_48 = "48h"
    HOUR_72 = "72h"
    DAY_3 = "3_days"


class CashTier(Enum):
    """Montants standardisés par horizon"""
    TIER_10K = 10000      # €10K - Quick wins, invoices
    TIER_25K = 25000      # €25K - Working capital
    TIER_50K = 50000      # €50K - Team/expansion
    TIER_80K = 80000      # €80K - Major acceleration


@dataclass
class FastCashOpportunity:
    """Opportunité de cash rapide"""
    id: str
    name: str
    category: str                    # "invoice", "receivable", "revenue", "contract"
    current_cash_gap: float
    target_cash_amount: float
    horizon: CashHorizon
    tier: CashTier
    solvability_score: float         # 0-100
    risk_level: str                  # "low", "medium", "high"
    
    # Détails de l'opportunité
    business_revenue: float
    monthly_recurring: float
    customer_count: int
    retention_rate: float
    
    # Timing
    urgency_level: str               # "critical", "high", "medium", "low"
    deadline: datetime
    
    # Contact
    contact_name: str
    contact_phone: str
    contact_email: str
    
    # Metadata
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)


@dataclass
class FastCashSolution:
    """Solution de cash rapide générée"""
    opportunity_id: str
    solution_id: str
    
    # Offre
    capital_provided: float
    revenue_share: float            # % de revenue à payer
    
    # Timeline
    horizon: CashHorizon
    funding_date: datetime
    repayment_date: datetime
    
    # Termes
    interest_rate: float            # Taux si applicable
    equivalent_multiple: float      # Équivalent en multiple
    
    # Métriques
    expected_roi: float
    confidence: float
    risk_mitigation: List[str]
    
    # Rationale
    rationale: str
    success_factors: List[str]
    

class FastCashBusinessEngine:
    """Moteur de génération de cash rapide"""
    
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=5)
        self.solutions_cache: Dict[str, FastCashSolution] = {}
        self.performance_metrics = {
            "24h_success_rate": 0.78,
            "48h_success_rate": 0.82,
            "72h_success_rate": 0.85,
            "3d_success_rate": 0.88,
        }
    
    def generate_fast_cash_solution(
        self, 
        opportunity: FastCashOpportunity
    ) -> FastCashSolution:
        """
        Génère une solution de cash rapide pour une opportunité
        """
        
        # Évaluer urgence et solvabilité
        urgency_score = self._calculate_urgency(opportunity)
        solvability_adjusted = opportunity.solvability_score * 0.9 if urgency_score > 0.8 else opportunity.solvability_score
        
        # Déterminer capital et termes
        capital = self._determine_capital(opportunity, urgency_score)
        revenue_share = self._calculate_revenue_share(opportunity, urgency_score)
        roi = self._project_roi(opportunity, capital, revenue_share)
        
        # Créer solution
        solution = FastCashSolution(
            opportunity_id=opportunity.id,
            solution_id=self._generate_solution_id(opportunity),
            capital_provided=capital,
            revenue_share=revenue_share,
            horizon=opportunity.horizon,
            funding_date=datetime.now(),
            repayment_date=self._calculate_repayment_date(opportunity.horizon),
            interest_rate=self._calculate_interest(opportunity.horizon, urgency_score),
            equivalent_multiple=1.2 if opportunity.horizon == CashHorizon.HOUR_24 else (
                1.3 if opportunity.horizon == CashHorizon.HOUR_48 else (
                    1.5 if opportunity.horizon == CashHorizon.HOUR_72 else 1.8
                )
            ),
            expected_roi=roi,
            confidence=self._calculate_confidence(opportunity, urgency_score),
            risk_mitigation=self._identify_risks(opportunity),
            rationale=f"Fast cash opportunity: {opportunity.name} needs €{capital:,.0f} in {opportunity.horizon.value}",
            success_factors=[
                f"Solvability score: {solvability_adjusted:.1f}/100",
                f"Monthly recurring: €{opportunity.monthly_recurring:,.0f}",
                f"Retention rate: {opportunity.retention_rate:.0%}",
                f"Customer count: {opportunity.customer_count}"
            ]
        )
        
        self.solutions_cache[solution.solution_id] = solution
        return solution
    
    def batch_fast_cash_hunt(
        self,
        opportunities: List[FastCashOpportunity],
        max_parallel: int = 5
    ) -> Tuple[List[FastCashSolution], Dict]:
        """
        Génère solutions en parallèle pour batch d'opportunités
        """
        solutions = []
        
        # Process en parallèle
        futures = []
        for opp in opportunities[:max_parallel]:
            future = self.executor.submit(self.generate_fast_cash_solution, opp)
            futures.append((opp.id, future))
        
        for opp_id, future in futures:
            try:
                solution = future.result(timeout=10)
                solutions.append(solution)
            except Exception as e:
                print(f"Error processing {opp_id}: {str(e)}")
        
        # Stats
        stats = {
            "total_processed": len(opportunities),
            "solutions_generated": len(solutions),
            "total_capital_offered": sum(s.capital_provided for s in solutions),
            "avg_roi": sum(s.expected_roi for s in solutions) / len(solutions) if solutions else 0,
            "success_rate": len(solutions) / len(opportunities) if opportunities else 0,
        }
        
        return solutions, stats
    
    def execute_fast_cash_call(
        self,
        solution: FastCashSolution,
        contact_data: Dict
    ) -> Dict:
        """
        Exécute l'appel de déploiement cash rapide
        """
        
        execution_plan = {
            "solution_id": solution.solution_id,
            "status": "ready_to_call",
            "call_script": self._generate_call_script(solution, contact_data),
            "key_talking_points": [
                f"We can deploy €{solution.capital_provided:,.0f} in {solution.horizon.value}",
                f"Simple revenue sharing: {solution.revenue_share:.0%} of new revenue",
                f"No dilution, no complexity",
                f"Repayment by {solution.repayment_date.strftime('%Y-%m-%d')}"
            ],
            "objection_handlers": self._create_objection_handlers(),
            "next_steps": [
                "Initial call: Interest gauge",
                "Follow-up: Detailed terms",
                "Documentation: Sign & deploy",
                f"Funding: {solution.funding_date.strftime('%Y-%m-%d')}"
            ]
        }
        
        return execution_plan
    
    # ========== HELPER METHODS ==========
    
    def _calculate_urgency(self, opp: FastCashOpportunity) -> float:
        """Calcule level d'urgence 0-1"""
        if opp.urgency_level == "critical":
            return 1.0
        elif opp.urgency_level == "high":
            return 0.75
        elif opp.urgency_level == "medium":
            return 0.5
        return 0.25
    
    def _determine_capital(self, opp: FastCashOpportunity, urgency: float) -> float:
        """Détermine montant de capital à offrir"""
        # Base sur solvabilité et urgency
        if opp.solvability_score >= 85:
            base_capital = min(opp.tier.value * 1.2, opp.target_cash_amount)
        elif opp.solvability_score >= 70:
            base_capital = opp.tier.value
        else:
            base_capital = opp.tier.value * 0.7
        
        return base_capital
    
    def _calculate_revenue_share(self, opp: FastCashOpportunity, urgency: float) -> float:
        """Calcule % de revenue share"""
        base_share = {
            CashHorizon.HOUR_24: 0.15,
            CashHorizon.HOUR_48: 0.18,
            CashHorizon.HOUR_72: 0.20,
            CashHorizon.DAY_3: 0.22,
        }
        
        share = base_share.get(opp.horizon, 0.20)
        
        # Ajuster pour urgency et solvabilité
        if urgency > 0.8:
            share += 0.03
        
        if opp.solvability_score < 70:
            share += 0.05
        
        return min(share, 0.40)  # Cap à 40%
    
    def _project_roi(self, opp: FastCashOpportunity, capital: float, share: float) -> float:
        """Projette ROI"""
        # Projection basée sur monthly recurring
        if opp.monthly_recurring == 0:
            return 1.0
        
        monthly_share = opp.monthly_recurring * share
        total_12m = monthly_share * 12
        roi = (total_12m + capital) / capital if capital > 0 else 1.0
        
        return min(roi, 3.0)  # Cap ROI à 3x
    
    def _calculate_interest(self, horizon: CashHorizon, urgency: float) -> float:
        """Calcule taux d'intérêt si applicable"""
        rates = {
            CashHorizon.HOUR_24: 0.05,
            CashHorizon.HOUR_48: 0.04,
            CashHorizon.HOUR_72: 0.03,
            CashHorizon.DAY_3: 0.02,
        }
        
        base_rate = rates.get(horizon, 0.03)
        
        # Ajuster pour urgency
        if urgency > 0.8:
            base_rate += 0.02
        
        return base_rate
    
    def _calculate_repayment_date(self, horizon: CashHorizon) -> datetime:
        """Calcule date de repayment"""
        base = datetime.now()
        
        if horizon == CashHorizon.HOUR_24:
            return base + timedelta(days=7)
        elif horizon == CashHorizon.HOUR_48:
            return base + timedelta(days=14)
        elif horizon == CashHorizon.HOUR_72:
            return base + timedelta(days=30)
        else:
            return base + timedelta(days=60)
    
    def _calculate_confidence(self, opp: FastCashOpportunity, urgency: float) -> float:
        """Calcule confidence 0-1"""
        base_confidence = opp.solvability_score / 100.0
        
        # Facteurs positifs
        if opp.monthly_recurring > 0:
            base_confidence += 0.1
        if opp.retention_rate > 0.8:
            base_confidence += 0.05
        if opp.customer_count > 50:
            base_confidence += 0.05
        
        # Facteurs négatifs
        if opp.risk_level == "high":
            base_confidence -= 0.15
        elif opp.risk_level == "medium":
            base_confidence -= 0.05
        
        return min(max(base_confidence, 0.3), 1.0)
    
    def _identify_risks(self, opp: FastCashOpportunity) -> List[str]:
        """Identifie risques et mitigations"""
        risks = []
        
        if opp.risk_level == "high":
            risks.append("High risk: Require collateral or personal guarantee")
        
        if opp.retention_rate < 0.7:
            risks.append("Customer churn risk: Milestone-based disbursement")
        
        if opp.customer_count < 10:
            risks.append("Small customer base: Revenue escrow account")
        
        if opp.monthly_recurring == 0:
            risks.append("No recurring revenue: Weekly reporting required")
        
        return risks
    
    def _generate_solution_id(self, opp: FastCashOpportunity) -> str:
        """Génère ID unique pour solution"""
        data = f"{opp.id}{opp.name}{datetime.now().isoformat()}"
        return f"CASH-{hashlib.md5(data.encode()).hexdigest()[:12].upper()}"
    
    def _generate_call_script(self, solution: FastCashSolution, contact: Dict) -> str:
        """Génère script d'appel"""
        return f"""
Hi {contact.get('name', 'there')},

We've been watching {contact.get('company', 'your business')} - impressive growth!

We've structured a fast-cash opportunity specifically for you:
- €{solution.capital_provided:,.0f} deployed in {solution.horizon.value}
- Simple structure: {solution.revenue_share:.0%} of NEW revenue only
- Keep full control, no equity dilution
- Repay by {solution.repayment_date.strftime('%b %d')}

This is designed to accelerate your growth without complexity.

Makes sense? Let's do a quick 15-min call this week to review structure.
"""
    
    def _create_objection_handlers(self) -> Dict[str, str]:
        """Crée handlers pour objections courantes"""
        return {
            "too_much_revenue_share": "Revenue share only applies to NEW revenue above baseline - you keep existing cash",
            "too_risky": "We take risk because we know you'll execute - aligned incentives",
            "prefer_equity": "No equity dilution means you stay in control - we profit when you profit",
            "need_to_think": "Offer is valid for 72 hours - let's schedule follow-up tomorrow?",
            "too_slow": "Actually, 24h funding - we can wire by end of business today",
        }


# ========== PUBLIC API ==========

def create_fast_cash_engine() -> FastCashBusinessEngine:
    """Factory pour créer engine"""
    return FastCashBusinessEngine()


def execute_fast_cash_hunt(
    opportunities: List[Dict],
    max_parallel: int = 5
) -> Tuple[List[FastCashSolution], Dict]:
    """
    API publique: Exécute hunt de fast cash
    """
    engine = create_fast_cash_engine()
    
    # Converter dicts to opportunities
    opp_objects = [
        FastCashOpportunity(
            id=opp['id'],
            name=opp['name'],
            category=opp.get('category', 'general'),
            current_cash_gap=opp.get('current_cash_gap', 0),
            target_cash_amount=opp.get('target_cash_amount', 50000),
            horizon=CashHorizon(opp.get('horizon', '24h')),
            tier=CashTier(opp.get('tier', 50000)),
            solvability_score=opp.get('solvability_score', 75),
            risk_level=opp.get('risk_level', 'medium'),
            business_revenue=opp.get('revenue', 0),
            monthly_recurring=opp.get('monthly_recurring', 0),
            customer_count=opp.get('customer_count', 0),
            retention_rate=opp.get('retention_rate', 0.5),
            urgency_level=opp.get('urgency', 'medium'),
            deadline=datetime.now() + timedelta(days=7),
            contact_name=opp.get('contact_name', ''),
            contact_phone=opp.get('contact_phone', ''),
            contact_email=opp.get('contact_email', ''),
            tags=opp.get('tags', []),
            metadata=opp.get('metadata', {}),
        )
        for opp in opportunities
    ]
    
    return engine.batch_fast_cash_hunt(opp_objects, max_parallel)
