"""
NAYA_HUNT_ADVANCED - SOPHISTICATED OPPORTUNITY HUNTING SYSTEM

Détection Intelligente de Solvables Réels
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Système de Chasse Multi-Niveaux:
1. SOLVABILITÉ RÉELLE: Détecte vrais solvables (vs illusions)
2. DISCRÉTION: Classification (Évident → Très Discret → Secret)
3. HORIZONS TEMPORELS: 24h, 48h, 72h, Moyen-Terme, Long-Terme
4. GÉNÉRATION OFFRES: Crée naturellement sans forcer
5. MULTI-MARCHÉS: Tous secteurs, géographies, verticals
6. PLANCHER PREMIUM: Qualité >= Premium absolu
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from enum import Enum
import hashlib
import json
from collections import defaultdict


# ============================================================================
# TIER 1: SOLVABILITÉ & DÉTECTION
# ============================================================================

class SolvabilityLevel(Enum):
    """Niveaux de solvabilité réelle."""
    EVIDENT = "evident"              # Clair, facile, visible
    DISCRETION_LEVEL_1 = "disc_1"   # Discret, attention requise
    DISCRETION_LEVEL_2 = "disc_2"   # Très discret, expertise requise
    HIDDEN = "hidden"                # Caché, découverte exceptionnelle
    SECRET = "secret"                # Ultra-secret, réseau requis


class SolvablityMarker(Enum):
    """Indicateurs de vraie solvabilité."""
    CASH_FLOW = "cash_flow"              # Flux de trésorerie réel
    RECURRING_REVENUE = "recurring_rev"   # Revenue récurrente
    ASSET_VALUE = "asset_value"          # Valeur d'actifs
    CUSTOMER_LOYALTY = "customer_loyalty" # Fidélité clients
    MARKET_POSITION = "market_position"   # Position de marché
    GROWTH_TRAJECTORY = "growth_traj"     # Trajectory de croissance
    OWNER_COMMITMENT = "owner_commit"     # Commitment du propriétaire
    INTELLECTUAL_PROPERTY = "ip"          # IP/Brevets/Secrets
    OPERATIONAL_LEVERAGE = "leverage"     # Levier opérationnel
    NETWORK_EFFECTS = "network"           # Effets réseau


@dataclass
class SolvabilityProfile:
    """Profil complet de solvabilité d'une opportunité."""
    opportunity_id: str
    name: str
    
    # Solvabilité
    solvability_level: SolvabilityLevel
    solvability_score: float  # 0-100
    confidence: float  # 0-1
    
    # Indicateurs clés
    markers: Dict[SolvablityMarker, float] = field(default_factory=dict)  # Each: 0-1
    
    # Marché & Horizon
    market: str  # Sector/Geography
    addressable_market_size: float
    growth_rate: float  # % annual
    
    # Cash & Valuation
    annual_revenue: float
    monthly_recurring: float
    cash_position: float
    valuation: float
    
    # Horizons de réalisation
    cash_24h_potential: float = 0.0
    cash_48h_potential: float = 0.0
    cash_72h_potential: float = 0.0
    medium_term_6m: float = 0.0   # 6 months potential
    long_term_2y: float = 0.0     # 2 years potential
    
    # Risques & Mitigation
    risk_score: float = 0.5  # 0-1
    risk_factors: List[str] = field(default_factory=list)
    mitigation_strategies: List[str] = field(default_factory=list)
    
    # Offre associée
    recommended_offer: Optional[Dict[str, Any]] = None
    
    # Métadonnées
    discovered_at: datetime = field(default_factory=datetime.utcnow)
    last_updated: datetime = field(default_factory=datetime.utcnow)


