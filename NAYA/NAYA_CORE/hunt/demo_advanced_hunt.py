"""
DEMO - ADVANCED HUNTING SYSTEM v4.1

Démonstration complète du système de chasse sophistiqué:
- Détection de solvables réels
- Classification par discrétion
- Génération d'offres multi-horizons
- Projection de cash flows
"""

from NAYA_CORE import hunt_opportunities, get_market_summary, get_cash_flow_projection


# ============================================================================
# SAMPLE MARKET DATA - REPRESENTATIVE OPPORTUNITIES
# ============================================================================

SAMPLE_MARKET_OPPORTUNITIES = [
    # OBVIOUS SOLVABLES (Evident)
    {
        "id": "OPP-001",
        "name": "Tech Saas Company - Strong Growth",
        "market": "SaaS",
        "annual_revenue": 500000,
        "monthly_revenue": 41667,
        "monthly_recurring": 40000,
        "monthly_burn": 35000,
        "revenue_growth_rate": 0.25,  # 25% YoY
        "customer_retention_rate": 0.92,
        "net_margin": 0.15,
        "gross_margin": 0.80,
        "asset_value": 100000,
        "cash_position": 80000,
        "years_operating": 4,
        "customer_count": 120,
        "has_ip": True,
        "is_defensible": True,
        "has_network_effects": False,
        "owner_committed": True,
        "market_size": 50000000,
        "market_growth_rate": 0.30,
        "market_share": 0.01,
        "valuation": 2000000,
        "top_customer_ratio": 0.05,
        "quick_wins": [
            {"value": 5000, "time_to_value": 1, "description": "Unpaid invoices"},
            {"value": 8000, "time_to_value": 2, "description": "Early payment discounts"}
        ]
    },
    
    # DISCREET SOLVABLES (Discretion Level 1)
    {
        "id": "OPP-002",
        "name": "Agency Services - Stable Cash Flow",
        "market": "Services",
        "annual_revenue": 300000,
        "monthly_revenue": 25000,
        "monthly_recurring": 15000,
        "monthly_burn": 20000,
        "revenue_growth_rate": 0.10,
        "customer_retention_rate": 0.85,
        "net_margin": 0.08,
        "gross_margin": 0.45,
        "asset_value": 50000,
        "cash_position": 45000,
        "years_operating": 6,
        "customer_count": 25,
        "has_ip": False,
        "is_defensible": True,
        "has_network_effects": False,
        "owner_committed": True,
        "market_size": 100000000,
        "market_growth_rate": 0.08,
        "market_share": 0.0003,
        "valuation": 900000,
        "top_customer_ratio": 0.12,
        "quick_wins": [
            {"value": 3000, "time_to_value": 2, "description": "Working capital"}
        ]
    },
    
    # HIDDEN SOLVABLES (Discretion Level 2)
    {
        "id": "OPP-003",
        "name": "E-Commerce Store - Niche Market",
        "market": "Retail",
        "annual_revenue": 150000,
        "monthly_revenue": 12500,
        "monthly_recurring": 2000,
        "monthly_burn": 8000,
        "revenue_growth_rate": 0.15,
        "customer_retention_rate": 0.70,
        "net_margin": 0.02,
        "gross_margin": 0.35,
        "asset_value": 200000,  # Inventory + equipment
        "cash_position": 20000,
        "years_operating": 3,
        "customer_count": 5000,
        "has_ip": False,
        "is_defensible": False,
        "has_network_effects": False,
        "owner_committed": True,
        "market_size": 200000000,
        "market_growth_rate": 0.20,
        "market_share": 0.000075,
        "valuation": 450000,
        "top_customer_ratio": 0.08,
        "quick_wins": [
            {"value": 2000, "time_to_value": 1, "description": "Clearance inventory"}
        ]
    },
    
    # VERY HIDDEN (Discretion Level 2+)
    {
        "id": "OPP-004",
        "name": "Consulting - High Expertise",
        "market": "Consulting",
        "annual_revenue": 200000,
        "monthly_revenue": 16667,
        "monthly_recurring": 8000,
        "monthly_burn": 10000,
        "revenue_growth_rate": 0.05,  # Low growth
        "customer_retention_rate": 0.95,
        "net_margin": 0.30,
        "gross_margin": 0.85,
        "asset_value": 0,
        "cash_position": 100000,
        "years_operating": 8,
        "customer_count": 8,
        "has_ip": True,
        "is_defensible": True,
        "has_network_effects": False,
        "owner_committed": True,
        "market_size": 500000000,
        "market_growth_rate": 0.05,
        "market_share": 0.00004,
        "valuation": 600000,
        "top_customer_ratio": 0.25,
        "quick_wins": []
    },
    
    # SECRET - EXCEPTIONAL
    {
        "id": "OPP-005",
        "name": "Platform - Network Effects",
        "market": "Marketplace",
        "annual_revenue": 1000000,
        "monthly_revenue": 83333,
        "monthly_recurring": 80000,
        "monthly_burn": 60000,
        "revenue_growth_rate": 0.50,
        "customer_retention_rate": 0.98,
        "net_margin": 0.20,
        "gross_margin": 0.95,
        "asset_value": 500000,
        "cash_position": 200000,
        "years_operating": 2,
        "customer_count": 50000,
        "has_ip": True,
        "is_defensible": True,
        "has_network_effects": True,
        "owner_committed": True,
        "market_size": 5000000000,
        "market_growth_rate": 0.100,
        "market_share": 0.00002,
        "valuation": 10000000,
        "top_customer_ratio": 0.02,
        "quick_wins": [
            {"value": 50000, "time_to_value": 2, "description": "Enterprise partnerships"},
            {"value": 30000, "time_to_value": 3, "description": "API licensing"}
        ]
    }
]


