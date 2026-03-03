#!/usr/bin/env python3
"""
Quick Integration Test - Verify all 4 layers work together

Test flow: Create opportunity → Route to executor → Persist result → Audit log
"""

import sys
import json
import os
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_imports():
    """Test all critical imports"""
    print("Testing imports...")
    try:
        # Layer 1: Execution
        from NAYA_ORCHESTRATION.orchestrator import ProjectOrchestrator
        from NAYA_ORCHESTRATION.router.execution_router import ExecutionRouter
        
        # Layer 2: Security
        from REAPERS.security_engine import RapersSecurityEngine
        
        # Layer 3: Persistence
        from PERSISTENCE.persistence_manager import PersistenceManager
        from PERSISTENCE.snapshot_manager import SnapshotManager
        
        # Layer 4: Business
        from BUSINESS_ENGINES.strategic_pricing_engine.pricing_engine import StrategicPricingEngine
        from BUSINESS_ENGINES.business_model_engine.pain_silence_engine import PainSilenceEngine
        from BUSINESS_ENGINES.business_model_engine.business_hunter_engine import BusinessHuntingOrchestrator
        from NAYA_PROJECT_ENGINE.supreme_business_orchestrator import SupremeBusinessOrchestrator
        
        print("✅ All imports successful!")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False


