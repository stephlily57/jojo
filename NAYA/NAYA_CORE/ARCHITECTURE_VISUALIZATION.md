# 🏛️ NAYA_CORE Architecture Visualization

## Current Active Flow

```
USER/APPLICATION
     │
     ▼
┌─────────────────────────────────────┐
│     engine_master.process()         │  [CORE/engine_master.py]
│  Main Decision Orchestrator         │
└─────────────────────────────────────┘
     │
     ├──────────────────────────────┐
     │                              │
     ▼                              ▼
┌─────────────────────────┐  ┌──────────────────────┐
│   DecisionCore          │  │  EXECUTION_TRIGGER   │
│ .evaluate(opportunity)  │  │  .trigger()          │
│ [DECISION/decision_core]│  │ [DECISION/exec_trig] │
└─────────────────────────┘  └──────────────────────┘
     │
     ├─────────────┬──────────────┐
     │             │              │
     ▼             ▼              ▼
┌──────────┐  ┌──────────────┐  ┌─────────────┐
│ CAPITAL  │  │ Economic     │  │ Core        │
│ RESERVE  │  │ Thresholds   │  │ Constitution│
│ MANAGER  │  │ [DOCTRINE]   │  │ [DOCTRINE]  │
│[ECONOMIC]│  └──────────────┘  └─────────────┘
└──────────┘
     │
     ▼
Returns: decision_payload
     │
     ├─ decision_id
     ├─ classification
     ├─ priority
     └─ execution_type
```

## Runtime Hub Architecture

```
┌──────────────────────────────────────────────────────────────┐
│          naya_core_runtime.py (RUNTIME HUB)                 │
│          [RUNTIME/naya_core_runtime.py]                     │
│                                                              │
│  Integrates: 5 Major Subsystems                            │
└──────────────────────────────────────────────────────────────┘
          │
          ├─────────────────┬─────────────┬──────────┬────────┐
          │                 │             │          │        │
          ▼                 ▼             ▼          ▼        ▼
    ┌─────────────┐  ┌──────────────┐  ┌────────┐┌────────┐┌────┐
    │DecisionCore │  │Distributed   │  │Adaptive││Opportunity││Guard│
    │             │  │Memory        │  │Feedback││Pipeline  ││ian │
    │[core]       │  │[memory]      │  │[evol]  ││[orch]    ││[risk]
    └─────────────┘  └──────────────┘  └────────┘└────────┘└────┘
```

## Cluster Hub Architecture

```
┌──────────────────────────────────────────────────────────────┐
│       naya_core_cluster.py (CLUSTER HUB)                    │
│       [CLUSTER/naya_core_cluster.py]                        │
│                                                              │
│   Integrates: 8 Major Subsystems                           │
└──────────────────────────────────────────────────────────────┘
          │
    ┌─────┴─────┬───────────┬──────────┬──────────┬────────┬─────────┬──────┐
    │           │           │          │          │        │         │      │
    ▼           ▼           ▼          ▼          ▼        ▼         ▼      ▼
┌─────────┐┌──────────┐┌──────────┐┌──────────┐┌────────┐┌────────┐┌─────┐┌─────┐
│StateStr ││Strategic ││Sovereign ││Restructur││Density ││Strategic││Adapt││Degrad│
│ore      ││Context  ││Layer     ││ing Layer ││Layer   ││Memory   ││ive  ││ation │
│[state]  ││[core]   ││[sovern]  ││[evol]    ││[?]     ││[system] ││Feed ││Ctrl  │
└─────────┘└──────────┘└──────────┘└──────────┘└────────┘└────────┘└─────┘└─────┘
```

## Cognition Module (NEW - Phase 2-3)

```
┌──────────────────────────────────────────────────────┐
│       CognitiveHubNAYA                              │
│    [COGNITION/cognitive_hub.py]                     │
│  Master Orchestrator - Intelligence & Humanization │
└──────────────────────────────────────────────────────┘
          │
          ├──────────────────────────┬──────────────────────────┐
          │                          │                          │
          ▼                          ▼                          ▼
┌──────────────────────────┐┌────────────────────────┐┌─────────────────┐
│CognitiveFramework        ││MultilingualEngine      ││(Humanization +  │
│Advanced Intelligence     ││+ HumanizationEngine    ││15+ Languages)   │
│- Reasoning               ││- Native languages     ││- Cultural       │
│- Perception              ││- Market profiles      ││  sensitivity     │
│- Adaptability            ││- Communication styles ││- Forgotten      │
│[450+ lines]              ││[cultural profiles]    ││  markets        │
└──────────────────────────┘└────────────────────────┘└─────────────────┘
```

## Full Subsystem Map

