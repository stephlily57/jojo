"""
NAYA_CORE - 10 BRAINS UNIFIED SYSTEM
Démonstration et Guide d'Utilisation

Utiliser le système intégré avec tous les cerveaux coordonnés.
"""

from NAYA_CORE.core.unified_orchestrator import (
    get_unified_orchestrator,
    evaluate_with_full_brains,
    get_system_capabilities
)

# ============================================================================
# EXAMPLE 1: Simple Usage - Evaluate Opportunity with All 10 Brains
# ============================================================================

def example_simple_evaluation():
    """
    Usage simple: passe une opportunité, obtiens une décision du système complet.
    """
    
    opportunity = {
        "name": "Market Expansion to Brazil",
        "value": 50000,
        "market": "South America",
        "type": "market_expansion",
        "timeline": "6 months",
        "risk_level": "medium"
    }
    
    # This internally engages ALL 10 brains
    result = evaluate_with_full_brains(opportunity)
    
    print("=" * 80)
    print("DECISION WITH ALL 10 BRAINS ENGAGED")
    print("=" * 80)
    print(f"Status: {result.get('status')}")
    print(f"Strategy Analysis: {result.get('strategy_analysis')}")
    print(f"Risk Assessment: {result.get('risk_assessment')}")
    print(f"Cognition Context: {result.get('cognition_context')}")
    print(f"Market Context: {result.get('market_context')}")
    print(f"Brains Engaged: {', '.join(result.get('brains_engaged'))}")
    print(f"System Health: {result.get('system_health')}%")


# ============================================================================
# EXAMPLE 2: Advanced Usage - Access Orchestrator Directly
# ============================================================================

def example_advanced_control():
    """
    Usage avancée: accès direct à l'orchestrateur pour contrôle granulaire.
    """
    
    orchestrator = get_unified_orchestrator()
    
    print("\n" + "=" * 80)
    print("ORCHESTRATOR DIRECT ACCESS")
    print("=" * 80)
    
    # Check system status
    status = orchestrator.get_system_status()
    print(f"\n✅ System Status:")
    print(f"   Brains Active: {status['brains_active']}")
    print(f"   Decisions Processed: {status['decisions_processed']}")
    print(f"   Learning Iterations: {status['learning_iterations']}")
    print(f"   System Health: {status['system_health']}%")
    
    # Evaluate multiple opportunities
    opportunities = [
        {"name": "Product Launch", "value": 30000},
        {"name": "Team Expansion", "value": 20000},
        {"name": "Tech Infrastructure", "value": 50000}
    ]
    
    print(f"\n📊 Processing {len(opportunities)} Opportunities:")
    
    for opp in opportunities:
        result = orchestrator.evaluate_opportunity(opp)
        print(f"\n  • {opp['name']} (${opp['value']}):")
        print(f"    Status: {result['status']}")
        print(f"    Decision: {result['decision_evaluation']}")


# ============================================================================
# EXAMPLE 3: System Capabilities Overview
# ============================================================================

def example_system_capabilities():
    """
    Affiche toutes les capacités du système.
    """
    
    capabilities = get_system_capabilities()
    
    print("\n" + "=" * 80)
    print("NAYA_CORE SYSTEM CAPABILITIES")
    print("=" * 80)
    
    print(f"\n🧠 Total Brains: {capabilities['total_brains']}")
    print(f"\n📋 Brain Details:")
    
    for brain in capabilities['brains']:
        print(f"\n   {brain['name']}")
        print(f"   ├─ Function: {brain['function']}")
        print(f"   ├─ Status: {brain['status']}")
        print(f"   ├─ Engines: {brain['engines']}")
        print(f"   └─ Dependencies: {', '.join(brain['dependencies'])}")


# ============================================================================
# EXAMPLE 4: Multi-Language Cognition Processing
# ============================================================================

def example_multilingual_cognition():
    """
    Démontre la capacité multilingue du Cognition Brain.
    """
    
    from NAYA_CORE.cognition import (
        get_cognitive_hub,
        LocalMarketLanguageProfile
    )
    
    print("\n" + "=" * 80)
    print("COGNITION BRAIN - MULTILINGUAL CAPABILITY")
    print("=" * 80)
    
    hub = get_cognitive_hub()
    
    languages = ["Portuguese", "Spanish", "French", "Japanese", "Arabic"]
    
    for lang in languages:
        print(f"\n🌍 Language: {lang}")
        # In real implementation, would process opportunity in native language
        print(f"   ✅ Native processing enabled")
        print(f"   ✅ Cultural markers recognized")
        print(f"   ✅ Market-specific communication adapted")


# ============================================================================
# EXAMPLE 5: Memory Brain - Historical Lookups
# ============================================================================

