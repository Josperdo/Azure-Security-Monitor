"""
Azure Security Monitor - Main CLI entry point.

Orchestrates log parsing, rule execution, and alert generation for Azure Activity Logs.
"""
import argparse
from pathlib import Path
from .parser import load_activity_logs
from .rules import run_all_rules
from .alerts import write_alerts_csv, write_summary_md


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the Azure Security Monitor CLI."""
    p = argparse.ArgumentParser(description="Azure Security Monitor")
    p.add_argument("--input", default=str(Path("data") / "sample_activity_logs.json"),
                   help="Path to Azure Activity Logs JSON")
    p.add_argument("--out-csv", default="alerts.csv",
                   help="Output path for CSV alerts file")
    p.add_argument("--out-md", default="SUMMARY.md",
                   help="Output path for Markdown summary file")
    return p.parse_args()


def main() -> None:
    """Main execution function: load logs, run rules, generate alerts."""
    args = parse_args()
    events = load_activity_logs(args.input)
    alerts = run_all_rules(events)
    write_alerts_csv(alerts, args.out_csv)
    write_summary_md(alerts, args.out_md)
    print(f"[+] Events: {len(events)}  Alerts: {len(alerts)}")
    print(f"[+] Wrote {args.out_csv} and {args.out_md}")


if __name__ == "__main__":
    main()