class SolvabilityDetector:
    """Détecteur sophistiqué de vraie solvabilité."""

    def __init__(self):
        self.profiles: Dict[str, SolvabilityProfile] = {}
        self.detection_history: List[Dict] = []
        self.marker_weights: Dict[SolvablityMarker, float] = self._init_weights()

    def _init_weights(self) -> Dict[SolvablityMarker, float]:
        """Initialise les poids des indicateurs de solvabilité."""
        return {
            SolvablityMarker.CASH_FLOW: 0.25,           # Plus important
            SolvablityMarker.RECURRING_REVENUE: 0.20,   # Très important
            SolvablityMarker.ASSET_VALUE: 0.15,
            SolvablityMarker.CUSTOMER_LOYALTY: 0.10,
            SolvablityMarker.MARKET_POSITION: 0.10,
            SolvablityMarker.GROWTH_TRAJECTORY: 0.08,
            SolvablityMarker.OWNER_COMMITMENT: 0.07,
            SolvablityMarker.INTELLECTUAL_PROPERTY: 0.03,
            SolvablityMarker.OPERATIONAL_LEVERAGE: 0.02,
            SolvablityMarker.NETWORK_EFFECTS: 0.00  # Nice to have
        }

    def analyze_solvability(self, opportunity: Dict[str, Any]) -> SolvabilityProfile:
        """Analyse complète de solvabilité réelle."""
        
        opp_id = opportunity.get("id", f"OPP-{int(datetime.utcnow().timestamp() * 1000)}")
        
        # ========== PHASE 1: EXTRACT SIGNALS ==========
        signals = self._extract_solvability_signals(opportunity)
        
        # ========== PHASE 2: CALCULATE MARKERS ==========
        markers = self._calculate_markers(signals, opportunity)
        
        # ========== PHASE 3: DETERMINE LEVEL ==========
        solvability_score = sum(m * self.marker_weights.get(marker, 0)
                               for marker, m in markers.items()) * 100
        
        level = self._classify_level(solvability_score, signals)
        
        # ========== PHASE 4: CASH POTENTIALS ==========
        cash_potentials = self._calculate_cash_potentials(opportunity, signals)
        
        # ========== PHASE 5: RISK ASSESSMENT ==========
        risk_score, risk_factors, mitigations = self._assess_risks(opportunity, signals)
        
        # ========== CREATE PROFILE ==========
        profile = SolvabilityProfile(
            opportunity_id=opp_id,
            name=opportunity.get("name", "Unknown"),
            solvability_level=level,
            solvability_score=solvability_score,
            confidence=min(sum(markers.values()) / len(markers) if markers else 0.5, 0.99),
            markers=markers,
            market=opportunity.get("market", "unknown"),
            addressable_market_size=opportunity.get("market_size", 0),
            growth_rate=opportunity.get("growth_rate", 0),
            annual_revenue=opportunity.get("annual_revenue", 0),
            monthly_recurring=opportunity.get("monthly_recurring", 0),
            cash_position=opportunity.get("cash_position", 0),
            valuation=opportunity.get("valuation", 0),
            cash_24h_potential=cash_potentials["24h"],
            cash_48h_potential=cash_potentials["48h"],
            cash_72h_potential=cash_potentials["72h"],
            medium_term_6m=cash_potentials["6m"],
            long_term_2y=cash_potentials["2y"],
            risk_score=risk_score,
            risk_factors=risk_factors,
            mitigation_strategies=mitigations
        )
        
        self.profiles[opp_id] = profile
        return profile

    def _extract_solvability_signals(self, opp: Dict) -> Dict[str, Any]:
        """Extrait les signaux de solvabilité d'une opportunité."""
        
        signals = {
            "has_history": bool(opp.get("years_operating", 0) > 0),
            "has_revenue": float(opp.get("annual_revenue", 0)) > 0,
            "has_recurring": float(opp.get("monthly_recurring", 0)) > 0,
            "has_customers": int(opp.get("customer_count", 0)) > 0,
            "has_assets": float(opp.get("asset_value", 0)) > 0,
            "has_ip": bool(opp.get("has_ip", False)),
            "market_growing": float(opp.get("market_growth_rate", 0)) > 0,
            "owner_committed": bool(opp.get("owner_committed", False)),
            "profitable": float(opp.get("net_margin", 0)) > 0,
            "growing": float(opp.get("revenue_growth_rate", 0)) > 0,
            "sticky_customers": float(opp.get("customer_retention_rate", 0)) > 0.7,
            "defensible": bool(opp.get("is_defensible", False)),
            "network_effects": bool(opp.get("has_network_effects", False))
        }
        
        return signals

    def _calculate_markers(self, signals: Dict, opp: Dict) -> Dict[SolvablityMarker, float]:
        """Calcule les scores pour chaque marqueur de solvabilité."""
        
        markers = {}
        
        # 1. Cash Flow
        if signals["has_history"] and signals["has_revenue"]:
            monthly_burn = opp.get("monthly_burn", 0)
            monthly_rev = opp.get("monthly_revenue", 0)
            if monthly_rev > 0:
                cf_ratio = monthly_rev / (monthly_burn + 1)
                markers[SolvablityMarker.CASH_FLOW] = min(cf_ratio / 5, 1.0)
            else:
                markers[SolvablityMarker.CASH_FLOW] = 0.3
        else:
            markers[SolvablityMarker.CASH_FLOW] = 0.1
        
        # 2. Recurring Revenue
        if signals["has_recurring"]:
            recurring_ratio = opp.get("monthly_recurring", 0) / max(opp.get("monthly_revenue", 1), 1)
            markers[SolvablityMarker.RECURRING_REVENUE] = min(recurring_ratio, 1.0)
        else:
            markers[SolvablityMarker.RECURRING_REVENUE] = 0.2
        
        # 3. Asset Value
        asset_to_revenue = opp.get("asset_value", 0) / max(opp.get("annual_revenue", 1), 1)
        markers[SolvablityMarker.ASSET_VALUE] = min(asset_to_revenue / 5, 1.0) if asset_to_revenue > 0 else 0.3
        
        # 4. Customer Loyalty
        retention = opp.get("customer_retention_rate", 0.5)
        markers[SolvablityMarker.CUSTOMER_LOYALTY] = min(retention, 1.0)
        
        # 5. Market Position
        market_share = opp.get("market_share", 0)
        markers[SolvablityMarker.MARKET_POSITION] = min(market_share * 100, 1.0)
        
        # 6. Growth Trajectory
        growth = opp.get("revenue_growth_rate", 0)
        markers[SolvablityMarker.GROWTH_TRAJECTORY] = min(growth / 2, 1.0)  # Normalize 200% = 1.0
        
        # 7. Owner Commitment
        markers[SolvablityMarker.OWNER_COMMITMENT] = 1.0 if signals["owner_committed"] else 0.3
        
        # 8. IP
        markers[SolvablityMarker.INTELLECTUAL_PROPERTY] = 1.0 if signals["has_ip"] else 0.1
        
        # 9. Operational Leverage
        gross_margin = opp.get("gross_margin", 0.3)
        markers[SolvablityMarker.OPERATIONAL_LEVERAGE] = min(gross_margin, 1.0)
        
        # 10. Network Effects
        markers[SolvablityMarker.NETWORK_EFFECTS] = 1.0 if signals["network_effects"] else 0.0
        
        return markers

    def _classify_level(self, score: float, signals: Dict) -> SolvabilityLevel:
        """Classifie le niveau de discrétion."""
        
        # Plus de signaux positifs = plus évident/visible
        positive_signals = sum(1 for v in signals.values() if v)
        
        if score >= 85 and positive_signals >= 10:
            return SolvabilityLevel.EVIDENT
        elif score >= 70 and positive_signals >= 8:
            return SolvabilityLevel.DISCRETION_LEVEL_1
        elif score >= 55 and positive_signals >= 6:
            return SolvabilityLevel.DISCRETION_LEVEL_2
        elif score >= 40 and positive_signals >= 4:
            return SolvabilityLevel.HIDDEN
        else:
            return SolvabilityLevel.SECRET

    def _calculate_cash_potentials(self, opp: Dict, signals: Dict) -> Dict[str, float]:
        """Calcule potentiels de cash à différents horizons."""
        
        monthly_rev = opp.get("monthly_revenue", 0)
        monthly_recurring = opp.get("monthly_recurring", 0)
        cash_position = opp.get("cash_position", 0)
        
        # Potentiels de réalisation rapide
        quick_wins = opp.get("quick_wins", [])
        
        potentials = {
            "24h": sum(w.get("value", 0) for w in quick_wins if w.get("time_to_value", 999) <= 1) + cash_position * 0.05,
            "48h": monthly_rev * 0.15 + cash_position * 0.10,
            "72h": monthly_rev * 0.20 + cash_position * 0.12,
            "6m": monthly_recurring * 6 + monthly_rev * 1.5,
            "2y": monthly_recurring * 24 + monthly_rev * 6 + opp.get("valuation", 0) * 0.3
        }
        
        return potentials

    def _assess_risks(self, opp: Dict, signals: Dict) -> Tuple[float, List[str], List[str]]:
        """Évalue les risques et mitigation."""
        
        risk_factors = []
        mitigations = []
        
        # Risk 1: History
        if opp.get("years_operating", 0) < 2:
            risk_factors.append("Early stage (< 2 years)")
            mitigations.append("Reduce initial investment, milestone-based")
        
        # Risk 2: Cash flow
        if opp.get("monthly_revenue", 0) < opp.get("monthly_burn", 0):
            risk_factors.append("Burn rate > revenue")
            mitigations.append("Provide revenue acceleration resources")
        
        # Risk 3: Dependency
        if opp.get("top_customer_ratio", 0) > 0.3:
            risk_factors.append("Customer concentration risk")
            mitigations.append("Diversify customer base")
        
        # Risk 4: Market
        if opp.get("market_growth_rate", 0) < -0.05:
            risk_factors.append("Declining market")
            mitigations.append("Look for niche positioning")
        
        # Risk 5: Execution
        if not signals.get("owner_committed", False):
            risk_factors.append("Owner engagement uncertain")
            mitigations.append("Align incentives, clear KPIs")
        
        # Calculate risk score
        risk_score = len(risk_factors) * 0.15  # 15% per factor, capped at ~100%
        risk_score = min(risk_score, 0.95)
        
        return risk_score, risk_factors, mitigations


