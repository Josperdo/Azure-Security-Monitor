import argparse
from pathlib import Path
from .parser import load_activity_logs
from .rules import run_all_rules
from .alerts import write_alerts_csv, write_summary_md

def parse_args():
    p = argparse.ArgumentParser(description="Azure Security Monitor")
    p.add_argument("--input", default=str(Path("data") / "sample_activity_logs.json"),
                   help="Path to Azure Activity Logs JSON")
    p.add_argument("--out-csv", default="alerts.csv")
    p.add_argument("--out-md", default="SUMMARY.md")
    return p.parse_args()

def main():
    args = parse_args()
    events = load_activity_logs(args.input)
    alerts = run_all_rules(events)
    write_alerts_csv(alerts, args.out_csv)
    write_summary_md(alerts, args.out_md)
    print(f"[+] Events: {len(events)}  Alerts: {len(alerts)}")
    print(f"[+] Wrote {args.out_csv} and {args.out_md}")

if __name__ == "__main__":
    main()