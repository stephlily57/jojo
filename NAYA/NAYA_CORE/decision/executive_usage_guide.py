"""
INTEGRATION: Executive Performance Core

Comment intégrer l'executive_performance_core dans une application.
"""

from NAYA_CORE.decision.executive_performance_core import get_executive_core

# ════════════════════════════════════════════════════════════════════════════
# UTILISATION SIMPLE
# ════════════════════════════════════════════════════════════════════════════

def simple_usage_example():
    """Exemple d'utilisation simple du système exécutif."""
    
    executive = get_executive_core()
    
    # Définir une opportunité
    opportunity = {
        "name": "BOTANICA_EGYPT",
        "value": 3_000_000,
        "pain_points": ["affordability", "quality", "trust"],
        "premium_positioning": True
    }
    
    # Définir le contexte marché
    market_context = {
        "cultural_sensitivity": 0.8,
        "market_temperature": 0.7,
        "regulatory_risk": 0.2
    }
    
    # ✅ ÉTAPE 1: DÉCISION COMPLÈTE (incorpore tout automatiquement)
    print("\n1. MAKING DECISION...")
    decision = executive.decide_and_execute(
        opportunity=opportunity,
        market_context=market_context
    )
    
    print(f"   Decision ID: {decision['decision_id']}")
    print(f"   Status: {decision['status']}")
    print(f"   Confidence: {decision['confidence_final']:.0%}")
    print(f"   Predicted Success: {decision['prediction']:.0%}")
    print(f"   Speed Target: {decision['target_speed']}")
    print(f"   Recommendation: {decision['recommendation']}")
    print(f"   Suggested Adaptations: {decision['adaptations']}")
    
    # ✅ ÉTAPE 2: EXÉCUTION
    print("\n2. EXECUTING...")
    print("   [Company executes the decision]")
    print("   [Real market results come back]")
    
    # Simule 3 mois plus tard
    actual_outcome = 0.82  # Mieux que prédit (0.80)
    
    # ✅ ÉTAPE 3: FEEDBACK (génère apprentissage automatique)
    print("\n3. RECORDING OUTCOME...")
    feedback = executive.record_outcome(
        decision_id=decision['decision_id'],
        actual_outcome=actual_outcome,
        was_successful=True
    )
    
    print(f"   Actual Success: {actual_outcome:.0%}")
    print(f"   vs Prediction: {decision['prediction']:.0%}")
    print(f"   Improvement: {feedback['improvement']:+.1%}")
    print(f"   Patterns Detected: {feedback['patterns_detected']}")
    print(f"   Confidence Improvement: {feedback['confidence_improvement']}")
    
    # ✅ ÉTAPE 4: LA PROCHAINE DÉCISION EST MEILLEURE
    print("\n4. NEXT DECISION (now improved)...")
    
    opportunity_2 = {
        "name": "BOTANICA_KENYA",
        "value": 2_500_000,
        "pain_points": ["affordability", "quality", "trust"],
        "premium_positioning": True  # Similaire à Égypte
    }
    
    market_2 = {
        "cultural_sensitivity": 0.75,
        "market_temperature": 0.65,
        "regulatory_risk": 0.25
    }
    
    decision_2 = executive.decide_and_execute(opportunity_2, market_2)
    
    # La confiance est maintenant plus ÉLEVÉE car NAYA a appris de Egypt
    print(f"   Confidence (initial): {decision_2['confidence_initial']:.0%}")
    print(f"   → Kenya is similar to Egypt where we learned")
    print(f"   → Confidence is now HIGHER automatically")
    
    # ════════════════════════════════════════════════════════════════════════
    # ✅ RÉSUMÉ FINAL
    # ════════════════════════════════════════════════════════════════════════
    
    print("\n" + "="*70)
    print("EXECUTIVE CORE SUMMARY")
    print("="*70)
    
    summary = executive.get_performance_summary()
    
    print(f"""
Decisions Processed: {summary.decisions_count}
  → {summary.decisions_completed} completed with outcomes
  
Decision Quality:
  → Accuracy: {summary.accuracy:.0%} (% correct decisions)
  → Speed: {summary.speed_vs_baseline:.2f}x baseline
  → Efficiency: {summary.efficiency:.2f} value/effort
  
Learning:
  → Velocity: {summary.learning_velocity:+.1%} improvement/cycle
  → Patterns detected: {summary.patterns_learned}
  → Strategy rules created: {summary.strategy_rules}
  
Calibration:
  → Confidence matches reality: {summary.confidence_calibration:.0%}
  → My expressed confidence = actual success rate
""")