# ============================================================================
# DEMO FUNCTIONS
# ============================================================================

def demo_1_basic_hunt():
    """Demo 1: Basic hunting across all opportunities."""
    
    print("\n" + "=" * 100)
    print("DEMO 1: ADVANCED HUNT - DISCOVER REAL SOLVABLES")
    print("=" * 100)
    
    print(f"\n🔍 Scanning {len(SAMPLE_MARKET_OPPORTUNITIES)} market opportunities...")
    
    # Run the hunt
    hunt_results = hunt_opportunities(SAMPLE_MARKET_OPPORTUNITIES)
    
    print(f"\n✅ Hunt Complete!")
    print(f"   Total Opportunities: {hunt_results['scan_summary']['total_scanned']}")
    print(f"   Solvables Found: {len(hunt_results['scan_summary']['solvables_found'])}")
    print(f"   Discovery Efficiency: {hunt_results['scan_summary']['efficiency']}")
    
    # Show breakdown by discretion
    print(f"\n📊 SOLVABILITY BREAKDOWN:")
    breakdown = hunt_results['solvability_summary']
    print(f"   Evident (obvious): {breakdown['evident']}")
    print(f"   Discreet (subtle): {breakdown['discreet_level_1']}")
    print(f"   Very Discreet: {breakdown['very_discreet']}")
    print(f"   Hidden: {breakdown['hidden']}")
    print(f"   Secret (exceptional): {breakdown['secret']}")


def demo_2_cash_potentials():
    """Demo 2: Cash flow potential across time horizons."""
    
    print("\n" + "=" * 100)
    print("DEMO 2: CASH FLOW POTENTIAL ANALYSIS")
    print("=" * 100)
    
    hunt_results = hunt_opportunities(SAMPLE_MARKET_OPPORTUNITIES)
    cash = hunt_results['cash_potential']
    
    print(f"\n💰 CASH POTENTIAL BY HORIZON:")
    print(f"   24 Hours: ${cash['24h']:,.0f}")
    print(f"   48 Hours: ${cash['48h']:,.0f}")
    print(f"   72 Hours: ${cash['72h']:,.0f}")
    print(f"   6 Months: ${cash['6m']:,.0f}")
    print(f"   2 Years: ${cash['2y']:,.0f}")
    
    total_24m = cash['24h'] + cash['48h'] + cash['72h'] + cash['6m']
    print(f"\n   TOTAL (24 months): ${total_24m:,.0f}")