```
                          NAYA_CORE
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    ┌───▼─────┐           ┌───▼─────┐         ┌────▼────┐
    │  KERNEL │           │ DECISION│         │ ECONOMIC│
    │  (CORE) │           │  FLOW   │         │ CONTROL │
    └─────────┘           └─────────┘         └─────────┘
    • naya_core.py        • decision_core       • capital
    • engine_master       • exec_trigger         • thresholds
    • state_store         • exec_perform_core    • cost_opt
        │                 • decision_perf_eng    
        │                 • outcome_predict      
        ▼                 • adapt_layer          
    ┌─────────────────────────────────────────────────┐
    │              DOCTRINE LAYER                     │
    │  Immuable Rules, Constitution, Governance       │
    │  • core_constitution.py                         │
    │  • economic_thresholds.py                       │
    │  • strategic_modes.py                           │
    └─────────────────────────────────────────────────┘
        │
        ├──────────┬──────────┬──────────┬──────────┐
        │          │          │          │          │
        ▼          ▼          ▼          ▼          ▼
    ┌────────┐┌─────────┐┌──────────┐┌──────────┐┌──────┐
    │RUNTIME ││ORCHESTRA││ COGNITION││ EVOLUTION││MEMORY│
    │        ││TION     ││          ││          ││      │
    │hubs:   ││• pipeline││intelligence││adapt_fb││dist_ │
    │runtime ││• channel ││• framework  ││• growth││mem  │
    │cluster ││• mission ││• multilingual││• signal││      │
    │        ││          ││• humanization││         ││      │
    └────────┘└─────────┘└──────────┘└──────────┘└──────┘
        │          │          │          │          │
        │          │          │          │          │
        ├──────────┼──────────┼──────────┼──────────┤
        │          │          │          │          │
        ▼          ▼          ▼          ▼          ▼
    ┌────────┐┌─────────┐┌──────────┐┌──────────┐┌─────┐
    │SOVEREIG││MONITORING││STRATEGY  ││  RISK    ││HUNT ││
    │NTY/OWN││• watchdog  ││ENGINE  ││  • guardian││• search
    │ERSHIP ││• self-heal ││(10 files)││(orphan?)││(orphan?
    │        ││• pattern  ││orphan?   ││          ││
    │        ││  detect    ││          ││          ││
    └────────┘└─────────┘└──────────┘└──────────┘└─────┘
```

## Integration Status by Subsystem

```
TIER 1 - CRITICAL PATH (100% active) ✅
├─ naya_core.py                   [ACTIVATION]
├─ engine_master.py               [DECISION FLOW]
├─ decision_core.py               [EVALUATION]
├─ DecisionCore→Capital           [GATE]
├─ DecisionCore→Thresholds        [GATE]
├─ DecisionCore→Constitution      [GATE]
└─ EXECUTION_TRIGGER              [EXECUTION]

TIER 2 - RUNTIME HUBS (50-100% active) ✅
├─ naya_core_runtime.py           [5/5 deps used ✅]
├─ naya_core_cluster.py           [8/8 deps used ✅]
└─ naya_core.py→Sovereignty       [1/5 deps used ✅]

TIER 3 - MEDIUM INTEGRATION (20-50%) ⚠️
├─ evolution/ (2/8 used)
├─ memory/ (1/8 used)
├─ orchestration/ (1/8 used)
├─ monitoring/ (1/7 used)
├─ system/ (1/4 used)
├─ risk/ (1/2 used)
├─ doctrine/ (2/5 used)
└─ economic/ (1/6 used)

TIER 4 - LOW INTEGRATION (0-20%) 🔴
├─ decision/ NEW ENGINES (0/5 used ❌)
├─ execution/ (? subdirs unexplored)
├─ cognition/ (3/13 used, subdirs unexplored)
├─ strategy_engine/ (0/10 used)
└─ hunt/ (0/2 used)

TIER 5 - UNKNOWN STATE (unpigeonholed) ❌
├─ execution/accelerators/
├─ execution/external_brains/
├─ execution/external_tools/
├─ execution/policies/
├─ execution/providers/
├─ execution/sovereign_automation/
├─ cognition/fusion/
├─ cognition/interface/
├─ cognition/layers/
└─ cognition/memory/
```

## New Engines Created (Phase 2-3) - Integration Status