# ════════════════════════════════════════════════════════════════════════════
# UTILISATION AVANCÉE
# ════════════════════════════════════════════════════════════════════════════

def advanced_usage_example():
    """Utilisation avancée avec contrôle fin."""
    
    executive = get_executive_core()
    
    opportunity = {
        "name": "HIGH_RISK_PROJECT",
        "value": 50_000_000,
        "pain_points": ["market", "execution", "cultural"],
        "premium_positioning": True,
        "team_experience_level": 0.6
    }
    
    market = {
        "cultural_sensitivity": 0.4,  # Faible
        "market_saturation": 0.8,      # Saturé
        "regulatory_risk": 0.5         # Modéré
    }
    
    # ✅ CAN FORCE SPEED
    decision = executive.decide_and_execute(
        opportunity=opportunity,
        market_context=market,
        force_speed="CAREFUL"  # Force une vitesse prudente
    )
    
    print(f"""
Forced Speed Decision:
  → Speed: {decision['target_speed']} (forced CAREFUL)
  → Confidence: {decision['confidence_final']:.0%}
  → Recommendation: {decision['recommendation']}
  → Risk Factors:
""")
    for risk in decision['risk_factors']:
        print(f"    - {risk['description']}")
        print(f"      Level: {risk['level']}")
    
    # ════════════════════════════════════════════════════════════════════════
    # ✅ INSPECT INTERNAL ENGINES
    # ════════════════════════════════════════════════════════════════════════
    
    print("\n════════════════════════════════════════════════")
    print("INTERNAL ENGINES STATE")
    print("════════════════════════════════════════════════")
    
    # 1. Performance Engine
    print("\n1. PERFORMANCE ENGINE:")
    perf = executive.performance_engine.get_performance_metrics("TOTAL")
    print(f"   Accuracy: {perf.accuracy:.0%}")
    print(f"   Speed: {perf.speed:.2f}x")
    print(f"   Efficiency: {perf.efficiency:.2f}")
    print(f"   Confidence Calibration: {perf.confidence_calibration:.0%}")
    
    # 2. Adaptation Layer
    print("\n2. ADAPTATION LAYER:")
    learning = executive.adaptation_layer.get_learning_summary()
    print(f"   Patterns Detected: {learning['patterns_detected']}")
    print(f"   Strategy Rules: {learning['strategy_rules_created']}")
    print(f"   Learning Velocity: {learning['learning_velocity']}")
    for pattern in learning['top_patterns'][:3]:
        print(f"   - {pattern['name']}: {pattern['strength']} (n={pattern['samples']})")
    
    # 3. Prediction Engine
    print("\n3. PREDICTION ENGINE:")
    pred_acc = executive.prediction_engine.get_prediction_accuracy()
    if pred_acc:
        print(f"   Prediction Accuracy: {pred_acc:.0%}")
    else:
        print(f"   No predictions recorded yet")
    
    # 4. Decision History
    print("\n4. RECENT DECISIONS:")
    history = executive.get_decision_history(limit=5)
    for rec in history:
        print(f"   - {rec['decision_id']}: {rec['opportunity']}")
        print(f"     Status: {rec['status']}, Confidence: {rec['confidence']:.0%}")


# ════════════════════════════════════════════════════════════════════════════
# INTEGRATION AVEC NAYA_CORE DECISION
# ════════════════════════════════════════════════════════════════════════════

