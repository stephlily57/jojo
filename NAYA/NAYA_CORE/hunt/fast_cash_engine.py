"""
NAYA_CORE v5.0 - FAST CASH ENGINE
24/48/72h Business Cash Deployment System
€10K-€80K daily execution without limits
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import asyncio
from concurrent.futures import ThreadPoolExecutor

# ============================================================================
# ENUMS & DATA STRUCTURES
# ============================================================================

class CashTier(Enum):
    """Daily cash deployment tiers"""
    TIER_24H = "24h"      # €10K-€20K, 4-hour decision
    TIER_48H = "48h"      # €20K-€50K, 8-hour decision
    TIER_72H = "72h"      # €50K-€80K, 16-hour decision


class CashStatus(Enum):
    """Deployment status tracking"""
    OPPORTUNITY = "opportunity_identified"
    ANALYZED = "analyzed_for_cash"
    OFFER_GENERATED = "offer_generated"
    DECISION_MADE = "decision_made"
    FUNDING_INITIATED = "funding_initiated"
    DEPLOYED = "deployed"
    REVENUE_ACTIVE = "revenue_active"
    COMPLETED = "completed"


@dataclass
class CashOpportunity:
    """Opportunity for fast cash deployment"""
    opportunity_id: str
    business_name: str
    
    # Financial profile
    annual_revenue: float
    daily_burn: float  # Daily operational cost
    monthly_recurring: float
    
    # Urgency & needs
    cash_needed: float  # How much needed
    time_available: float  # Hours until deadline
    use_case: str  # "payroll", "supplier", "inventory", "marketing"
    
    # Business health
    solvability_score: float  # From Hunt System (0-100)
    discretion_level: str  # From Hunt System
    
    # Metadata
    discovered_at: datetime = field(default_factory=datetime.now)
    status: CashStatus = CashStatus.OPPORTUNITY
    tier: Optional[CashTier] = None


@dataclass
class CashOffer:
    """Fast cash offer structure"""
    offer_id: str
    opportunity_id: str
    
    # Offer parameters
    capital_amount: float  # €
    revenue_share_percent: float  # 10-20%
    daily_income_target: float  # Expected daily revenue share
    
    # Timeline
    tier: CashTier
    deployment_hours: int
    estimated_payback_days: float
    
    # Metrics
    expected_monthly_return: float
    expected_annual_return: float
    risk_score: float  # 0-100 (higher = riskier)
    confidence: float  # 0-1.0 (from ML engine)
    
    # Rationale
    key_factors: List[str]
    risks: List[str]
    mitigation: List[str]


@dataclass
class CashPortfolio:
    """Portfolio of active cash deployments"""
    deployments: List[Dict] = field(default_factory=list)
    total_deployed: float = 0.0
    daily_revenue: float = 0.0  # Current daily revenue from portfolio
    monthly_revenue: float = 0.0
    success_rate: float = 0.0  # % of deployments generating revenue
    
    def add_deployment(self, deployment: Dict):
        """Add new deployment"""
        self.deployments.append(deployment)
        self.total_deployed += deployment['capital']
    
    def update_metrics(self):
        """Recalculate portfolio metrics"""
        if not self.deployments:
            return
        
        active = [d for d in self.deployments if d['status'] == 'active']
        successful = [d for d in active if d.get('daily_revenue', 0) > 0]
        
        self.daily_revenue = sum(d.get('daily_revenue', 0) for d in active)
        self.monthly_revenue = self.daily_revenue * 30
        self.success_rate = len(successful) / len(active) if active else 0.0


# ============================================================================
# FAST CASH ENGINE
# ============================================================================

class FastCashEngine:
    """
    Main engine for 24/48/72h fast cash deployment
    €10K-€80K daily execution
    """
    
    def __init__(self, max_workers: int = 10):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.portfolio = CashPortfolio()
        self.deployments = {}  # id -> deployment_record
        self.offer_history = []  # Track all offers generated
        
        # Performance metrics
        self.metrics = {
            'opportunities_analyzed': 0,
            'offers_generated': 0,
            'offers_accepted': 0,
            'deployments_active': 0,
            'total_deployed': 0.0,
            'daily_revenue': 0.0,
            'success_rate': 0.0,
        }
    
    # ========================================================================
    # CORE METHODS
    # ========================================================================
    
    def analyze_opportunity(self, opportunity: CashOpportunity) -> Tuple[CashTier, float]:
        """
        Analyze opportunity and assign to cash tier
        
        Returns: (tier, confidence_score)
        """
        # Time-based assignment
        if opportunity.time_available <= 12:  # <12 hours
            tier = CashTier.TIER_24H
            max_capital = 20000
        elif opportunity.time_available <= 24:  # <24 hours
            tier = CashTier.TIER_48H
            max_capital = 50000
        else:  # 24+ hours
            tier = CashTier.TIER_72H
            max_capital = 80000
        
        # Adjust by solvability
        confidence = self._calculate_confidence(opportunity)
        adjusted_capital = max_capital * confidence
        
        opportunity.tier = tier
        opportunity.status = CashStatus.ANALYZED
        self.metrics['opportunities_analyzed'] += 1
        
        return tier, confidence
    
    def generate_offers(self, opportunity: CashOpportunity, count: int = 3) -> List[CashOffer]:
        """
        Generate 3-4 different cash offer options
        """
        tier, confidence = self.analyze_opportunity(opportunity)
        
        offers = []
        
        # Offer 1: Conservative (lower capital, higher share)
        offer1 = self._create_offer(
            opportunity,
            tier,
            capital=self._get_tier_capital(tier) * 0.6,
            revenue_share=0.18,
            confidence=confidence
        )
        offers.append(offer1)
        
        # Offer 2: Balanced (medium capital, medium share)
        offer2 = self._create_offer(
            opportunity,
            tier,
            capital=self._get_tier_capital(tier) * 0.8,
            revenue_share=0.15,
            confidence=confidence
        )
        offers.append(offer2)
        
        # Offer 3: Aggressive (high capital, lower share)
        offer3 = self._create_offer(
            opportunity,
            tier,
            capital=self._get_tier_capital(tier) * 1.0,
            revenue_share=0.12,
            confidence=confidence
        )
        offers.append(offer3)
        
        # Optional: Offer 4 (special case)
        if count >= 4 and opportunity.solvability_score > 80:
            offer4 = self._create_offer(
                opportunity,
                tier,
                capital=self._get_tier_capital(tier) * 1.2,  # 20% boost
                revenue_share=0.10,  # Lower share for larger capital
                confidence=confidence * 0.95  # Slightly lower confidence
            )
            offers.append(offer4)
        
        opportunity.status = CashStatus.OFFER_GENERATED
        self.offer_history.extend(offers)
        self.metrics['offers_generated'] += len(offers)
        
        return offers
    
    async def deploy_cash(self, offer: CashOffer) -> Dict:
        """
        Deploy cash to opportunity
        Async for parallel execution
        """
        deployment = {
            'deployment_id': f"deploy_{offer.offer_id}",
            'offer_id': offer.offer_id,
            'opportunity_id': offer.opportunity_id,
            'capital': offer.capital_amount,
            'revenue_share': offer.revenue_share_percent,
            'tier': offer.tier.value,
            'deployed_at': datetime.now(),
            'status': 'active',
            'daily_revenue': 0.0,
            'total_collected': 0.0,
            'expected_return': offer.expected_annual_return,
        }
        
        # Store deployment
        self.deployments[deployment['deployment_id']] = deployment
        self.portfolio.add_deployment(deployment)
        self.metrics['deployments_active'] = len(self.deployments)
        self.metrics['total_deployed'] += offer.capital_amount
        
        # Simulate funding (in real world, this connects to fintech partners)
        await self._execute_funding(deployment)
        
        return deployment
    
    async def deploy_multiple(self, offers: List[CashOffer]) -> List[Dict]:
        """
        Deploy multiple cash offers simultaneously (async)
        """
        tasks = [self.deploy_cash(offer) for offer in offers]
        deployments = await asyncio.gather(*tasks)
        return deployments
    
    # ========================================================================
    # PRIVATE HELPER METHODS
    # ========================================================================
    
    def _calculate_confidence(self, opp: CashOpportunity) -> float:
        """
        Calculate confidence score for this opportunity
        
        Factors:
        - Solvability score from Hunt System (40%)
        - Revenue stability (30%)
        - Business health (20%)
        - Timeline fit (10%)
        """
        # Solvability (normalized 0-100 → 0-1)
        solv_factor = opp.solvability_score / 100.0 * 0.4
        
        # Revenue stability (monthly recurring / total revenue)
        stability = (opp.monthly_recurring * 12 / opp.annual_revenue) if opp.annual_revenue else 0
        stability_factor = min(stability, 1.0) * 0.3
        
        # Business health (burn rate < daily revenue?)
        health_factor = 0.2 if opp.daily_burn < (opp.monthly_recurring / 20) else 0.1
        
        # Timeline fit (more time = more confidence)
        time_factor = min(opp.time_available / 72, 1.0) * 0.1
        
        confidence = solv_factor + stability_factor + health_factor + time_factor
        return min(confidence, 1.0)  # Cap at 100%
    
    def _create_offer(self, opp: CashOpportunity, tier: CashTier,
                      capital: float, revenue_share: float, confidence: float) -> CashOffer:
        """Create individual offer"""
        
        # Calculate metrics
        daily_income = capital * revenue_share / 30  # Rough estimate
        estimated_payback_days = capital / daily_income if daily_income > 0 else 999
        
        return CashOffer(
            offer_id=f"offer_{opp.opportunity_id}_{len(self.offer_history)}",
            opportunity_id=opp.opportunity_id,
            capital_amount=capital,
            revenue_share_percent=revenue_share,
            daily_income_target=daily_income,
            tier=tier,
            deployment_hours=self._get_tier_hours(tier),
            estimated_payback_days=estimated_payback_days,
            expected_monthly_return=daily_income * 30,
            expected_annual_return=daily_income * 365,
            risk_score=self._calculate_risk(opp),
            confidence=confidence,
            key_factors=self._extract_key_factors(opp),
            risks=self._identify_risks(opp),
            mitigation=self._suggest_mitigation(opp),
        )
    
    def _get_tier_capital(self, tier: CashTier) -> float:
        """Get max capital for tier"""
        tiers = {
            CashTier.TIER_24H: 20000,
            CashTier.TIER_48H: 50000,
            CashTier.TIER_72H: 80000,
        }
        return tiers.get(tier, 20000)
    
    def _get_tier_hours(self, tier: CashTier) -> int:
        """Get deployment hours for tier"""
        tiers = {
            CashTier.TIER_24H: 4,
            CashTier.TIER_48H: 8,
            CashTier.TIER_72H: 16,
        }
        return tiers.get(tier, 4)
    
    def _calculate_risk(self, opp: CashOpportunity) -> float:
        """
        Calculate risk score (0-100)
        Higher = riskier
        """
        risk = 0.0
        
        # Solvability risk (inverse of score)
        risk += (100 - opp.solvability_score) * 0.3
        
        # Burn rate risk
        monthly_revenue = opp.monthly_recurring * 12 / 12
        if opp.daily_burn > (monthly_revenue / 20):
            risk += 20
        
        # Stability risk
        if opp.monthly_recurring < opp.annual_revenue * 0.5:
            risk += 15
        
        # Time pressure risk
        if opp.time_available < 24:
            risk += 10
        
        return min(risk, 100.0)
    
    def _extract_key_factors(self, opp: CashOpportunity) -> List[str]:
        """Extract key positive factors"""
        factors = []
        
        if opp.solvability_score > 80:
            factors.append("High solvability score")
        if opp.monthly_recurring > opp.annual_revenue * 0.7:
            factors.append("Strong recurring revenue")
        if opp.daily_burn < (opp.monthly_recurring / 25):
            factors.append("Healthy burn rate")
        if opp.time_available > 24:
            factors.append("Adequate decision time")
        
        # Add discretion level if available
        if opp.discretion_level in ["EVIDENT", "DISCRETION_LEVEL_1"]:
            factors.append(f"Obvious opportunity ({opp.discretion_level})")
        
        return factors or ["Viable business opportunity"]
    
    def _identify_risks(self, opp: CashOpportunity) -> List[str]:
        """Identify key risks"""
        risks = []
        
        if opp.solvability_score < 60:
            risks.append("Lower solvability score - verify fundamentals")
        if opp.daily_burn > (opp.monthly_recurring / 20):
            risks.append("Burn rate high - monitor cash carefully")
        if opp.time_available < 12:
            risks.append("Time pressure - tight decision window")
        if opp.monthly_recurring < opp.annual_revenue * 0.5:
            risks.append("Revenue concentration - seasonal or unpredictable")
        
        return risks or ["Standard market risk"]
    
    def _suggest_mitigation(self, opp: CashOpportunity) -> List[str]:
        """Suggest risk mitigation strategies"""
        mitigation = []
        
        if "burn rate" in str(self._identify_risks(opp)):
            mitigation.append("Monitor weekly revenue - adjust if needed")
        
        mitigation.append("Require weekly financial reporting")
        mitigation.append("Set up automated revenue share collection")
        mitigation.append("Build relationship with founder for transparency")
        mitigation.append("Have revenue reduction contingency plan")
        
        return mitigation
    
    async def _execute_funding(self, deployment: Dict):
        """
        Execute actual funding deployment
        (Integration point with fintech/banking partners)
        """
        # In production, this would:
        # 1. Create bank transfer
        # 2. Set up automated revenue share collection
        # 3. Send legal documents
        # 4. Monitor compliance
        
        # Simulate async funding process
        await asyncio.sleep(0.5)  # Placeholder for actual funding
        deployment['status'] = 'active'
        deployment['deployed_at'] = datetime.now()
    
    # ========================================================================
    # PORTFOLIO MANAGEMENT
    # ========================================================================
    
    def update_portfolio(self):
        """Update portfolio metrics"""
        self.portfolio.update_metrics()
        self.metrics['daily_revenue'] = self.portfolio.daily_revenue
        self.metrics['success_rate'] = self.portfolio.success_rate
    
    def get_portfolio_summary(self) -> Dict:
        """Get portfolio overview"""
        self.update_portfolio()
        return {
            'total_deployments': len(self.deployments),
            'total_deployed': self.metrics['total_deployed'],
            'daily_revenue': self.portfolio.daily_revenue,
            'monthly_revenue': self.portfolio.monthly_revenue,
            'success_rate': f"{self.portfolio.success_rate * 100:.1f}%",
            'next_30_days_revenue': self.portfolio.monthly_revenue,
            'next_year_revenue': self.portfolio.daily_revenue * 365,
        }
    
    def get_metrics(self) -> Dict:
        """Return current metrics"""
        return self.metrics.copy()


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    # Initialize engine
    engine = FastCashEngine()
    
    # Create test opportunity
    opp = CashOpportunity(
        opportunity_id="opp_001",
        business_name="Tech SaaS Company",
        annual_revenue=500000,
        daily_burn=800,
        monthly_recurring=40000,
        cash_needed=30000,
        time_available=48,  # 48 hours
        use_case="hiring",
        solvability_score=89.5,
        discretion_level="EVIDENT"
    )
    
    # Analyze and generate offers
    tier, confidence = engine.analyze_opportunity(opp)
    print(f"Tier: {tier.value}, Confidence: {confidence:.1%}")
    
    offers = engine.generate_offers(opp)
    print(f"\nGenerated {len(offers)} offers:")
    for offer in offers:
        print(f"  {offer.capital_amount}€ @ {offer.revenue_share_percent:.0%} = "
              f"{offer.expected_monthly_return:.0f}€/month")
    
    print(f"\nPortfolio: {engine.get_portfolio_summary()}")
