#!/usr/bin/env python3
"""Scan the repository for potentially unused Python code using vulture.

Usage:
  python scripts/find_unused.py [--report-type json|txt|csv] [--min-score SCORE] [path...]
  python scripts/find_unused.py --help

Exits with code 0 if no unused items found, 2 otherwise. Outputs report to stdout.
"""
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

try:
    from vulture import Vulture
except ImportError:
    print("Please install vulture: pip install vulture", file=sys.stderr)
    sys.exit(1)

EXCLUDE_DIRS = {'.git', '.venv', 'venv', '__pycache__', 'build', 'dist', '.egg-info'}
EXCLUDE_FILES = {'conftest.py', 'setup.py', '__init__.py'}

def collect_py_files(paths: List[str]) -> List[str]:
    """Collect all Python files from given paths."""
    files = []
    for p in paths:
        ppath = Path(p)
        if not ppath.exists():
            continue
        if ppath.is_file() and ppath.suffix == '.py':
            if ppath.name not in EXCLUDE_FILES:
                files.append(str(ppath))
        else:
            for f in ppath.rglob('*.py'):
                if not any(part in EXCLUDE_DIRS for part in f.parts):
                    if f.name not in EXCLUDE_FILES:
                        files.append(str(f))
    return sorted(set(files))

def generate_text_report(unused: List[Dict[str, Any]]) -> str:
    """Generate a human-readable text report."""
    if not unused:
        return "✓ No unused code found!"

    report = f"\n{'='*80}\n"
    report += f"UNUSED CODE REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"{'='*80}\n"
    report += f"Total issues found: {len(unused)}\n\n"

    by_file = {}
    for item in unused:
        fname = item['filename']
        if fname not in by_file:
            by_file[fname] = []
        by_file[fname].append(item)

    for fname in sorted(by_file.keys()):
        report += f"\n📄 {fname}\n"
        report += "-" * 80 + "\n"
        for item in by_file[fname]:
            report += f"  Line {item['first_lineno']:4d} | {item['type']:12s} | {item['name']:30s}"
            if item.get('score'):
                report += f" (score: {item['score']:.1f})"
            report += "\n"

    report += f"\n{'='*80}\n"
    return report

def generate_csv_report(unused: List[Dict[str, Any]]) -> str:
    """Generate a CSV-formatted report."""
    if not unused:
        return "filename,line_number,name,type,score\n"

    lines = ["filename,line_number,name,type,score"]
    for item in unused:
        line = f'{item["filename"]},{item["first_lineno"]},"{item["name"]}",{item["type"]},{item.get("score", "")}'
        lines.append(line)
    return "\n".join(lines)

def main(argv: List[str]) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Scan repository for unused Python code using Vulture"
    )
    parser.add_argument(
        'paths',
        nargs='*',
        default=['.'],
        help='Paths to scan (default: current directory)'
    )
    parser.add_argument(
        '--report-type',
        choices=['json', 'txt', 'csv'],
        default='json',
        help='Report format (default: json)'
    )
    parser.add_argument(
        '--min-score',
        type=float,
        default=0,
        help='Minimum score to report (default: 0)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Output file (default: stdout)'
    )

    args = parser.parse_args(argv[1:])

    # Collect Python files
    py_files = collect_py_files(args.paths)
    if not py_files:
        print('No Python files found.', file=sys.stderr)
        return 0

    print(f"Scanning {len(py_files)} Python files...", file=sys.stderr)

    # Run Vulture analysis
    v = Vulture()
    v.scavenge(py_files)

    unused = []
    for item in v.get_unused_code():
        score = getattr(item, 'score', 0)
        if score >= args.min_score:
            unused.append({
                'filename': item.filename,
                'first_lineno': item.first_lineno,
                'name': getattr(item, 'name', ''),
                'type': type(item).__name__,
                'score': score,
            })

    # Generate report
    if args.report_type == 'json':
        report = json.dumps(unused, indent=2, ensure_ascii=False)
    elif args.report_type == 'txt':
        report = generate_text_report(unused)
    elif args.report_type == 'csv':
        report = generate_csv_report(unused)
    else:
        report = json.dumps(unused, indent=2, ensure_ascii=False)

    # Output report
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved to {args.output}", file=sys.stderr)
    else:
        print(report)

    print(f"\nFound {len(unused)} unused items.", file=sys.stderr)
    return 0 if not unused else 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
