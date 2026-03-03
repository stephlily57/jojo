#!/usr/bin/env python3
"""NAYA System Audit - Analyzes actual state vs intended architecture.

Checks:
1. Module dependencies and connections
2. Import errors
3. Missing files/modules
4. Bootstrap readiness
5. Critical system paths

Generates a GAP REPORT showing what works vs what's missing.
"""
import sys
import os
import json
import ast
import importlib.util
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Any

# Add project root
ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# ====================================================================
# ANALYSIS ENGINE
# ====================================================================

class DependencyAnalyzer:
    """Scans all Python files and extracts import statements."""

    def __init__(self, root_path: Path):
        self.root = root_path
        self.py_files = []
        self.imports = defaultdict(list)  # file -> list of imports
        self.errors = []
        self.missing_modules = set()

    def scan_files(self):
        """Collect all Python files."""
        exclude_dirs = {'.git', '.venv', 'venv', '__pycache__', 'build', 'dist', '.egg-info', 'NAYA.egg-info'}

        for py_file in self.root.rglob('*.py'):
            # Skip excluded dirs
            if any(part in exclude_dirs for part in py_file.parts):
                continue
            self.py_files.append(py_file)

    def extract_imports(self):
        """Extract all import statements from Python files."""
        for py_file in self.py_files:
            try:
                with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                tree = ast.parse(content)

                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            self.imports[str(py_file)].append({
                                'type': 'import',
                                'module': alias.name,
                                'lineno': node.lineno
                            })
                    elif isinstance(node, ast.ImportFrom):
                        module = node.module or ''
                        for alias in node.names:
                            self.imports[str(py_file)].append({
                                'type': 'from',
                                'module': module,
                                'name': alias.name,
                                'lineno': node.lineno
                            })
            except Exception as e:
                self.errors.append({
                    'file': str(py_file),
                    'error': str(e)
                })

    def check_imports(self):
        """Check which imports are resolvable."""
        unresolvable = []

        for file_path, imports in self.imports.items():
            for imp in imports:
                module_name = imp['module']

                # Skip built-in and relative imports for now
                if module_name in sys.builtin_module_names:
                    continue
                if module_name.startswith('.'):
                    continue

                # Check if module is in project
                is_project_module = self._is_project_module(module_name)

                if not is_project_module:
                    try:
                        # Try to import
                        importlib.util.find_spec(module_name)
                    except (ImportError, ModuleNotFoundError, ValueError):
                        unresolvable.append({
                            'file': file_path,
                            'module': module_name,
                            'import_line': imp['lineno'],
                            'type': imp['type']
                        })
                        self.missing_modules.add(module_name)

        return unresolvable

    def _is_project_module(self, module_name: str) -> bool:
        """Check if a module is part of the NAYA project."""
        top_level = module_name.split('.')[0]

        # Check if it's a top-level project folder
        if (self.root / top_level).is_dir():
            return True
        if (self.root / top_level).with_suffix('.py').is_file():
            return True

        return False


class ArchitectureValidator:
    """Validates that the architecture matches the design."""

    REQUIRED_MODULES = {
        'NAYA Core': ['NAYA_CORE', 'KERNEL'],
        'NAYA Business': ['BUSINESS_ENGINES', 'EVOLUTION_SYSTEM', 'EXECUTIVE_ARCHITECTURE'],
        'NAYA Security': ['REAPERS'],
        'Data Layer': ['DATA_GOVERNANCE', 'PERSISTENCE', 'VERSION_CONTROL'],
        'Distributed': ['DISTRIBUTED_LAYER', 'GLOBAL_SYNC'],
        'Bootstrap': ['bootstrap'],
        'Communication': ['NAYA_EVENT_STREAM', 'NAYA_COMMAND_GATEAWAY'],
        'Governance': ['CONSTITUTION'],
    }

    def __init__(self, root_path: Path):
        self.root = root_path
        self.status = {}

    def validate(self) -> Dict[str, Any]:
        """Check if all required modules exist."""
        result = {
            'present': {},
            'missing': {},
            'partial': {}
        }

        for system_name, modules in self.REQUIRED_MODULES.items():
            all_present = True
            partial_present = []
            missing = []

            for module in modules:
                module_path = self.root / module
                if module_path.is_dir() or module_path.with_suffix('.py').is_file():
                    partial_present.append(module)
                else:
                    all_present = False
                    missing.append(module)

            if all_present:
                result['present'][system_name] = modules
            elif partial_present:
                result['partial'][system_name] = {
                    'present': partial_present,
                    'missing': missing
                }
            else:
                result['missing'][system_name] = modules

        return result


class BootstrapValidator:
    """Checks if the bootstrap system is operational."""

    def __init__(self, root_path: Path):
        self.root = root_path
        self.issues = []

    def validate(self) -> Dict[str, Any]:
        """Check bootstrap readiness."""
        result = {
            'bootstrap_files': [],
            'entry_points': [],
            'activation_ready': False,
            'blockers': []
        }

        # Check bootstrap files
        bootstrap_files = {
            'bootstrap/bootstrap_unified.py': 'Universal bootstrapper',
            'bootstrap/cloudrun_initializer.py': 'Cloud Run support',
            'bootstrap/vm_initializer.py': 'VM support',
            'bootstrap/local_initializer.py': 'Local mode',
            'naya_activation_universelle.py': 'Main activation',
            'boot_dashboard.py': 'Dashboard boot',
        }

        for file_path, description in bootstrap_files.items():
            full_path = self.root / file_path
            if full_path.exists():
                result['bootstrap_files'].append({
                    'file': file_path,
                    'status': 'present',
                    'description': description
                })
            else:
                result['bootstrap_files'].append({
                    'file': file_path,
                    'status': 'missing',
                    'description': description
                })
                result['blockers'].append(f"Missing: {file_path}")

        # Try to import main modules
        entry_points = [
            'naya_activation_universelle',
            'boot_dashboard',
            'bootstrap.bootstrap_unified',
        ]

        for ep in entry_points:
            try:
                importlib.util.find_spec(ep)
                result['entry_points'].append({
                    'module': ep,
                    'status': 'importable'
                })
            except:
                result['entry_points'].append({
                    'module': ep,
                    'status': 'import_error'
                })
                result['blockers'].append(f"Cannot import: {ep}")

        result['activation_ready'] = len(result['blockers']) == 0

        return result