# ============================================================================
# TIER 2: GÉNÉRATEUR D'OFFRES NATURELLES
# ============================================================================

class OfferTemplate(Enum):
    """Templates d'offres naturelles."""
    REVENUE_ACCELERATION = "revenue_accel"      # Croissance rapide
    CASH_INJECTION = "cash_inject"              # Capital rapide
    STRATEGIC_PARTNERSHIP = "partnership"       # Partenariat
    ACQUISITION_OFFER = "acquisition"           # Acquisition complète
    REVENUE_SHARE = "revenue_share"             # Revenue sharing
    GROWTH_INVESTMENT = "growth_invest"         # Investment + support
    ASSET_PURCHASE = "asset_purchase"           # Acheter les actifs
    OPERATIONAL_SUPPORT = "operational"        # Support opérationnel


@dataclass
class BusinessOffer:
    """Offre commerciale structurée."""
    offer_id: str
    opportunity_id: str
    template: OfferTemplate
    
    # Valeur
    capital_offered: float
    revenue_share: float = 0.0   # % de revenue si applicable
    equity_offered: float = 0.0  # % si applicable
    
    # Timeline
    horizon: str  # "24h", "48h", "72h", "6m", "2y"
    time_to_cash: int  # days
    
    # Conditions
    key_conditions: List[str] = field(default_factory=list)
    milestones: List[Dict[str, Any]] = field(default_factory=list)
    
    # Justification (pourquoi c'est naturel)
    rationale: str = ""
    expected_returns: Dict[str, float] = field(default_factory=dict)  # stage -> return
    
    # Status
    created_at: datetime = field(default_factory=datetime.utcnow)
    attractiveness_score: float = 0.8  # 0-1


