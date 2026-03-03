"""
NAYA_HUNT_ORCHESTRATION - Intégration Complète du Système de Chasse Avancé

Orchestre:
1. Détection de solvabilité réelle (vs illusions)
2. Classification par discrétion (Évident → Secret)
3. Horizons multiples (24h → 2 ans)
4. Génération d'offres naturelles
5. Multi-marchés & tous les paliers
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from datetime import datetime
from NAYA_CORE.hunt.advanced_hunt_engine import (
    create_advanced_hunt_system,
    SolvabilityLevel,
    OfferTemplate
)


@dataclass
class HuntOpportunity:
    """Opportunité structurée pour la chasse."""
    id: str
    name: str
    market: str
    
    # Fundamentals
    annual_revenue: float = 0.0
    monthly_revenue: float = 0.0
    monthly_recurring: float = 0.0
    monthly_burn: float = 0.0
    
    # Growth & Health
    revenue_growth_rate: float = 0.0  # % annual
    customer_retention_rate: float = 0.7
    net_margin: float = 0.0
    gross_margin: float = 0.3
    
    # Assets & Quality
    asset_value: float = 0.0
    cash_position: float = 0.0
    years_operating: int = 1
    customer_count: int = 0
    
    # Strategic Factors
    has_ip: bool = False
    is_defensible: bool = False
    has_network_effects: bool = False
    owner_committed: bool = True
    
    # Market Factors
    market_size: float = 0.0
    market_growth_rate: float = 0.0
    market_share: float = 0.0
    
    # Valuation & Potential
    valuation: float = 0.0
    top_customer_ratio: float = 0.0  # % revenue from top customer
    
    # Quick Wins
    quick_wins: List[Dict[str, Any]] = field(default_factory=list)


class HuntOrchestrationLayer:
    """Layer d'orchestration pour la chasse avancée intégrée au Super Brain."""

    def __init__(self):
        self.hunt_system = create_advanced_hunt_system()
        self.discovered_opportunities: Dict[str, HuntOpportunity] = {}
        self.active_campaigns: Dict[str, Dict[str, Any]] = {}
        self.cash_flow_timeline: Dict[str, float] = {
            "24h": 0,
            "48h": 0,
            "72h": 0,
            "6m": 0,
            "2y": 0
        }

    def discover_opportunities(self, market_scans: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Découvre et analyse les opportunités."""
        
        # Convert market scans to structured opportunities
        opportunities = []
        
        for scan in market_scans:
            opp = HuntOpportunity(
                id=scan.get("id", f"OPP-{int(datetime.utcnow().timestamp())}"),
                name=scan.get("name", "Unknown"),
                market=scan.get("market", "unknown"),
                annual_revenue=float(scan.get("annual_revenue", 0)),
                monthly_revenue=float(scan.get("monthly_revenue", 0)),
                monthly_recurring=float(scan.get("monthly_recurring", 0)),
                monthly_burn=float(scan.get("monthly_burn", 0)),
                revenue_growth_rate=float(scan.get("revenue_growth_rate", 0)),
                customer_retention_rate=float(scan.get("customer_retention_rate", 0.7)),
                net_margin=float(scan.get("net_margin", 0)),
                gross_margin=float(scan.get("gross_margin", 0.3)),
                asset_value=float(scan.get("asset_value", 0)),
                cash_position=float(scan.get("cash_position", 0)),
                years_operating=int(scan.get("years_operating", 1)),
                customer_count=int(scan.get("customer_count", 0)),
                has_ip=bool(scan.get("has_ip", False)),
                is_defensible=bool(scan.get("is_defensible", False)),
                has_network_effects=bool(scan.get("has_network_effects", False)),
                owner_committed=bool(scan.get("owner_committed", True)),
                market_size=float(scan.get("market_size", 0)),
                market_growth_rate=float(scan.get("market_growth_rate", 0)),
                market_share=float(scan.get("market_share", 0)),
                valuation=float(scan.get("valuation", 0)),
                top_customer_ratio=float(scan.get("top_customer_ratio", 0)),
                quick_wins=scan.get("quick_wins", [])
            )
            
            opportunities.append(opp.__dict__)
            self.discovered_opportunities[opp.id] = opp
        
        # Run complete hunt analysis
        hunt_results = self.hunt_system.hunt_and_analyze(opportunities)
        
        # Build comprehensive report
        report = {
            "hunt_timestamp": hunt_results["timestamp"],
            "scan_summary": {
                "total_scanned": hunt_results["opportunities_analyzed"],
                "solvables_found": hunt_results["profiles"],
                "efficiency": f"{(len(hunt_results['profiles']) / max(hunt_results['opportunities_analyzed'], 1) * 100):.1f}%"
            },
            
            "solvability_summary": {
                "by_discretion": dict(hunt_results["solvables_by_discretion"]),
                "evident": len(hunt_results["solvables_by_discretion"].get("evident", [])),
                "discreet_level_1": len(hunt_results["solvables_by_discretion"].get("disc_1", [])),
                "very_discreet": len(hunt_results["solvables_by_discretion"].get("disc_2", [])),
                "hidden": len(hunt_results["solvables_by_discretion"].get("hidden", [])),
                "secret": len(hunt_results["solvables_by_discretion"].get("secret", []))
            },
            
            "cash_potential": hunt_results["cash_potential"],
            
            "offers_generated": {
                "24h": hunt_results["offers_by_horizon"].get("24h", []),
                "48h": hunt_results["offers_by_horizon"].get("48h", []),
                "72h": hunt_results["offers_by_horizon"].get("72h", []),
                "6m": hunt_results["offers_by_horizon"].get("6m", []),
                "2y": hunt_results["offers_by_horizon"].get("2y", []),
                "premium": hunt_results["offers_by_horizon"].get("premium", [])
            },
            
            "strategies": self._generate_strategies(hunt_results),
            "recommended_actions": self._prioritize_actions(hunt_results)
        }
        
        # Update cash flow timeline
        self.cash_flow_timeline.update(hunt_results["cash_potential"])
        
        return report

    def _generate_strategies(self, hunt_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Génère des stratégies basées sur les opportunités découvertes."""
        
        strategies = []
        
        # Strategy 1: Quick Cash (24-72h)
        quick_cash_potential = hunt_results["cash_potential"]["72h"]
        if quick_cash_potential > 0:
            strategies.append({
                "name": "Quick Cash Acceleration",
                "horizon": "72h",
                "target_value": quick_cash_potential,
                "tactics": [
                    "Identify immediate cash needs in target businesses",
                    "Structure revenue-sharing agreements",
                    "Deploy working capital instantly",
                    "Document quick wins for rapid deployment"
                ]
            })
        
        # Strategy 2: Medium-Term Growth (6 months)
        medium_potential = hunt_results["cash_potential"]["6m"]
        if medium_potential > 0:
            strategies.append({
                "name": "Growth Acceleration Program",
                "horizon": "6m",
                "target_value": medium_potential,
                "tactics": [
                    "Fund team expansion in high-growth companies",
                    "Implement revenue acceleration playbooks",
                    "Support market expansion initiatives",
                    "Enable product development cycles"
                ]
            })
        
        # Strategy 3: Long-Term Value Creation (2 years)
        long_potential = hunt_results["cash_potential"]["2y"]
        if long_potential > 0:
            strategies.append({
                "name": "Strategic Category Dominance",
                "horizon": "2y",
                "target_value": long_potential,
                "tactics": [
                    "Acquire or invest in market leaders",
                    "Consolidate fragmented markets",
                    "Build network effects and defensibility",
                    "Establish category leadership position"
                ]
            })
        
        return strategies

    def _prioritize_actions(self, hunt_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Priorise les actions recommandées."""
        
        actions = []
        
        # Action 1: Obvious opportunities
        evident_count = len(hunt_results["solvables_by_discretion"].get("evident", []))
        if evident_count > 0:
            actions.append({
                "priority": 1,
                "action": "Engage obvious solvables immediately",
                "count": evident_count,
                "timeline": "Next 24 hours",
                "expected_value": hunt_results["cash_potential"]["24h"]
            })
        
        # Action 2: Discreet opportunities
        discreet_count = len(hunt_results["solvables_by_discretion"].get("disc_1", []))
        if discreet_count > 0:
            actions.append({
                "priority": 2,
                "action": "Research and approach discreet opportunities",
                "count": discreet_count,
                "timeline": "Next 48-72 hours",
                "expected_value": hunt_results["cash_potential"]["72h"]
            })
        
        # Action 3: Hidden opportunities
        hidden_count = len(hunt_results["solvables_by_discretion"].get("hidden", []))
        if hidden_count > 0:
            actions.append({
                "priority": 3,
                "action": "Deep research and network outreach for hidden gems",
                "count": hidden_count,
                "timeline": "Next 1-2 weeks",
                "expected_value": hunt_results["cash_potential"]["6m"]
            })
        
        # Action 4: Secret opportunities
        secret_count = len(hunt_results["solvables_by_discretion"].get("secret", []))
        if secret_count > 0:
            actions.append({
                "priority": 4,
                "action": "Activate premium network for secret deals",
                "count": secret_count,
                "timeline": "Ongoing",
                "expected_value": hunt_results["cash_potential"]["2y"]
            })
        
        return actions

    def get_market_summary(self, market: str) -> Dict[str, Any]:
        """Résumé d'un marché spécifique."""
        
        market_opps = [
            opp for opp in self.discovered_opportunities.values()
            if opp.market == market
        ]
        
        total_revenue = sum(o.annual_revenue for o in market_opps)
        avg_growth = sum(o.revenue_growth_rate for o in market_opps) / len(market_opps) if market_opps else 0
        
        return {
            "market": market,
            "opportunities_count": len(market_opps),
            "total_addressable": total_revenue,
            "avg_growth_rate": avg_growth,
            "cash_available": sum(o.cash_position for o in market_opps),
            "consolidated_quick_wins": sum(len(o.quick_wins) for o in market_opps)
        }

    def get_cash_flow_projection(self) -> Dict[str, Any]:
        """Projection complète des cash flows."""
        
        return {
            "projections": self.cash_flow_timeline,
            "total_potential_24h": self.cash_flow_timeline["24h"],
            "total_potential_72h": self.cash_flow_timeline["72h"],
            "total_potential_6m": self.cash_flow_timeline["6m"],
            "total_potential_2y": self.cash_flow_timeline["2y"],
            "cumulative_24m": sum([
                self.cash_flow_timeline["24h"],
                self.cash_flow_timeline["48h"],
                self.cash_flow_timeline["72h"],
                self.cash_flow_timeline["6m"]
            ])
        }


# ============================================================================
# PUBLIC API
# ============================================================================

def create_hunt_orchestration() -> HuntOrchestrationLayer:
    """Crée la couche d'orchestration de chasse."""
    return HuntOrchestrationLayer()