def demo_3_offers_by_horizon():
    """Demo 3: Generated offers by time horizon."""
    
    print("\n" + "=" * 100)
    print("DEMO 3: GENERATED OFFERS BY HORIZON")
    print("=" * 100)
    
    hunt_results = hunt_opportunities(SAMPLE_MARKET_OPPORTUNITIES)
    offers = hunt_results['offers_generated']
    
    print(f"\n📋 OFFERS GENERATED:")
    
    for horizon in ['24h', '48h', '72h', '6m', '2y']:
        horizon_offers = offers.get(horizon, [])
        if horizon_offers:
            print(f"\n   {horizon.upper()}:")
            for offer in horizon_offers[:3]:  # Show top 3
                print(f"      - {offer['template']}: ${offer['capital']:,.0f}")
                if offer['revenue_share'] > 0:
                    print(f"        Revenue Share: {offer['revenue_share']*100:.0f}%")
                if offer['equity'] > 0:
                    print(f"        Equity: {offer['equity']*100:.0f}%")


def demo_4_market_focus():
    """Demo 4: Focus on specific market."""
    
    print("\n" + "=" * 100)
    print("DEMO 4: FOCUSED MARKET ANALYSIS")
    print("=" * 100)
    
    hunt_opportunities(SAMPLE_MARKET_OPPORTUNITIES)
    
    # Analyze SaaS market
    saas_summary = get_market_summary("SaaS")
    
    print(f"\n📍 SAAS MARKET ANALYSIS:")
    print(f"   Opportunities: {saas_summary['opportunities_count']}")
    print(f"   Total Addressable: ${saas_summary['total_addressable']:,.0f}")
    print(f"   Growth Rate: {saas_summary['avg_growth_rate']*100:.1f}%")
    print(f"   Available Cash: ${saas_summary['cash_available']:,.0f}")
    print(f"   Quick Wins: {saas_summary['consolidated_quick_wins']}")


def demo_5_strategies():
    """Demo 5: Recommended strategies."""
    
    print("\n" + "=" * 100)
    print("DEMO 5: INTELLIGENT STRATEGIES")
    print("=" * 100)
    
    hunt_results = hunt_opportunities(SAMPLE_MARKET_OPPORTUNITIES)
    strategies = hunt_results['strategies']
    
    print(f"\n🎯 RECOMMENDED STRATEGIES ({len(strategies)}):")
    
    for i, strategy in enumerate(strategies, 1):
        print(f"\n   STRATEGY {i}: {strategy['name']}")
        print(f"   Horizon: {strategy['horizon']}")
        print(f"   Target Value: ${strategy['target_value']:,.0f}")
        print(f"   Tactics:")
        for tactic in strategy['tactics']:
            print(f"      • {tactic}")


def demo_6_action_plan():
    """Demo 6: Prioritized action plan."""
    
    print("\n" + "=" * 100)
    print("DEMO 6: ACTIONABLE PRIORITIES")
    print("=" * 100)
    
    hunt_results = hunt_opportunities(SAMPLE_MARKET_OPPORTUNITIES)
    actions = hunt_results['recommended_actions']
    
    print(f"\n⚡ PRIORITY ACTIONS (in order):")
    
    for action in actions:
        print(f"\n   PRIORITY {action['priority']}: {action['action']}")
        print(f"   Count: {action['count']} opportunities")
        print(f"   Timeline: {action['timeline']}")
        print(f"   Expected Value: ${action['expected_value']:,.0f}")