class NaturalOfferGenerator:
    """Génère des offres commerciales naturelles et séduisantes."""

    def __init__(self):
        self.generated_offers: List[BusinessOffer] = []
        self.templates: Dict[OfferTemplate, Dict] = self._init_templates()

    def _init_templates(self) -> Dict[OfferTemplate, Dict]:
        """Initialise les templates d'offres."""
        
        return {
            OfferTemplate.REVENUE_ACCELERATION: {
                "description": "Capital pour accélération revenue",
                "typical_amount": {"low": 10000, "high": 100000},
                "typical_sharing": 0.20,  # 20% de croissance
                "horizon": "6m",
                "natural_triggers": ["stalled_growth", "market_opportunity", "talent_shortage"]
            },
            OfferTemplate.CASH_INJECTION: {
                "description": "Cash rapide pour besoins urgents",
                "typical_amount": {"low": 5000, "high": 50000},
                "typical_sharing": 0.15,  # 15% revenue share
                "horizon": "24h-48h",
                "natural_triggers": ["payroll", "supplier", "tax"]
            },
            OfferTemplate.GROWTH_INVESTMENT: {
                "description": "Investment capital + support stratégique",
                "typical_amount": {"low": 50000, "high": 500000},
                "typical_equity": 0.10,  # 10% equity
                "horizon": "2y",
                "natural_triggers": ["scaling_ready", "team_expansion", "market_expansion"]
            },
            OfferTemplate.ACQUISITION_OFFER: {
                "description": "Acquisition complète à valuation attractive",
                "typical_multiple": 4,  # 4x revenue
                "horizon": "6m",
                "natural_triggers": ["founder_exit", "market_consolidation"]
            },
            OfferTemplate.REVENUE_SHARE: {
                "description": "Revenue sharing - croissance partagée",
                "typical_sharing": 0.25,  # 25% de revenue growth
                "horizon": "6-24m",
                "natural_triggers": ["mutual_growth", "profit_sharing"]
            },
            OfferTemplate.ASSET_PURCHASE: {
                "description": "Achat sélectif d'actifs clés",
                "typical_amount": {"low": 20000, "high": 200000},
                "horizon": "3m",
                "natural_triggers": ["technology", "customer_base", "brand"]
            }
        }

    def generate_offers(self, profile: SolvabilityProfile) -> List[BusinessOffer]:
        """Génère un ensemble d'offres naturelles pour une opportunité."""
        
        offers = []
        
        # ========== OFFRE 1: RAPIDE (24-72h) ==========
        if profile.cash_24h_potential > 0:
            offer_24h = self._create_quick_cash_offer(profile, "24h")
            if offer_24h:
                offers.append(offer_24h)
        
        if profile.cash_48h_potential > profile.cash_24h_potential:
            offer_48h = self._create_quick_cash_offer(profile, "48h")
            if offer_48h:
                offers.append(offer_48h)
        
        if profile.cash_72h_potential > profile.cash_48h_potential:
            offer_72h = self._create_quick_cash_offer(profile, "72h")
            if offer_72h:
                offers.append(offer_72h)
        
        # ========== OFFRE 2: MOYEN TERME (6 mois) ==========
        if profile.medium_term_6m > 0:
            offer_medium = self._create_medium_term_offer(profile)
            if offer_medium:
                offers.append(offer_medium)
        
        # ========== OFFRE 3: LONG TERME (2 ans) ==========
        if profile.long_term_2y > 0:
            offer_long = self._create_long_term_offer(profile)
            if offer_long:
                offers.append(offer_long)
        
        # ========== OFFRE 4: STRUCTURÉE (si applicable) ==========
        if profile.solvability_score >= 60:
            offer_structured = self._create_structured_offer(profile)
            if offer_structured:
                offers.append(offer_structured)
        
        self.generated_offers.extend(offers)
        return offers

    def _create_quick_cash_offer(self, profile: SolvabilityProfile, horizon: str) -> Optional[BusinessOffer]:
        """Crée une offre de cash rapide."""
        
        if horizon == "24h":
            amount = min(profile.cash_24h_potential, 50000)
            time_to_cash = 1
        elif horizon == "48h":
            amount = min(profile.cash_48h_potential, 75000)
            time_to_cash = 2
        else:  # 72h
            amount = min(profile.cash_72h_potential, 100000)
            time_to_cash = 3
        
        if amount < 5000:
            return None
        
        offer = BusinessOffer(
            offer_id=f"OFF-QC-{horizon}-{int(datetime.utcnow().timestamp() * 1000)}",
            opportunity_id=profile.opportunity_id,
            template=OfferTemplate.CASH_INJECTION,
            capital_offered=amount,
            revenue_share=0.15,  # 15% revenue share
            horizon=horizon,
            time_to_cash=time_to_cash,
            key_conditions=[
                "Clear revenue path",
                "Weekly reporting",
                "Repayment schedule agreed"
            ],
            rationale=f"Quick capital injection for immediate needs. {horizon} deployment. Revenue sharing ensures alignment.",
            expected_returns={
                "3m": amount * 1.15,
                "6m": amount * 1.35,
                "12m": amount * 1.60
            },
            attractiveness_score=0.85
        )
        
        return offer

    def _create_medium_term_offer(self, profile: SolvabilityProfile) -> Optional[BusinessOffer]:
        """Crée une offre moyen terme (6 mois)."""
        
        amount = min(profile.medium_term_6m * 0.3, 250000)  # 30% of 6m potential
        
        if amount < 20000:
            return None
        
        offer = BusinessOffer(
            offer_id=f"OFF-MT-6m-{int(datetime.utcnow().timestamp() * 1000)}",
            opportunity_id=profile.opportunity_id,
            template=OfferTemplate.REVENUE_ACCELERATION,
            capital_offered=amount,
            revenue_share=0.20,  # 20% revenue share on NEW revenue
            horizon="6m",
            time_to_cash=180,
            key_conditions=[
                "Revenue growth targets",
                "Monthly milestone reviews",
                "Team expansion plan",
                "Market expansion strategy"
            ],
            milestones=[
                {"day": 30, "target": "Onboard 2 key hires", "value": 0},
                {"day": 90, "target": "+30% revenue", "value": amount * 0.15},
                {"day": 135, "target": "+60% revenue", "value": amount * 0.40},
                {"day": 180, "target": "+100% revenue", "value": amount * 1.0}
            ],
            rationale="Growth capital for revenue acceleration. 6-month focused expansion with revenue sharing.",
            expected_returns={
                "6m": amount * 1.40,
                "12m": amount * 2.20,
                "24m": amount * 4.50
            },
            attractiveness_score=0.80
        )
        
        return offer

    def _create_long_term_offer(self, profile: SolvabilityProfile) -> Optional[BusinessOffer]:
        """Crée une offre long terme (2 ans)."""
        
        amount = min(profile.long_term_2y * 0.25, 500000)  # 25% of 2y potential
        
        if amount < 50000:
            return None
        
        equity = 0.10 if profile.solvability_score >= 75 else 0.15
        
        offer = BusinessOffer(
            offer_id=f"OFF-LT-2y-{int(datetime.utcnow().timestamp() * 1000)}",
            opportunity_id=profile.opportunity_id,
            template=OfferTemplate.GROWTH_INVESTMENT,
            capital_offered=amount,
            equity_offered=equity,
            horizon="2y",
            time_to_cash=730,
            key_conditions=[
                "Board seat or observer rights",
                "Quarterly business reviews",
                "Annual strategic refresh",
                "Exit negotiation window at 24m"
            ],
            milestones=[
                {"month": 6, "target": "Category leadership in segment", "value": 0},
                {"month": 12, "target": "5x revenue growth", "value": 0},
                {"month": 18, "target": "Profitable operations", "value": 0},
                {"month": 24, "target": "Exit or refinance", "value": amount * 10}
            ],
            rationale="Strategic growth investment. Multi-horizon expansion with equity participation.",
            expected_returns={
                "12m": amount * 2.5,
                "24m": amount * 10.0,
                "36m": amount * 25.0
            },
            attractiveness_score=0.75
        )
        
        return offer

    def _create_structured_offer(self, profile: SolvabilityProfile) -> Optional[BusinessOffer]:
        """Crée une offre structurée plus sophistiquée."""
        
        # Choix du template basé sur profil
        if profile.solvability_score >= 80 and profile.long_term_2y > profile.medium_term_6m * 3:
            template = OfferTemplate.ACQUISITION_OFFER
            amount = min(profile.valuation * 4, 1000000)  # 4x revenue
            
            offer = BusinessOffer(
                offer_id=f"OFF-ACQ-{int(datetime.utcnow().timestamp() * 1000)}",
                opportunity_id=profile.opportunity_id,
                template=template,
                capital_offered=amount,
                horizon="6m",
                time_to_cash=180,
                key_conditions=[
                    "Due diligence acceptance",
                    "Key person agreements",
                    "Customer retention commitments",
                    "Earn-out potential"
                ],
                rationale="Full acquisition offer at attractive valuation. Accelerated exit for founder.",
                expected_returns={"exit": amount * 1.5},
                attractiveness_score=0.88
            )
            
            return offer
        
        return None