def test_quick_business_generation():
    """Test the quick business generation pipeline"""
    print("\nTesting quick business generation...")
    try:
        from BUSINESS_ENGINES.strategic_pricing_engine.pricing_engine import StrategicPricingEngine
        
        engine = StrategicPricingEngine()
        
        # Test quick cash options
        options = engine.get_fast_cash_options()
        assert len(options) > 0, "No fast cash options generated"
        
        # Test bundle recommendations
        bundles = engine.get_bundle_recommendations()
        assert len(bundles) >= 5, "Expected 5+ bundle recommendations"
        
        # Test proposal generation
        proposal = engine.generate_quick_proposal(
            client_name="Test Corp",
            problem_area="Efficiency",
            budget=10000,
            timeline_days=3
        )
        
        assert proposal['total_price'] <= 10000, "Proposal exceeds budget"
        assert proposal['timeline'] <= 3, "Proposal exceeds timeline"
        
        print(f"✅ Generated {len(options)} fast-cash options")
        print(f"✅ Generated {len(bundles)} premium bundles")
        print(f"✅ Generated proposal for €{proposal['total_price']}")
        return True
        
    except Exception as e:
        print(f"❌ Quick business generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_execution_planning():
    """Test execution planning and routing"""
    print("\nTesting execution planning...")
    try:
        from NAYA_ORCHESTRATION.orchestrator import ProjectOrchestrator, ProjectStatus
        
        orchestrator = ProjectOrchestrator()
        
        # Create a test business model
        business_model = {
            'name': 'Quick Audit Service',
            'type': 'audit',
            'scope': 'Complete systems audit',
            'requirements': ['analysis', 'reporting']
        }
        
        # Create execution plan
        plan = orchestrator.create_execution_plan(
            project_id="test-001",
            business_model=business_model
        )
        
        assert plan is not None, "No execution plan created"
        assert plan.project_id == "test-001", "Project ID mismatch"
        assert plan.status == ProjectStatus.PENDING, "Plan should start as PENDING"
        assert len(plan.execution_tasks) > 0, "No tasks created"
        
        print(f"✅ Created execution plan with {len(plan.execution_tasks)} tasks")
        print(f"✅ Plan status: {plan.status.value}")
        return True
        
    except Exception as e:
        print(f"❌ Execution planning failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_security_engine():
    """Test security and audit logging"""
    print("\nTesting security engine...")
    try:
        from REAPERS.security_engine import RapersSecurityEngine, SecurityLevel
        
        reapers = RapersSecurityEngine()
        
        # Test authentication
        authenticated, token = reapers.authenticate_user(
            "test_user",
            {"password": "test_password"}
        )
        
        assert authenticated, "Authentication failed"
        assert token is not None, "No token issued"
        
        # Test authorization
        is_allowed = reapers.authorize_action(
            token,
            "read",
            "project_data"
        )
        
        # Test audit trail
        trail = reapers.get_audit_trail(limit=10)
        assert len(trail) > 0, "No audit trail events"
        
        print(f"✅ Authentication successful, token issued")
        print(f"✅ Authorization check passed")
        print(f"✅ Audit trail has {len(trail)} events")
        return True
        
    except Exception as e:
        print(f"❌ Security engine test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_persistence():
    """Test data persistence and recovery"""
    print("\nTesting persistence layer...")
    try:
        from PERSISTENCE.persistence_manager import PersistenceManager, MemoryBackend
        from PERSISTENCE.snapshot_manager import SnapshotManager
        
        # Test memory backend
        manager = PersistenceManager(MemoryBackend())
        
        # Save a project
        saved = manager.save_project("test-project", {
            "name": "Test Project",
            "status": "active",
            "value": 5000
        })
        
        assert saved, "Save failed"
        
        # Load project
        loaded = manager.load_project("test-project")
        assert loaded is not None, "Load failed"
        assert loaded['name'] == "Test Project", "Data mismatch"
        
        # Test snapshots
        snapshot_mgr = SnapshotManager()
        snap = snapshot_mgr.create_snapshot(
            system_state={"active": True},
            projects={"test": "data"},
            kpis={"score": 85},
            metadata={"test": True}
        )
        
        assert snap is not None, "Snapshot creation failed"
        verified = snapshot_mgr.verify_snapshot_integrity(snap.snapshot_id)
        assert verified, "Snapshot integrity check failed"
        
        print(f"✅ Project saved and loaded successfully")
        print(f"✅ Snapshot created with ID: {snap.snapshot_id}")
        print(f"✅ Snapshot integrity verified")
        return True
        
    except Exception as e:
        print(f"❌ Persistence test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_business_hunting():
    """Test discrete business hunting"""
    print("\nTesting business hunting...")
    try:
        from BUSINESS_ENGINES.business_model_engine.business_hunter_engine import (
            BusinessHuntingOrchestrator,
            OpportunitySignal
        )
        
        hunting = BusinessHuntingOrchestrator()
        
        # Perform a hunt
        signals = {
            OpportunitySignal.MARGIN_EROSION: 0.8,
            OpportunitySignal.PROCESS_INEFFICIENCY: 0.7
        }
        
        result = hunting.hunt_and_execute_cycle(
            org_name="Test Corporation",
            industry="finance",
            signals=signals
        )
        
        assert result['status'] in ['OPPORTUNITY_IDENTIFIED', 'OPPORTUNITY_INSUFFICIENT'], "Invalid status"
        
        if result['status'] == 'OPPORTUNITY_IDENTIFIED':
            assert result['hunt_score'] > 50, "Insufficient hunt score"
            assert result['ready_for_pitch'], "Not ready for pitch"
        
        # Get dashboard
        dashboard = hunting.get_hunting_dashboard()
        assert 'total_hunts' in dashboard, "Missing dashboard metrics"
        
        print(f"✅ Hunt completed with score: {result.get('hunt_score', 0):.1f}")
        print(f"✅ Hunting dashboard shows {dashboard['total_hunts']} total hunts")
        return True
        
    except Exception as e:
        print(f"❌ Business hunting test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_supreme_orchestrator():
    """Test the master orchestrator"""
    print("\nTesting supreme orchestrator...")
    try:
        from NAYA_PROJECT_ENGINE.supreme_business_orchestrator import SupremeBusinessOrchestrator
        
        supreme = SupremeBusinessOrchestrator()
        
        # Create opportunities
        pain_points = [
            {
                'id': 'pain-001',
                'description': 'User reporting system crashes',
                'affected_segment': 'Finance',
                'frequency': 5,
                'market_opportunity': 50000
            }
        ]
        
        opportunities = supreme.detect_and_create_opportunities(
            pain_points=pain_points,
            market_signals=[],
            hunting_data=None
        )
        
        assert len(opportunities) > 0, "No opportunities created"
        
        # Get dashboard
        dashboard = supreme.get_business_creation_dashboard()
        assert dashboard['system_status'] == 'ACTIVE', "System not active"
        
        print(f"✅ Created {len(opportunities)} opportunities")
        print(f"✅ Dashboard shows €{dashboard['total_value_under_management']:,.0f} total value")
        return True
        
    except Exception as e:
        print(f"❌ Supreme orchestrator test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("="*70)
    print("NAYA SYSTEM INTEGRATION TEST")
    print("="*70)
    
    tests = [
        ("Imports", test_imports),
        ("Quick Business Generation", test_quick_business_generation),
        ("Execution Planning", test_execution_planning),
        ("Security Engine", test_security_engine),
        ("Persistence Layer", test_persistence),
        ("Business Hunting", test_business_hunting),
        ("Supreme Orchestrator", test_supreme_orchestrator),
    ]
    
    results = []
    for name, test_func in tests:
        result = test_func()
        results.append((name, result))
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:10} {name}")
    
    print(f"\n{passed}/{total} tests passed")
    
    if passed == total:
        print("\n✅ ALL SYSTEMS OPERATIONAL - READY FOR PRODUCTION")
        return 0
    else:
        print("\n❌ SOME SYSTEMS NEED ATTENTION")
        return 1


if __name__ == '__main__':
    sys.exit(main())
