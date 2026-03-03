"""
NAYA_CORE Cleanup Script

Removes NayaCore/ folder (incorrect casing + duplicate)
Removes stub/empty files in NAYA_CORE/ subdirectories
Validates the final structure

Run this ONCE to clean up the system.
"""

import os
import shutil
from pathlib import Path


def remove_directory(path: str) -> bool:
    """Remove a directory and all its contents."""
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"✓ Removed: {path}")
            return True
        else:
            print(f"⚠ Not found: {path}")
            return False
    except Exception as e:
        print(f"✗ Error removing {path}: {e}")
        return False


def remove_file(path: str) -> bool:
    """Remove a file."""
    try:
        if os.path.exists(path):
            os.remove(path)
            print(f"✓ Removed: {path}")
            return True
        else:
            print(f"⚠ Not found: {path}")
            return False
    except Exception as e:
        print(f"✗ Error removing {path}: {e}")
        return False


def is_stub_file(filepath: str) -> bool:
    """Check if a file is a stub (empty or only contains TODO)."""
    try:
        with open(filepath, 'r') as f:
            content = f.read().strip()
            # Check for stub patterns
            if not content or len(content) < 50:
                return True
            if "Auto-generated stub" in content:
                return True
            if "TODO: Implement" in content and len(content) < 200:
                return True
            return False
    except:
        return False


def cleanup_naya_core():
    """Main cleanup operation."""
    
    print("\n" + "="*60)
    print("NAYA_CORE CLEANUP OPERATION")
    print("="*60 + "\n")
    
    naya_root = "c:\\NAYA"
    naya_core = os.path.join(naya_root, "NAYA_CORE")
    naya_core_wrong = os.path.join(naya_root, "NayaCore")
    
    # Step 1: Remove NayaCore/ directory (wrong casing)
    print("\n[1/3] Removing NayaCore/ (incorrect casing)...")
    remove_directory(naya_core_wrong)
    
    # Step 2: Clean up stub files in NAYA_CORE
    print("\n[2/3] Removing stub/empty files in NAYA_CORE/...")
    
    stub_count = 0
    for root, dirs, files in os.walk(naya_core):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                filepath = os.path.join(root, file)
                if is_stub_file(filepath):
                    print(f"  ⚠ Stub detected: {filepath}")
                    # Don't delete yet, just log
                    stub_count += 1
    
    if stub_count > 0:
        print(f"\n  Found {stub_count} stub files. Review before deletion.")
    
    # Step 3: Validate final structure
    print("\n[3/3] Validating NAYA_CORE structure...")
    
    required_files = [
        "NAYA_CORE/__init__.py",
        "NAYA_CORE/STRUCTURE.md",
        "NAYA_CORE/decision/decision_core.py",
        "NAYA_CORE/decision/strategic_domain_router.py",
        "NAYA_CORE/economic/capital_reserve_manager.py",
        "NAYA_CORE/doctrine/core_constitution.py",
    ]
    
    validated = []
    for file_path in required_files:
        full_path = os.path.join(naya_root, file_path)
        if os.path.exists(full_path):
            print(f"  ✓ {file_path}")
            validated.append(True)
        else:
            print(f"  ✗ MISSING: {file_path}")
            validated.append(False)
    
    print("\n" + "="*60)
    if all(validated) and not os.path.exists(naya_core_wrong):
        print("✓ NAYA_CORE CLEANUP COMPLETE & VALIDATED")
    else:
        print("⚠ NAYA_CORE has issues - review above")
    print("="*60 + "\n")


if __name__ == "__main__":
    cleanup_naya_core()
