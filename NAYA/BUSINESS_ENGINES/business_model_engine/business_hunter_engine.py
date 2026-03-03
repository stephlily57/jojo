"""
Business Hunter Engine

Chasse, détecte et crée du business soluble réel et discret.
Identifie les opportunités cachées et les transforme en services Premium.

Stratégie:
- Hunting: Détecter les signaux faibles de problèmes réels
- Analysis: Évaluer viabilité et valeur
- Discrete Creation: Créer offer sans faire de bruit marketing
- Premium Execution: Services à haute valeur (10k-500k€+)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from datetime import datetime, timedelta
import hashlib


class OpportunitySignal(Enum):
    """Signaux révélant une opportunité cachée."""
    BUDGET_AVAILABLE = "budget_available"        # Budget non utilisé = pain point
    PROCESS_INEFFICIENCY = "inefficiency"       # Processus inefficace = coût caché
    COMPETING_MANUALLY = "manual_work"          # Faire à la main = automatable
    REGULATORY_PRESSURE = "regulatory"          # Compliance issue = urgent
    TALENT_SHORTAGE = "talent_gap"              # Pas assez d'experts = besoin
    TECH_DEBT = "tech_debt"                     # Infrastructure vieille = risque
    MARGIN_EROSION = "margin_pressure"          # Marge en baisse = urgence
    CUSTOMER_CHURN = "churn"                    # Clients partent = retention


class DiscreteServiceTier(Enum):
    """Niveaux de services discrets/premium."""
    ADVISORY = "advisory"                   # Strategic advice (€10k-50k)
    IMPLEMENTATION = "implementation"       # Full build/deploy (€25k-200k)
    TRANSFORMATION = "transformation"      # Business transformation (€50k-500k)
    PARTNERSHIP = "partnership"             # Joint venture/equity (€100k+)


@dataclass
class OpportunityScan:
    """Résultat du scan d'une opportunité."""

    scan_id: str
    organization_name: str
    industry: str
    signals_detected: List[OpportunitySignal] = field(default_factory=list)
    signal_strength: float = 0.0  # 0-1, confidence level
    estimated_value: float = 0.0  # Estimated annual value
    urgency_score: int = 0         # 1-10, how urgent
    competitive_gaps: List[str] = field(default_factory=list)

    def get_hunt_score(self) -> float:
        """Score cette opportunité pour hunting (0-100)."""
        return (
            (self.signal_strength * 40) +
            (min(self.urgency_score / 10, 1) * 30) +
            (min(self.estimated_value / 500000, 1) * 30)
        )


@dataclass
class DiscreteService:
    """Service discret/premium à haute valeur."""

    service_id: str
    name: str
    description: str
    tier: DiscreteServiceTier
    base_price: float              # Starting price
    scope: str
    deliverables: List[str] = field(default_factory=list)
    delivery_weeks: int = 4
    confidentiality_level: str = "HIGH"  # PUBLIC, CONFIDENTIAL, TOP_SECRET

    def is_discrete(self) -> bool:
        """Service is truly discrete/confidential."""
        return self.confidentiality_level in ["CONFIDENTIAL", "TOP_SECRET"]


class BusinessHunter:
    """
    Chasse les opportunités cachées dans les organisations.

    Méthode:
    1. Observer les comportements anormaux
    2. Identifier les signaux faibles
    3. Évaluer la valeur réelle
    4. Créer une offer discrète
    """

    def __init__(self):
        self.scans = {}
        self.hunt_history = []
        self.confidential_signals = {}

    def scan_organization(
        self,
        org_name: str,
        industry: str,
        revenue_range: str,
        observed_signals: Dict[OpportunitySignal, float]
    ) -> OpportunityScan:
        """
        Scan une organisation pour détecter les opportunités.

        Signaux observables:
        - Budget approuvé mais non dépensé (pain point réel)
        - Meetings fréquentes sur même sujet (urgence)
        - High headcount dans une area (inefficience)
        - Manual processes (automation = value)
        """

        scan_id = f"scan:{org_name}:{datetime.utcnow().isoformat()}"

        # Calculate signal strength
        total_signal = sum(observed_signals.values())
        signal_strength = min(total_signal / 5, 1.0)

        # Estimate value
        estimated_value = self._estimate_opportunity_value(
            industry,
            list(observed_signals.keys())
        )

        # Calculate urgency
        urgency_score = self._calculate_urgency(observed_signals)

        scan = OpportunityScan(
            scan_id=scan_id,
            organization_name=org_name,
            industry=industry,
            signals_detected=list(observed_signals.keys()),
            signal_strength=signal_strength,
            estimated_value=estimated_value,
            urgency_score=urgency_score
        )

        self.scans[scan_id] = scan
        self.hunt_history.append({
            'timestamp': datetime.utcnow().isoformat(),
            'org': org_name,
            'score': scan.get_hunt_score()
        })

        return scan

    def _estimate_opportunity_value(
        self,
        industry: str,
        signals: List[OpportunitySignal]
    ) -> float:
        """Estimer la valeur de l'opportunité."""

        # Base values by industry
        base_value = {
            'finance': 500000,
            'tech': 400000,
            'healthcare': 600000,
            'manufacturing': 350000,
            'retail': 250000,
            'energy': 700000,
            'other': 300000
        }

        industry_base = base_value.get(industry.lower(), 300000)

        # Amplify by signal count
        signal_multiplier = 1 + (len(signals) * 0.15)

        # Regulatory signals are worth 2x
        if OpportunitySignal.REGULATORY_PRESSURE in signals:
            signal_multiplier *= 1.5

        # Churn is critical
        if OpportunitySignal.CUSTOMER_CHURN in signals:
            signal_multiplier *= 1.3

        return industry_base * signal_multiplier

    def _calculate_urgency(self, signals: Dict[OpportunitySignal, float]) -> int:
        """Calculer l'urgence (1-10)."""

        urgency = 5  # Base

        # Regulatory = urgent
        if OpportunitySignal.REGULATORY_PRESSURE in signals:
            urgency += 3

        # Churn = urgent
        if OpportunitySignal.CUSTOMER_CHURN in signals:
            urgency += 2

        # Multiple signals = urgent
        if len(signals) >= 3:
            urgency += 2

        return min(urgency, 10)

    def get_hot_opportunities(self) -> List[Dict[str, Any]]:
        """Get top opportunities to hunt (scan score > 60)."""

        opportunities = [
            {
                'scan_id': scan.scan_id,
                'organization': scan.organization_name,
                'industry': scan.industry,
                'signals': [s.value for s in scan.signals_detected],
                'score': scan.get_hunt_score(),
                'estimated_value': scan.estimated_value,
                'urgency': scan.urgency_score
            }
            for scan in self.scans.values()
            if scan.get_hunt_score() >= 60
        ]

        return sorted(opportunities, key=lambda x: x['score'], reverse=True)