def demo_7_detailed_profiles():
    """Demo 7: Detailed solvability profiles."""
    
    print("\n" + "=" * 100)
    print("DEMO 7: DETAILED SOLVABILITY PROFILES")
    print("=" * 100)
    
    hunt_results = hunt_opportunities(SAMPLE_MARKET_OPPORTUNITIES)
    profiles = hunt_results['scan_summary']['solvables_found']
    
    print(f"\n📋 DISCOVERED SOLVABLES ({len(profiles)}):")
    
    for profile in profiles[:3]:  # Show top 3
        print(f"\n   {profile['name']}")
        print(f"   ID: {profile['id']}")
        print(f"   Level: {profile['solvability_level']}")
        print(f"   Score: {profile['solvability_score']:.1f}/100")
        print(f"   Confidence: {profile['confidence']:.1%}")
        print(f"   Risk: {profile['risk_score']:.1%}")


def main():
    """Run all demonstrations."""
    
    print("\n")
    print("╔" + "=" * 98 + "╗")
    print("║" + " " * 98 + "║")
    print("║" + "NAYA_CORE - ADVANCED HUNTING SYSTEM v4.1".center(98) + "║")
    print("║" + "Sophisticated Solvability Detection & Offer Generation".center(98) + "║")
    print("║" + " " * 98 + "║")
    print("╚" + "=" * 98 + "╝")
    
    # Run demonstrations
    demo_1_basic_hunt()
    demo_2_cash_potentials()
    demo_3_offers_by_horizon()
    demo_4_market_focus()
    demo_5_strategies()
    demo_6_action_plan()
    demo_7_detailed_profiles()
    
    # Final summary
    print("\n" + "=" * 100)
    print("SYSTEM CAPABILITIES SUMMARY")
    print("=" * 100)
    
    hunt_results = hunt_opportunities(SAMPLE_MARKET_OPPORTUNITIES)
    cash_flows = get_cash_flow_projection()
    
    print(f"""
✅ WHAT THE SYSTEM DISCOVERED:

   SOLVABLES ACROSS ALL MARKETS:
   • Evident (obvious): Easy to identify and approach
   • Discreet: Requires some research and finesse
   • Very Discreet: Deep market knowledge required
   • Hidden: Exceptional opportunities requiring network
   • Secret: Ultra-rare, premium-tier opportunities

   CASH FLOWS BY HORIZON:
   • 24h Cash: ${hunt_results['cash_potential']['24h']:,.0f} (immediate needs)
   • 48h Cash: ${hunt_results['cash_potential']['48h']:,.0f} (urgent capital)
   • 72h Cash: ${hunt_results['cash_potential']['72h']:,.0f} (quick deployment)
   • 6-Month: ${hunt_results['cash_potential']['6m']:,.0f} (growth capital)
   • 2-Year: ${hunt_results['cash_potential']['2y']:,.0f} (strategic value)

   NATURAL OFFERS GENERATED:
   • Quick Cash Injection (revenue sharing)
   • Revenue Acceleration (partnership model)
   • Growth Investment (equity model)
   • Full Acquisition (strategic buyout)
   • Revenue Share (aligned growth)
   • Asset Purchase (selective acquisition)

   MULTI-MARKET COVERAGE:
   • All sectors (SaaS, Services, Retail, Consulting, Marketplace)
   • All geographies (scalable framework)
   • All stages (early to mature)
   • All quality levels (from cash-struggling to exceptional)

   INTELLIGENCE:
   • Detects REAL vs illusory solvability
   • Ranks by discretion level (visibility)
   • Prioritizes by natural fit
   • Generates thoughtful offers (not forced)
   • Projects cash flows across time horizons
   • Adapts strategy by market & opportunity type

═════════════════════════════════════════════════════════════════════════════════════════════════════

RESULT: SOPHISTICATED HUNTING SYSTEM
→ Discovers real solvables across all markets
→ Creates natural business offers
→ Projects realistic cash flows
→ No forcing, no fake opportunities
→ Premium quality focus from launch
→ Multi-horizon strategies (24h → 2y)
""")
    
    print("=" * 100)
    print("✅ ADVANCED HUNT SYSTEM OPERATIONAL")
    print("=" * 100)


if __name__ == "__main__":
    main()
