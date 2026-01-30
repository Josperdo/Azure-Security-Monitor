"""
Alert output formatting and file generation.

Handles writing detected alerts to CSV and Markdown summary files.
"""
from typing import List, Dict


def write_alerts_csv(alerts: List[Dict], path: str = "alerts.csv") -> None:
    import csv
    fields = sorted({k for a in alerts for k in a.keys()}) if alerts else ["rule","time","caller","resource"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for a in alerts:
            w.writerow(a)

def write_summary_md(alerts: List[Dict], path: str = "SUMMARY.md") -> None:
    by_rule = {}
    for a in alerts:
        by_rule[a["rule"]] = by_rule.get(a["rule"], 0) + 1
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Azure Security Monitor — Summary\n\n")
        if not alerts:
            f.write("No alerts generated.\n")
            return
        for r, n in sorted(by_rule.items(), key=lambda x: x[0]):
            f.write(f"- **{r}**: {n}\n")