class DiscreteOfferingBuilder:
    """
    Crée des offerings discrets et premium basées sur les opportunités.

    Principe:
    - Silent deployment (pas de marketing)
    - High value (€25k minimum)
    - Customized to pain point
    - Confidential terms
    """

    def __init__(self):
        self.offers = {}

    def create_offer_for_scan(
        self,
        scan: OpportunityScan,
        suggested_tier: DiscreteServiceTier
    ) -> DiscreteService:
        """Crée une offer discrète pour une opportunité."""

        # Déterminer le nom/description basés sur les signaux
        if OpportunitySignal.MARGIN_EROSION in scan.signals_detected:
            name = "Margin Recovery Program"
            description = "Identify and recover lost margin"
        elif OpportunitySignal.CUSTOMER_CHURN in scan.signals_detected:
            name = "Retention & Growth Strategy"
            description = "Reduce churn, grow revenue"
        elif OpportunitySignal.TECH_DEBT in scan.signals_detected:
            name = "Technology Modernization"
            description = "Modernize infrastructure, reduce risk"
        elif OpportunitySignal.TALENT_SHORTAGE in scan.signals_detected:
            name = "Talent Augmentation Program"
            description = "Strategic talent expansion plan"
        else:
            name = "Business Optimization Program"
            description = f"Custom solution for {scan.organization_name}"

        # Pricing based on tier and value
        base_prices = {
            DiscreteServiceTier.ADVISORY: 25000,
            DiscreteServiceTier.IMPLEMENTATION: 75000,
            DiscreteServiceTier.TRANSFORMATION: 200000,
            DiscreteServiceTier.PARTNERSHIP: 500000
        }

        base_price = base_prices.get(suggested_tier, 50000)

        # Ajuster basé sur valeur estimée
        if scan.estimated_value > 500000:
            base_price *= 1.5

        service = DiscreteService(
            service_id=f"discrete:{scan.scan_id}",
            name=name,
            description=description,
            tier=suggested_tier,
            base_price=base_price,
            scope=f"Custom engagement for {scan.organization_name}",
            deliverables=[
                "Executive assessment",
                "Implementation roadmap",
                "Project execution",
                "Results verification"
            ],
            delivery_weeks=8,
            confidentiality_level="TOP_SECRET"
        )

        self.offers[service.service_id] = service
        return service

    def get_offers_for_industry(self, industry: str) -> List[DiscreteService]:
        """Get all discrete offers for an industry."""
        product_offers = []
        for offer in self.offers.values():
            if offer.confidentiality_level in ["CONFIDENTIAL", "TOP_SECRET"]:
                product_offers.append(offer)
        return product_offers