```
CREATED BUT NOT WIRED ❌
─────────────────────────

executive_performance_core.py
  ├─ 5 internal engines:
  │  ├─ decision_performance_engine.py
  │  ├─ outcome_prediction_engine.py
  │  ├─ strategic_adaptation_layer.py
  │  └─ decision_accelerator.py
  │
  Imported by:
  ├─ executive_usage_guide.py ✅ (guide only)
  ├─ deployment_guide.py ✅ (guide only)
  └─ decision_core.py? ❌ NO!
  
  Status: ORPHANED - Created but not integrated into main flow!

WIRED & PRODUCTION ✅
─────────────────────────

cognitive_hub.py
  ├─ Imports:
  │  ├─ cognitive_intelligence_framework.py
  │  └─ multilingual_cultural_engine.py
  │
  Imported by:
  ├─ executive_usage_guide.py ✅
  ├─ deployment_guide.py ✅
  └─ cognition/__init__.py ✅
  
  Status: PRODUCTION - Well integrated

cognitive_intelligence_framework.py
  ├─ 450+ lines production code
  ├─ 5 advanced engines
  └─ Full cognitive reasoning
  
  Status: PRODUCTION

multilingual_cultural_engine.py
  ├─ 15+ native language support
  ├─ Cultural market profiles
  └─ Humanization layer
  
  Status: PRODUCTION
```

## Data Flow Paths

```
PATH 1: DECISION EXECUTION
────────────────────────────
opportunity_data
  → engine_master.process()
    → DecisionCore.evaluate()
      → check_capital() [ECONOMIC]
      → classify() [DOCTRINE]
      → hash_integrity() [DOCTRINE]
      → return decision_payload
    → EXECUTION_TRIGGER.trigger()
      → route_to_executor()

PATH 2: RUNTIME ORCHESTRATION
──────────────────────────────
naya_core_runtime.run()
  ├─ DecisionCore.evaluate()
  ├─ DistributedMemory.fetch()
  ├─ AdaptiveFeedback.process()
  ├─ OpportunityPipeline.execute()
  └─ Guardian.validate_risk()
  
  → Continuous loop

PATH 3: CLUSTER REPLICATION
────────────────────────────
naya_core_cluster.sync()
  ├─ StateStore.replicate()
  ├─ StrategicContext.share()
  ├─ SovereigntyLayer.verify()
  ├─ RestructuringLayer.adapt()
  ├─ DensityLayer.compute()
  ├─ StrategicMemory.broadcast()
  ├─ AdaptiveFeedback.sync_learning()
  └─ DegradationControl.report()

PATH 4: COGNITION PROCESSING (GUIDES ONLY)
────────────────────────────────────────────
get_cognitive_hub()
  → CognitiveFramework.process()
    ├─ AdvancedIntelligenceEngine.reason()
    ├─ PerceptionEngine.sense()
    └─ AdaptabilityEngine.adapt()
  
  AND

  → MultilingualEngine.translate_to_native()
    → HumanizationEngine.humanize_response()
    → return_culturally_appropriate_message()
```

## Critical Issues Map

```
❌ PROBLEM 1: Executive Core Not Wired
  Location: decision/executive_performance_core.py
  Impact: 5 new engines created but unused
  Severity: HIGH
  
❌ PROBLEM 2: Strategy Engine Orphaned?
  Location: strategy_engine/ (10 files)
  Impact: No integration detected
  Severity: MEDIUM
  
❌ PROBLEM 3: Subdirs Not Explored
  Location: execution/*, cognition/submodules
  Impact: Unknown integration status
  Severity: MEDIUM
  
❌ PROBLEM 4: Empty __init__.py Files
  Location: decision/, economic/, execution/
  Impact: Broken module exports
  Severity: MEDIUM
  
❌ PROBLEM 5: Hunt & Strategy Abandoned?
  Location: hunt/, strategy_engine/
  Impact: 12 files possible orphans
  Severity: LOW
```

## Recommended Integration Points

```
IMMEDIATE ACTIONS
─────────────────

1. Wire executive_performance_core into decision_core
   
   decision_core.py should call:
   from NAYA_CORE.decision.executive_performance_core import get_executive_core
   
   In evaluate() method:
   executive_result = get_executive_core().process(opportunity)

2. Populate __init__.py files
   
   decision/__init__.py → export DecisionCore + new engines
   economic/__init__.py → export CAPITAL_RESERVE_MANAGER + others
   execution/__init__.py → export ExecutionMatrix + others

3. Explore subdirectories
   
   List all files in:
   - execution/accelerators/
   - execution/external_brains/
   - execution/external_tools/
   - execution/policies/
   - execution/providers/
   - execution/sovereign_automation/
   - cognition/fusion/
   - cognition/interface/
   - cognition/layers/
   - cognition/memory/

MEDIUM TERM ACTIONS
───────────────────

4. Integrate or Orphan Strategy Engine
   
   Determine:
   - Is strategy_engine called anywhere?
   - Is it lazy-loaded by orchestration?
   - If unused for 6+ months → deprecate?

5. Validate Hunt & Monitoring
   
   - Verify hunt/ is not used elsewhere
   - Verify monitoring/ is properly called
   - Check if watchdog/self-healing active

6. Create Dependency Graph
   
   Generate visual map of all import chains
   for documentation
```