def integration_with_naya_core():
    """Comment intégrer avec le reste de NAYA_CORE."""
    
    from NAYA_CORE.economic.capital_reserve_manager import CAPITAL_RESERVE_MANAGER
    from NAYA_CORE.doctrine.core_constitution import CoreConstitution
    from NAYA_CORE.cognition import get_cognitive_hub, LocalMarketLanguageProfile
    
    executive = get_executive_core()
    
    opportunity = {
        "name": "BOTANICA_SWAHILI",
        "value": 2_000_000,
        "pain_points": ["affordability", "quality"],
        "premium_positioning": True
    }
    
    # ════════════════════════════════════════════════════════════════════────
    # OPTION 1: Intégration simple (laisse executive gérer)
    # ════════════════════════────────────────────────────────────────────────
    
    decision = executive.decide_and_execute(opportunity)
    
    if decision['status'] == "APPROVED":
        print("✓ Decision approved by executive")
        print("  Proceeding to execution...")
    
    # ════════════════════════════════════════════════════════════════════────
    # OPTION 2: Intégration riche (utiliser cognitive hub aussi)
    # ════════════════════────────────────────────────────────────────────────
    
    print("\n" + "="*70)
    print("ENRICHED INTEGRATION")
    print("="*70)
    
    # 1. Executive decision
    market = {
        "cultural_sensitivity": 0.8,
        "regulatory_risk": 0.2
    }
    
    decision = executive.decide_and_execute(opportunity, market)
    
    # 2. Cognitive analysis (pour humanisation + multilingual)
    if decision['status'] == "APPROVED":
        hub = get_cognitive_hub()
        
        market_profile = LocalMarketLanguageProfile(
            market_name="Kenya (Swahili)",
            primary_language_code="sw",
            secondary_languages=["en"],
            communication_style="relational",
            group_harmony_importance=0.8
        )
        
        cognitive_analysis = hub.analyze_opportunity_for_market(opportunity, market_profile)
        
        print(f"Executive Decision: {decision['confidence_final']:.0%} confidence")
        print(f"Cognitive Analysis: {cognitive_analysis['weighted_recommendation_score']:.1%} fit")
        print(f"Humanized Message: '{cognitive_analysis['cognitive_dimensions']['humanization']['human_centric_narrative'][:60]}...'")
        print(f"Native Language: {cognitive_analysis['cognitive_dimensions']['multilingual']['language_code'].upper()}")
    
    # ════════════════════════════════════════════════════════════════════────
    # OPTION 3: Feed back into NAYA ecosystem
    # ════════════────────────────────────════════════────────────────────────
    
    print("\n" + "="*70)
    print("FEEDBACK INTO NAYA ECOSYSTEM")
    print("="*70)
    
    # Months later, outcomes come in
    actual_market_result = 0.84
    
    # Record in executive
    feedback = executive.record_outcome(decision['decision_id'], actual_market_result)
    
    # This automatically:
    # 1. ✓ Updates performance metrics
    # 2. ✓ Improves prediction accuracy
    # 3. ✓ Learns new patterns
    # 4. ✓ Creates strategy rules
    # 5. ✓ Calibrates confidence
    
    print(f"Outcome recorded: {actual_market_result:.0%}")
    print(f"Learning applied: {feedback['patterns_detected']} patterns detected")
    print(f"Next decisions: Will be {feedback['confidence_improvement']} more confident")


# ════════════════════════════════════════════════════════════════════════════
# BATCH OPERATIONS
# ════════════════════════════════════════════════════════════════════════════

def batch_decision_processing():
    """Traiter plusieurs décisions en batch."""
    
    executive = get_executive_core()
    
    opportunities = [
        {
            "name": "PROJ_1",
            "value": 1_000_000,
            "pain_points": ["cost"],
            "premium_positioning": False
        },
        {
            "name": "PROJ_2",
            "value": 5_000_000,
            "pain_points": ["cost", "quality"],
            "premium_positioning": True
        },
        {
            "name": "PROJ_3",
            "value": 2_000_000,
            "pain_points": ["cost", "quality", "trust"],
            "premium_positioning": True
        }
    ]
    
    print("\n" + "="*70)
    print("BATCH DECISION PROCESSING")
    print("="*70)
    
    decisions = []
    
    for opp in opportunities:
        decision = executive.decide_and_execute(opportunity=opp)
        decisions.append(decision)
        print(f"✓ {opp['name']}: {decision['confidence_final']:.0%} confidence → {decision['recommendation']}")
    
    # Après exécution batch
    print(f"\nProcessed {len(decisions)} decisions")
    
    # Simu feedback
    for decision, actual in zip(decisions, [0.75, 0.88, 0.82]):
        executive.record_outcome(decision['decision_id'], actual)
    
    summary = executive.get_performance_summary()
    print(f"\nSystem Learning Status:")
    print(f"  → {summary.patterns_learned} patterns learned")
    print(f"  → {summary.strategy_rules} strategy rules")
    print(f"  → {summary.learning_velocity:+.1%} improvement velocity")


# ════════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    
    print("""
╔═══════════════════════════════════════════════════════════╗
║  EXECUTIVE PERFORMANCE CORE - USAGE GUIDE                ║
║                                                           ║
║  NAYA_CORE Naturally Intelligent, Fast & Self-Learning   ║
╚═══════════════════════════════════════════════════════════╝
""")
    
    print("1. SIMPLE USAGE")
    print("─" * 70)
    simple_usage_example()
    
    print("\n\n2. ADVANCED USAGE")
    print("─" * 70)
    # advanced_usage_example()
    
    # print("\n\n3. INTEGRATION WITH NAYA_CORE")
    # print("─" * 70)
    # integration_with_naya_core()
    
    # print("\n\n4. BATCH OPERATIONS")
    # print("─" * 70)
    # batch_decision_processing()