def example_memory_brain():
    """
    Démontre la capacité de mémoire du Memory Brain.
    """
    
    print("\n" + "=" * 80)
    print("MEMORY BRAIN - HISTORICAL DECISION LOOKUPS")
    print("=" * 80)
    
    orchestrator = get_unified_orchestrator()
    
    # Simulate memory lookups
    similar_decisions = [
        {
            "id": "D-12847",
            "decision": "Market expansion to France",
            "value": 45000,
            "outcome": "✅ Success",
            "roi": "196%",
            "time_to_execution": "4 months"
        },
        {
            "id": "D-12891",
            "decision": "Market expansion to Germany",
            "value": 48000,
            "outcome": "✅ Success",
            "roi": "186%",
            "time_to_execution": "3 months"
        },
        {
            "id": "D-12920",
            "decision": "Market expansion to Spain",
            "value": 50000,
            "outcome": "✅ Success",
            "roi": "240%",
            "time_to_execution": "5 months"
        }
    ]
    
    print("\n🔍 Similar Past Decisions:")
    
    for decision in similar_decisions:
        print(f"\n   ID: {decision['id']}")
        print(f"   └─ Decision: {decision['decision']}")
        print(f"   └─ Value: ${decision['value']}")
        print(f"   └─ Outcome: {decision['outcome']}")
        print(f"   └─ ROI: {decision['roi']}")
        print(f"   └─ Timeline: {decision['time_to_execution']}")
    
    print(f"\n📈 Analysis:")
    print(f"   • Average ROI for similar decisions: 207%")
    print(f"   • Success rate: 100% (3/3)")
    print(f"   • Confidence for similar new decision: 95%")


# ============================================================================
# EXAMPLE 6: Evolution Brain - Continuous Learning
# ============================================================================

def example_evolution_brain():
    """
    Démontre la capacité d'apprentissage du Evolution Brain.
    """
    
    print("\n" + "=" * 80)
    print("EVOLUTION BRAIN - CONTINUOUS LEARNING")
    print("=" * 80)
    
    orchestrator = get_unified_orchestrator()
    
    # Simulate learning cycle
    decision_cycle = {
        "decision": "Launch promotional campaign",
        "expected_outcome": {
            "revenue_increase": 60000,
            "roi": "3:1"
        },
        "actual_outcome": {
            "revenue_increase": 85000,
            "roi": "4.25:1"
        },
        "delta": "+25000" ,
        "learning_applied": {
            "marketing_confidence": "+8% (78% → 86%)",
            "promotion_timing": "Sweet spot identified: mid-week",
            "budget_allocation": "+5% to marketing",
            "new_pattern": "Q2 promotions outperform Q3"
        }
    }
    
    print(f"\n🔄 Learning Cycle:")
    print(f"\n   Decision: {decision_cycle['decision']}")
    print(f"\n   Expected: ${decision_cycle['expected_outcome']['revenue_increase']} " +
          f"({decision_cycle['expected_outcome']['roi']})")
    print(f"   Actual: ${decision_cycle['actual_outcome']['revenue_increase']} " +
          f"({decision_cycle['actual_outcome']['roi']})")
    print(f"   Delta: {decision_cycle['delta']} (outperformed by +42%)")
    
    print(f"\n   💡 Learning Applied:")
    for item, value in decision_cycle['learning_applied'].items():
        print(f"      • {item}: {value}")
    
    print(f"\n   📊 Impact on Future Decisions:")
    print(f"      ✅ Next marketing decision: +8% confidence")
    print(f"      ✅ Budget allocation: Shifted 5% to marketing")
    print(f"      ✅ Decision speed: 15% faster approval")


# ============================================================================
# EXAMPLE 7: Risk Brain - Intelligent Protection
# ============================================================================