class ExecutionExecutor:
    """
    Exécute les services discrets de manière discrete.

    Caractéristiques:
    - Silent deployment
    - No public announcements
    - Confidential reporting
    - Results-focused
    """

    def __init__(self):
        self.active_engagements = {}
        self.completed_engagements = {}

    def launch_engagement(
        self,
        service: DiscreteService,
        client_org: str,
        nda_signed: bool = True,
        confidentiality_hash: str = None
    ) -> Dict[str, Any]:
        """Launch a discrete engagement."""

        if not nda_signed:
            return {'error': 'NDA required for premium services'}

        # Generate confidential engagement ID
        engagement_hash = hashlib.sha256(
            f"{service.service_id}:{client_org}:{datetime.utcnow().isoformat()}".encode()
        ).hexdigest()[:16]

        engagement_id = f"eng:{engagement_hash}"

        engagement = {
            'engagement_id': engagement_id,
            'service': service.name,
            'client': client_org,
            'start_date': datetime.utcnow().isoformat(),
            'expected_completion': (
                datetime.utcnow() + timedelta(weeks=service.delivery_weeks)
            ).isoformat(),
            'status': 'ACTIVE',
            'confidentiality_level': service.confidentiality_level,
            'milestones_completed': 0,
            'client_satisfaction': 0.0
        }

        self.active_engagements[engagement_id] = engagement

        return {
            'engagement_id': engagement_id,
            'status': 'LAUNCHED',
            'confidentiality': 'HIGH - No public announcements',
            'next_milestone': 'Executive assessment',
            'timeline': f"{service.delivery_weeks} weeks"
        }

    def update_engagement_progress(
        self,
        engagement_id: str,
        milestone_completed: str,
        satisfaction_update: float = None
    ) -> Dict[str, Any]:
        """Update engagement progress discretely."""

        if engagement_id not in self.active_engagements:
            return {'error': 'Engagement not found'}

        engagement = self.active_engagements[engagement_id]
        engagement['milestones_completed'] += 1
        engagement['last_milestone'] = milestone_completed
        engagement['last_update'] = datetime.utcnow().isoformat()

        if satisfaction_update:
            engagement['client_satisfaction'] = satisfaction_update

        return {
            'engagement_id': engagement_id,
            'status': 'ON_TRACK',
            'progress': f"{engagement['milestones_completed']} milestones completed"
        }

    def complete_engagement(
        self,
        engagement_id: str,
        final_results: Dict[str, Any],
        roi_achieved: float
    ) -> Dict[str, Any]:
        """Complete engagement and archive."""

        if engagement_id not in self.active_engagements:
            return {'error': 'Engagement not found'}

        engagement = self.active_engagements.pop(engagement_id)
        engagement['status'] = 'COMPLETED'
        engagement['completion_date'] = datetime.utcnow().isoformat()
        engagement['final_results'] = final_results
        engagement['roi_achieved'] = roi_achieved

        self.completed_engagements[engagement_id] = engagement

        return {
            'engagement_id': engagement_id,
            'status': 'COMPLETED',
            'roi': roi_achieved,
            'archive_status': 'CONFIDENTIAL_ARCHIVE'
        }


class BusinessHuntingOrchestrator:
    """
    Orchestre le cycle complet: Hunt → Analyze → Create → Execute
    """

    def __init__(self):
        self.hunter = BusinessHunter()
        self.builder = DiscreteOfferingBuilder()
        self.executor = ExecutionExecutor()

    def hunt_and_execute_cycle(
        self,
        org_name: str,
        industry: str,
        signals: Dict[OpportunitySignal, float]
    ) -> Dict[str, Any]:
        """
        Cycle complet:
        1. Scan l'organisation
        2. Évalue les signaux
        3. Crée une offer discrète
        4. Prépare l'engagement
        """

        # Step 1: Hunt
        scan = self.hunter.scan_organization(org_name, industry, "", signals)

        if scan.get_hunt_score() < 50:
            return {'status': 'OPPORTUNITY_INSUFFICIENT', 'score': scan.get_hunt_score()}

        # Step 2: Suggest tier based on value/urgency
        if scan.estimated_value > 800000:
            tier = DiscreteServiceTier.TRANSFORMATION
        elif scan.estimated_value > 300000:
            tier = DiscreteServiceTier.IMPLEMENTATION
        else:
            tier = DiscreteServiceTier.ADVISORY

        # Step 3: Create offer
        offer = self.builder.create_offer_for_scan(scan, tier)

        return {
            'status': 'OPPORTUNITY_IDENTIFIED',
            'organization': org_name,
            'hunt_score': scan.get_hunt_score(),
            'estimated_value': scan.estimated_value,
            'offered_service': offer.name,
            'service_value': offer.base_price,
            'confidentiality': offer.confidentiality_level,
            'ready_for_pitch': True
        }

    def get_hunting_dashboard(self) -> Dict[str, Any]:
        """Get complete hunting dashboard."""

        hot_opps = self.hunter.get_hot_opportunities()
        active = len(self.executor.active_engagements)
        completed = len(self.executor.completed_engagements)

        total_active_value = sum(
            e.get('client_satisfaction', 0) * 100000
            for e in self.executor.active_engagements.values()
        )

        return {
            'total_hunts': len(self.hunter.scans),
            'hot_opportunities': len(hot_opps),
            'top_opportunities': hot_opps[:5],
            'active_engagements': active,
            'completed_engagements': completed,
            'total_active_value': total_active_value,
            'discrete_offers_created': len(self.builder.offers)
        }


__all__ = [
    'BusinessHuntingOrchestrator',
    'BusinessHunter',
    'DiscreteOfferingBuilder',
    'ExecutionExecutor',
    'OpportunityScan',
    'DiscreteService',
    'OpportunitySignal'
]