# ====================================================================
# REPORT GENERATOR
# ====================================================================

def generate_gap_report(root: Path) -> str:
    """Generate comprehensive GAP report."""

    report = []
    report.append("=" * 80)
    report.append("NAYA SYSTEM AUDIT - GAP REPORT")
    report.append("=" * 80)

    # 1. Architecture Validation
    report.append("\n[1] ARCHITECTURE VALIDATION")
    report.append("-" * 80)

    arch_validator = ArchitectureValidator(root)
    arch_result = arch_validator.validate()

    report.append(f"\nPresent Systems ({len(arch_result['present'])}):")
    for system, modules in arch_result['present'].items():
        report.append(f"  ✓ {system}: {', '.join(modules)}")

    if arch_result['partial']:
        report.append(f"\nPartial Systems ({len(arch_result['partial'])}):")
        for system, info in arch_result['partial'].items():
            report.append(f"  ~ {system}")
            report.append(f"      Present: {', '.join(info['present'])}")
            report.append(f"      Missing: {', '.join(info['missing'])}")

    if arch_result['missing']:
        report.append(f"\nMissing Systems ({len(arch_result['missing'])}):")
        for system, modules in arch_result['missing'].items():
            report.append(f"  ✗ {system}: {', '.join(modules)}")

    # 2. Dependency Analysis
    report.append("\n[2] DEPENDENCY ANALYSIS")
    report.append("-" * 80)

    analyzer = DependencyAnalyzer(root)
    analyzer.scan_files()
    analyzer.extract_imports()
    unresolvable = analyzer.check_imports()

    report.append(f"Total Python files: {len(analyzer.py_files)}")
    report.append(f"Total import statements: {sum(len(v) for v in analyzer.imports.values())}")
    report.append(f"Unresolvable imports: {len(unresolvable)}")

    if unresolvable:
        report.append("\nUnresolvable Imports (Critical Issues):")
        by_module = defaultdict(list)
        for item in unresolvable:
            by_module[item['module']].append(item)

        for module in sorted(by_module.keys()):
            issues = by_module[module]
            report.append(f"\n  Missing: {module} (referenced in {len(issues)} places)")
            for issue in issues[:3]:  # Show first 3
                report.append(f"    - {issue['file'].replace(str(root), '.')}:{issue['import_line']}")
            if len(issues) > 3:
                report.append(f"    - ... and {len(issues) - 3} more")

    if analyzer.errors:
        report.append(f"\nParse Errors: {len(analyzer.errors)}")
        for error in analyzer.errors[:5]:
            report.append(f"  {error['file'].replace(str(root), '.')}: {error['error'][:60]}")

    # 3. Bootstrap Readiness
    report.append("\n[3] BOOTSTRAP READINESS")
    report.append("-" * 80)

    bootstrap_validator = BootstrapValidator(root)
    bootstrap_result = bootstrap_validator.validate()

    present_count = sum(1 for f in bootstrap_result['bootstrap_files'] if f['status'] == 'present')
    report.append(f"Bootstrap files: {present_count}/{len(bootstrap_result['bootstrap_files'])} present")

    if bootstrap_result['blockers']:
        report.append(f"\nACTIVATION BLOCKERS ({len(bootstrap_result['blockers'])}):")
        for blocker in bootstrap_result['blockers']:
            report.append(f"  ✗ {blocker}")
    else:
        report.append(f"\n✓ ACTIVATION READY - NO BLOCKERS")

    # 4. Final Verdict
    report.append("\n" + "=" * 80)
    report.append("VERDICT")
    report.append("=" * 80)

    total_missing_systems = len(arch_result['missing'])
    total_partial_systems = len(arch_result['partial'])
    total_import_errors = len(unresolvable)
    activation_ready = bootstrap_result['activation_ready']

    if activation_ready and total_missing_systems == 0 and total_import_errors == 0:
        report.append("\n✓ SYSTEM COMPLETE - Ready for activation")
        report.append("  Status: PASS")
    else:
        report.append("\n✗ SYSTEM INCOMPLETE - Needs work")
        report.append(f"  Missing systems: {total_missing_systems}")
        report.append(f"  Partial systems: {total_partial_systems}")
        report.append(f"  Import errors: {total_import_errors}")
        report.append(f"  Activation blockers: {len(bootstrap_result['blockers'])}")
        report.append("  Status: FAIL")

    report.append("\n" + "=" * 80)

    return "\n".join(report)


def main():
    """Main entry point."""
    import io
    import sys

    # Force UTF-8 encoding for output
    if sys.stdout.encoding and 'utf' not in sys.stdout.encoding.lower():
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    report = generate_gap_report(ROOT)
    print(report)

    # Save report
    reports_dir = ROOT / 'reports'
    reports_dir.mkdir(exist_ok=True)

    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = reports_dir / f'system_audit_{timestamp}.txt'
    report_file.write_text(report, encoding='utf-8')

    print(f"\nReport saved: {report_file}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
