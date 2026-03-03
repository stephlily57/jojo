"""
Strategic Pricing & Fast Business Models

Génère des modèles business complets et vendables en 24-72h.
Stratégie: Premium Floor 1000€ minimum, cash rapide via bundling services.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from enum import Enum
from datetime import datetime, timedelta


class ServiceType(Enum):
    """Types de services deployables rapidement."""
    DIAGNOSTIC = "diagnostic"        # Analyse rapide (€1000-5000)
    AUDIT = "audit"                 # Audit complet (€5000-25000)
    CHATBOT = "chatbot"             # Chatbot custom (€10000-150000)
    CONSULTING = "consulting"       # Consulting (€3000-50000)
    IMPLEMENTATION = "implementation"  # Implementation (€5000-100000)


class ServiceTier(Enum):
    """Niveaux de service."""
    STARTER = "starter"             # Entry level, quick wins
    PROFESSIONAL = "professional"   # Standard deployment
    ENTERPRISE = "enterprise"       # Full-featured, premium


@dataclass
class ServiceOffering:
    """Single service offering with pricing."""

    service_type: ServiceType
    tier: ServiceTier
    name: str
    description: str
    base_price: float              # Minimum 1000€
    delivery_days: int             # How many days to deliver
    scope: str
    deliverables: List[str] = field(default_factory=list)

    def __post_init__(self):
        # Enforce premium floor
        if self.base_price < 1000:
            self.base_price = 1000

        assert self.delivery_days <= 3, "Must deliver in 72 hours max"


@dataclass
class ServiceBundle:
    """Bundle multiple services for higher value/margin."""

    bundle_id: str
    name: str
    description: str
    services: List[ServiceOffering] = field(default_factory=list)
    bundle_discount: float = 0      # Discount % for bundle
    total_days: int = 0

    def get_bundle_price(self) -> float:
        """Calculate bundled price with discount."""
        subtotal = sum(s.base_price for s in self.services)
        return subtotal * (1 - self.bundle_discount / 100)

    def recalc_delivery_time(self):
        """Recalculate total delivery time."""
        self.total_days = max((s.delivery_days for s in self.services), default=1)
        return self.total_days


class StrategicPricingEngine:
    """
    Complete Fast-Deploy Pricing Engine

    Features:
    - Premium floor: €1000 minimum
    - Fast deployment: 24-72 hours
    - Service bundling for premium pricing
    - Tiered offerings from quick wins to enterprise
    """

    PREMIUM_FLOOR = 1000
    MAX_DEPLOYMENT_DAYS = 3

    # Fast-Deploy Service Templates
    FAST_SERVICES = {
        # Diagnostics: Quick analysis
        'diagnostic_quick': ServiceOffering(
            service_type=ServiceType.DIAGNOSTIC,
            tier=ServiceTier.STARTER,
            name="Quick Diagnostic",
            description="2-hour analysis of your business problem",
            base_price=1000,
            delivery_days=1,
            scope="Quick analysis and report",
            deliverables=["Discovery call", "Analysis document", "2-page recommendation"]
        ),

        # Full audit
        'audit_standard': ServiceOffering(
            service_type=ServiceType.AUDIT,
            tier=ServiceTier.PROFESSIONAL,
            name="Complete Audit",
            description="Deep-dive analysis with implementation roadmap",
            base_price=5000,
            delivery_days=2,
            scope="2-day on-site/remote audit",
            deliverables=["Audit report", "Gap analysis", "30-60-90 roadmap", "Training session"]
        ),

        'audit_enterprise': ServiceOffering(
            service_type=ServiceType.AUDIT,
            tier=ServiceTier.ENTERPRISE,
            name="Enterprise Audit + Strategy",
            description="Full audit with strategic recommendations",
            base_price=15000,
            delivery_days=3,
            scope="Multi-day comprehensive audit",
            deliverables=["Audit report", "Strategic plan", "Executive briefing", "12-month roadmap"]
        ),

        # Chatbot implementations
        'chatbot_voice': ServiceOffering(
            service_type=ServiceType.CHATBOT,
            tier=ServiceTier.STARTER,
            name="Basic Chatbot",
            description="Simple FAQ chatbot deployment",
            base_price=5000,
            delivery_days=2,
            scope="Basic Q&A chatbot",
            deliverables=["Chatbot deployed", "Training", "100x conversation support"]
        ),

        'chatbot_pro': ServiceOffering(
            service_type=ServiceType.CHATBOT,
            tier=ServiceTier.PROFESSIONAL,
            name="Professional AI Chatbot",
            description="Advanced chatbot with learning",
            base_price=25000,
            delivery_days=3,
            scope="Custom AI chatbot with business logic",
            deliverables=["Custom chatbot", "Integration", "Analytics dashboard", "3-month support"]
        ),

        'chatbot_enterprise': ServiceOffering(
            service_type=ServiceType.CHATBOT,
            tier=ServiceTier.ENTERPRISE,
            name="Enterprise Chatbot Suite",
            description="Full conversational AI platform",
            base_price=75000,
            delivery_days=3,
            scope="Complete AI platform with multi-channel",
            deliverables=["Multi-channel chatbot", "CRM integration", "API access", "12-month support", "Custom training"]
        ),

        # Consulting
        'consulting_day': ServiceOffering(
            service_type=ServiceType.CONSULTING,
            tier=ServiceTier.STARTER,
            name="1-Day Workshop",
            description="Strategic workshop with your team",
            base_price=3000,
            delivery_days=1,
            scope="1 day on-site consulting",
            deliverables=["Workshop facilitation", "Action items list", "Follow-up email"]
        ),

        'consulting_sprint': ServiceOffering(
            service_type=ServiceType.CONSULTING,
            tier=ServiceTier.PROFESSIONAL,
            name="3-Day Strategy Sprint",
            description="Intensive strategy development",
            base_price=12000,
            delivery_days=3,
            scope="3-day intensive sprint",
            deliverables=["Strategy document", "Implementation plan", "Quarterly reviews included"]
        ),
    }

    def __init__(self):
        self.services = self.FAST_SERVICES.copy()
        self.custom_bundles = {}

    def create_cash_bundle(
        self,
        bundle_name: str,
        target_price: float,
        services_to_include: List[str],
        discount_percent: float = 10
    ) -> ServiceBundle:
        """
        Create a bundle targeting specific price for quick deployment.

        Example: "Start to Enterprise" - 1000€ diagnostic + 5000€ audit = 6000€
        but bundle them at 5500€ to drive adoption.
        """

        selected_services = [
            self.services[s] for s in services_to_include
            if s in self.services
        ]

        bundle = ServiceBundle(
            bundle_id=f"bundle:{bundle_name}:{datetime.utcnow().isoformat()}",
            name=bundle_name,
            description=f"Complete {bundle_name} package",
            services=selected_services,
            bundle_discount=discount_percent
        )

        bundle.recalc_delivery_time()
        self.custom_bundles[bundle.bundle_id] = bundle

        return bundle

    def get_fast_cash_options(self) -> List[Dict[str, Any]]:
        """Return fastest ways to generate cash (24-72h)."""

        options = []

        for key, service in self.services.items():
            if service.delivery_days <= self.MAX_DEPLOYMENT_DAYS:
                options.append({
                    'service_key': key,
                    'name': service.name,
                    'type': service.service_type.value,
                    'tier': service.tier.value,
                    'price': service.base_price,
                    'delivery_days': service.delivery_days,
                    'scope': service.scope,
                    'roi_days': max(1, service.delivery_days)  # ROI in delivery time
                })

        # Sort by value/time ratio (fastest ROI)
        return sorted(
            options,
            key=lambda x: x['price'] / max(1, x['delivery_days']),
            reverse=True
        )

    def get_bundle_recommendations(self) -> List[Dict[str, Any]]:
        """Get recommended bundles for maximum revenue."""

        recommendations = [
            {
                'bundle': 'Starter Quick Win',
                'description': 'Fastest cash in 24h',
                'price': 3000,
                'services': ['diagnostic_quick', 'consulting_day'],
                'delivery_days': 1
            },
            {
                'bundle': 'Professional Audit',
                'description': 'Complete solution in 2-3 days',
                'price': 8000,  #€5000 audit + €3000 consulting, bundled
                'services': ['audit_standard', 'consulting_day'],
                'delivery_days': 2
            },
            {
                'bundle': 'Enterprise Transform',
                'description': 'Premium package delivering value',
                'price': 24000,  # €15000 audit + €10000 chatbot, bundled
                'services': ['audit_enterprise', 'chatbot_pro'],
                'delivery_days': 3
            },
            {
                'bundle': 'Chatbot Powerhouse',
                'description': 'AI automation solution',
                'price': 32000,  # €25000 chatbot + €8000 consulting, bundled
                'services': ['chatbot_pro', 'consulting_sprint'],
                'delivery_days': 3
            },
            {
                'bundle': 'Enterprise AI Suite',
                'description': 'Maximum value, premium positioning',
                'price': 98000,  # €75000 enterprise chatbot + €25000 audit, bundled
                'services': ['chatbot_enterprise', 'audit_enterprise'],
                'delivery_days': 3
            }
        ]

        return recommendations

    def calculate_price(self, impact_value, client_capacity):
        """
        Legacy method - calculate strategic price based on impact.
        Enforces premium floor €1000 minimum.
        """

        base_price = max(impact_value * 0.2, self.PREMIUM_FLOOR)

        if client_capacity < base_price:
            return None

        return round(base_price, 2)

    def generate_quick_proposal(
        self,
        client_name: str,
        problem_area: str,
        budget: float,
        timeline_days: int = 3
    ) -> Dict[str, Any]:
        """Generate a complete sales proposal for quick deployment."""

        best_services = []
        remaining_budget = budget

        # Recommend services within budget and timeline
        for key, service in sorted(
            self.services.items(),
            key=lambda x: x[1].base_price,
            reverse=True
        ):
            if (service.base_price <= remaining_budget and
                service.delivery_days <= timeline_days):
                best_services.append(service)
                remaining_budget -= service.base_price

        if not best_services:
            # Fallback: diagnostic
            best_services = [self.services['diagnostic_quick']]

        total_price = sum(s.base_price for s in best_services)

        return {
            'client': client_name,
            'problem': problem_area,
            'proposal_id': f"prop:{datetime.utcnow().isoformat()}",
            'proposed_services': [
                {
                    'name': s.name,
                    'price': s.base_price,
                    'days': s.delivery_days,
                    'deliverables': s.deliverables
                }
                for s in best_services
            ],
            'total_price': total_price,
            'timeline': max((s.delivery_days for s in best_services), default=1),
            'proposed_start': datetime.utcnow().isoformat(),
            'estimated_completion': (
                datetime.utcnow() + timedelta(days=max((s.delivery_days for s in best_services), default=1))
            ).isoformat()
        }


__all__ = ['StrategicPricingEngine', 'ServiceOffering', 'ServiceBundle', 'ServiceType', 'ServiceTier']
