# Azure Security Monitor

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

Parses **Azure Activity Logs** and raises alerts for high-risk operations, starting with:
- **Elevated RBAC assignments** (e.g., Owner / User Access Administrator)
- **Key Vault secret access** operations (list/get)

This is a small, reproducible demo that highlights Python scripting, basic detection logic, and clean repo hygiene—cloud edition.

---

## 🚀 Quick Start

1) **Clone**
```bash
git clone https://github.com/Josperdo/Azure-Security-Monitor.git
cd Azure-Security-Monitor
```

2) Create & activate a virtual environment
```bash
# Windows PowerShell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3) Install dependencies
```bash
pip install -r requirements.txt
```

4) Run on the included sample data
```bash
python -m src.main --input data/sample_activity_logs.json
```

## 📂 Project Structure
```bash
Azure-Security-Monitor/
├── src/
│   ├── __init__.py
│   ├── main.py        # CLI: parser -> rules -> alerts
│   ├── parser.py      # Load/normalize Azure Activity Logs
│   ├── rules.py       # Detection rules (RBAC, Key Vault, etc.)
│   └── alerts.py      # Outputs: alerts.csv + SUMMARY.md
├── tests/
│   ├── conftest.py    # Adds src/ to import path for pytest/CI
│   ├── test_parser.py # Sample data parse test
│   └── test_rules.py  # Rule sanity tests
├── data/
│   ├── sample_activity_logs.json
│   ├── sample_alerts.csv     # Example output
│   └── sample_SUMMARY.md     # Example summary
├── requirements.txt
├── .gitignore
├── .github/workflows/ci.yml   # (Optional) CI for tests
└── README.md
```

## 🔍 Detections

### Elevated RBAC Assignment
- Triggers on Microsoft.Authorization/roleAssignments/write.
- Flags lines that indicate high-privilege roles like Owner or User Access Administrator.
### Key Vault Secret Access
- Triggers on:
  - Microsoft.KeyVault/vaults/secrets/get/action
  - Microsoft.KeyVault/vaults/secrets/list/action
- Flags successful access events as a visibility aid (expandable with allowlists).

## 📸 Example Output
CLI:
```bash
$ python -m src.main --input data/sample_activity_logs.json
[+] Events: 2  Alerts: 2
[+] Wrote alerts.csv and SUMMARY.md
```
Sample outputs are included in [data/sample_alerts.csv](data/sample_alerts.csv) and [data/sample_SUMMARY.md](data/sample_SUMMARY.md).