# ============================================================================
# TIER 3: ORCHESTRATION HUNT AVANCÉ
# ============================================================================

class AdvancedHuntOrchestrator:
    """Orchestre l'ensemble du système de chasse avancé."""

    def __init__(self):
        self.solvability_detector = SolvabilityDetector()
        self.offer_generator = NaturalOfferGenerator()
        
        # Statistiques
        self.opportunities_analyzed = 0
        self.solvables_found = defaultdict(int)  # By level
        self.offers_generated = 0

    def hunt_and_analyze(self, opportunities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Lance la chasse complète: détection + génération d'offres."""
        
        results = {
            "timestamp": datetime.utcnow().isoformat(),
            "opportunities_analyzed": len(opportunities),
            "profiles": [],
            "offers_by_horizon": defaultdict(list),
            "solvables_by_discretion": defaultdict(list),
            "cash_potential": {
                "24h": 0,
                "48h": 0,
                "72h": 0,
                "6m": 0,
                "2y": 0
            }
        }
        
        for opp in opportunities:
            try:
                # 1. Analyze solvability
                profile = self.solvability_detector.analyze_solvability(opp)
                
                # 2. Generate offers
                offers = self.offer_generator.generate_offers(profile)
                
                # 3. Accumulate results
                results["profiles"].append({
                    "id": profile.opportunity_id,
                    "name": profile.name,
                    "solvability_level": profile.solvability_level.value,
                    "solvability_score": profile.solvability_score,
                    "confidence": profile.confidence,
                    "cash_24h": profile.cash_24h_potential,
                    "cash_48h": profile.cash_48h_potential,
                    "cash_72h": profile.cash_72h_potential,
                    "medium_6m": profile.medium_term_6m,
                    "long_2y": profile.long_term_2y,
                    "risk_score": profile.risk_score
                })
                
                # Group offers by horizon
                for offer in offers:
                    results["offers_by_horizon"][offer.horizon].append({
                        "id": offer.offer_id,
                        "template": offer.template.value,
                        "capital": offer.capital_offered,
                        "revenue_share": offer.revenue_share,
                        "equity": offer.equity_offered,
                        "attractiveness": offer.attractiveness_score
                    })
                
                # Track solvables by discretion
                results["solvables_by_discretion"][profile.solvability_level.value].append(
                    profile.opportunity_id
                )
                
                # Accumulate cash potential
                results["cash_potential"]["24h"] += max(profile.cash_24h_potential, 0)
                results["cash_potential"]["48h"] += max(profile.cash_48h_potential, 0)
                results["cash_potential"]["72h"] += max(profile.cash_72h_potential, 0)
                results["cash_potential"]["6m"] += max(profile.medium_term_6m, 0)
                results["cash_potential"]["2y"] += max(profile.long_term_2y, 0)
                
                self.opportunities_analyzed += 1
                self.solvables_found[profile.solvability_level.value] += 1
                self.offers_generated += len(offers)
                
            except Exception as e:
                print(f"Error analyzing {opp.get('name', 'Unknown')}: {str(e)}")
                continue
        
        return results

    def get_hunt_summary(self) -> Dict[str, Any]:
        """Retourne un résumé de la chasse."""
        
        total_solvables = sum(self.solvables_found.values())
        
        return {
            "total_opportunities_analyzed": self.opportunities_analyzed,
            "total_solvables_found": total_solvables,
            "breakdown": dict(self.solvables_found),
            "total_offers_generated": self.offers_generated,
            "discovery_efficiency": (total_solvables / max(self.opportunities_analyzed, 1)) * 100
        }


# ============================================================================
# PUBLIC API
# ============================================================================

def create_advanced_hunt_system() -> AdvancedHuntOrchestrator:
    """Crée le système complet de chasse avancée."""
    return AdvancedHuntOrchestrator()
