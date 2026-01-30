# Azure Security Monitor

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

Parses **Azure Activity Logs** and raises alerts for high-risk operations, starting with:
- **Elevated RBAC assignments** (e.g., Owner / User Access Administrator)
- **Key Vault secret access** operations (list/get)

This is a small, reproducible demo that highlights Python scripting, basic detection logic, and clean repo hygiene—cloud edition.

## 🛠️ Technologies Used
- **Python 3.8+** - Core language with modern type hints
- **pandas** - Data manipulation and CSV handling
- **Azure SDK** - Azure Identity and Monitor Query libraries
- **pytest** - Unit and integration testing
- **GitHub Actions** - Automated CI/CD pipeline

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

## ✨ Key Features & Highlights

**For Interview Discussions:**
- **Modular Architecture** - Separation of concerns with dedicated modules for parsing, rules, and alerts
- **Type Safety** - Full type hints throughout codebase for maintainability
- **Extensible Rule Engine** - Easy to add new detection rules by implementing simple Python functions
- **Multiple Output Formats** - CSV for data analysis, Markdown for human-readable summaries
- **CI/CD Integration** - Automated testing across multiple Python versions
- **Cloud Security Focus** - Addresses real-world Azure security monitoring challenges

**Design Decisions:**
- Kept detection logic simple and readable over complex pattern matching
- Used JSON input for easy integration with Azure exports and local testing
- Normalized heterogeneous log formats to consistent internal schema
- Included sample data for reproducibility without Azure credentials

## 📸 Example Output
CLI:
```bash
$ python -m src.main --input data/sample_activity_logs.json
[+] Events: 2  Alerts: 2
[+] Wrote alerts.csv and SUMMARY.md
```
Sample outputs are included in [data/sample_alerts.csv](data/sample_alerts.csv) and [data/sample_SUMMARY.md](data/sample_SUMMARY.md).

## 🚀 Potential Enhancements

This project demonstrates core security monitoring concepts. In a production environment, consider:

**Scalability & Performance:**
- Stream processing for real-time log ingestion (e.g., Azure Event Hubs)
- Database backend for alert history and trend analysis
- Parallel processing for large log volumes

**Enhanced Detection:**
- Machine learning for anomaly detection (unusual access patterns)
- Contextual rules (time-of-day, geolocation, user baseline behavior)
- Integration with threat intelligence feeds
- False positive reduction through allowlisting and tuning

**Operations & Integration:**
- Webhook/email notifications for critical alerts
- SIEM integration (Splunk, Sentinel, ELK)
- Dashboard visualization (Grafana, PowerBI)
- Alert deduplication and correlation
- Automated response actions (e.g., disable compromised accounts)

**Security Hardening:**
- Managed identity authentication instead of credentials
- Secrets management via Azure Key Vault
- Input validation and sanitization
- Audit logging of the monitor itself

