#!/usr/bin/env python3
"""Code quality check pipeline for NAYA project.

Integrates multiple code quality tools:
- Unused code detection (vulture)
- Summary statistics
- Report generation

Usage:
  python scripts/code_quality_check.py [--report-type txt|json|csv] [--save-report]
"""
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

def run_find_unused(report_type: str = 'json') -> Dict[str, Any]:
    """Run the find_unused.py script."""
    script_path = Path(__file__).parent / 'find_unused.py'

    try:
        result = subprocess.run(
            [sys.executable, str(script_path), '--report-type', report_type, '.'],
            capture_output=True,
            text=True,
            timeout=120
        )

        if report_type == 'json':
            try:
                data = json.loads(result.stdout)
                return {
                    'success': True,
                    'data': data,
                    'count': len(data)
                }
            except json.JSONDecodeError:
                return {
                    'success': False,
                    'error': result.stderr,
                    'data': []
                }
        else:
            return {
                'success': True,
                'data': result.stdout,
                'count': len(result.stdout.split('\n'))
            }
    except subprocess.TimeoutExpired:
        return {'success': False, 'error': 'Scan timeout', 'data': []}
    except Exception as e:
        return {'success': False, 'error': str(e), 'data': []}

def generate_summary(unused_data: List[Dict]) -> str:
    """Generate a summary of code quality metrics."""
    if not unused_data:
        return "✓ Code quality excellent - no unused code detected!"

    # Group by type
    by_type = {}
    total_score = 0
    for item in unused_data:
        item_type = item.get('type', 'Unknown')
        score = item.get('score', 0) or 0
        if item_type not in by_type:
            by_type[item_type] = {'count': 0, 'score': 0}
        by_type[item_type]['count'] += 1
        by_type[item_type]['score'] += score
        total_score += score

    # Format summary
    summary = "\n" + "="*80 + "\n"
    summary += "CODE QUALITY SUMMARY\n"
    summary += "="*80 + "\n"
    summary += f"Total unused items: {len(unused_data)}\n"
    summary += f"Total quality score: {total_score:.1f}\n\n"
    summary += "Breakdown by type:\n"
    summary += "-"*80 + "\n"

    for item_type in sorted(by_type.keys()):
        info = by_type[item_type]
        summary += f"  {item_type:20s}: {info['count']:3d} items (score: {info['score']:6.1f})\n"

    summary += "="*80 + "\n"
    return summary

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Code quality check pipeline")
    parser.add_argument('--report-type', choices=['txt', 'json', 'csv'], default='txt')
    parser.add_argument('--save-report', action='store_true', help='Save report to file')

    args = parser.parse_args()

    print("Running code quality checks...\n", file=sys.stderr)

    # Run scan
    result = run_find_unused(args.report_type)

    if not result['success']:
        print(f"Error: {result.get('error', 'Unknown error')}", file=sys.stderr)
        return 1

    # Output report
    if args.report_type == 'txt' or args.report_type == 'json':
        if isinstance(result['data'], list):
            # JSON data - generate text output
            print(generate_summary(result['data']))
            print(json.dumps(result['data'], indent=2, ensure_ascii=False))
        else:
            # Already formatted text
            print(result['data'])
    else:
        print(result['data'])

    # Save if requested
    if args.save_report:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = Path('reports') / f'code_quality_{timestamp}.txt'
        report_file.parent.mkdir(exist_ok=True)

        if isinstance(result['data'], list):
            content = generate_summary(result['data'])
            content += "\n" + json.dumps(result['data'], indent=2, ensure_ascii=False)
        else:
            content = result['data']

        report_file.write_text(content, encoding='utf-8')
        print(f"\nReport saved: {report_file}", file=sys.stderr)

    return 0

if __name__ == '__main__':
    sys.exit(main())
