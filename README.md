# Azure Security Monitor

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
│   └── sample_activity_logs.json
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
alerts.csv (truncated):
```bash
rule,time,caller,resource
keyvault_secret_access,2025-08-10T12:00:00Z,alice@contoso.com,/subscriptions/xxx/.../vaults/kv
elevated_rbac_assignment,2025-08-10T12:05:00Z,bob@contoso.com,/subscriptions/xxx
```