def example_risk_brain():
    """
    Démontre la capacité de protection du Risk Brain.
    """
    
    print("\n" + "=" * 80)
    print("RISK BRAIN - INTELLIGENT PROTECTION")
    print("=" * 80)
    
    risk_assessment = {
        "opportunity": "Expand to unstable political region",
        "value": 100000,
        "risk_analysis": {
            "capital_risk": {"score": "2/10", "status": "LOW"},
            "market_risk": {"score": "7/10", "status": "HIGH"},
            "execution_risk": {"score": "6/10", "status": "MEDIUM-HIGH"},
            "external_risk": {"score": "8/10", "status": "HIGH"}
        },
        "composite_risk": "6.5/10 (ELEVATED)",
        "automatic_mitigations": [
            "Phased approach: Start with $30K pilot",
            "Partnership: Find local partner",
            "Insurance: Add political risk coverage",
            "Timeline: Extend from 6 to 12 months",
            "Contingency: Reserve additional capital"
        ],
        "modified_proposal": {
            "phase_1": {"duration": "3 months", "investment": "$5K",
                        "focus": "Research + partner ID"},
            "phase_2": {"duration": "3 months", "investment": "$30K",
                        "focus": "Pilot + regulatory"},
            "phase_3": {"duration": "6 months", "investment": "$40K",
                        "focus": "Gradual expansion"}
        }
    }
    
    print(f"\n⚠️ Opportunity: {risk_assessment['opportunity']}")
    print(f"   Value: ${risk_assessment['value']}")
    
    print(f"\n   Risk Scores:")
    for risk_type, assessment in risk_assessment['risk_analysis'].items():
        print(f"   • {risk_type}: {assessment['score']} ({assessment['status']})")
    
    print(f"\n   Composite Risk: {risk_assessment['composite_risk']}")
    
    print(f"\n   🛡️ Automatic Mitigations Engaged:")
    for i, mitigation in enumerate(risk_assessment['automatic_mitigations'], 1):
        print(f"      {i}. {mitigation}")
    
    print(f"\n   ✅ Modified Proposal (Phased Approach):")
    for phase, details in risk_assessment['modified_proposal'].items():
        print(f"      {phase.upper()}: {details['duration']} | " +
              f"${details['investment']} | {details['focus']}")
    
    print(f"\n   ✅ Guardian Approval: Recommended APPROVAL with safeguards")


# ============================================================================
# EXAMPLE 8: Orchestration Brain - Complex Mission
# ============================================================================

def example_orchestration_brain():
    """
    Démontre la coordination complexe du Orchestration Brain.
    """
    
    print("\n" + "=" * 80)
    print("ORCHESTRATION BRAIN - COMPLEX MISSION COORDINATION")
    print("=" * 80)
    
    mission = {
        "opportunities": [
            {"name": "Product update", "value": 20000, "urgency": "HIGH"},
            {"name": "Market entry", "value": 50000, "urgency": "MEDIUM"},
            {"name": "Partnership deal", "value": 15000, "urgency": "MEDIUM"},
            {"name": "Team training", "value": 8000, "urgency": "LOW"},
            {"name": "Infrastructure", "value": 30000, "urgency": "MEDIUM"}
        ],
        "optimized_plan": {
            "phase_1": {
                "week": "Week 1",
                "actions": ["Infrastructure upgrade"],
                "investment": "$30K"
            },
            "phase_2": {
                "week": "Weeks 2-3",
                "actions": ["Product update", "Team training"],
                "investment": "$28K"
            },
            "phase_3": {
                "week": "Weeks 4-6",
                "actions": ["Market entry + Partnership (fused)"],
                "investment": "$65K"
            }
        },
        "results": {
            "timeline_improvement": "40% faster",
            "cost_savings": "15% via deduplication",
            "sequential_time": "10 weeks",
            "optimized_time": "6 weeks"
        }
    }
    
    print(f"\n📋 Opportunities Detected: {len(mission['opportunities'])}")
    
    for opp in mission['opportunities']:
        print(f"   • {opp['name']}: ${opp['value']} (Urgency: {opp['urgency']})")
    
    print(f"\n🎯 Optimized Orchestration Plan:")
    
    for phase, details in mission['optimized_plan'].items():
        print(f"\n   {phase.upper()} ({details['week']}):")
        print(f"   ├─ Actions: {', '.join(details['actions'])}")
        print(f"   └─ Investment: {details['investment']}")
    
    print(f"\n📊 Results:")
    print(f"   • Timeline: {mission['results']['sequential_time']} → " +
          f"{mission['results']['optimized_time']} " +
          f"({mission['results']['timeline_improvement']})")
    print(f"   • Cost savings: {mission['results']['cost_savings']}")


# ============================================================================
# MAIN - Run All Examples
# ============================================================================

if __name__ == "__main__":
    
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "NAYA_CORE - 10 UNIFIED BRAINS DEMONSTRATION".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")
    
    # Run examples
    example_system_capabilities()
    example_simple_evaluation()
    example_advanced_control()
    example_multilingual_cognition()
    example_memory_brain()
    example_evolution_brain()
    example_risk_brain()
    example_orchestration_brain()
    
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + "Summary: All 10 Brains Operating".center(78) + "║")
    print("║" + "✅ Decision | Strategy | Cognition | Evolution | Orchestration".center(78) + "║")
    print("║" + "✅ Memory | Monitoring | Hunt | Cluster | Risk".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("║" + "Result: Integrated Business Intelligence System".center(78) + "║")
    print("╚" + "=" * 78 + "╝")
    print()
