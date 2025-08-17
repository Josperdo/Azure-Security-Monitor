from __future__ import annotations
from typing import List, Dict

def rule_elevated_rbac_assignment(events: List[Dict]) -> List[Dict]:
    """Flag assignments of Owner/User Access Administrator roles."""
    hits = []
    keywords = {"Microsoft.Authorization/roleAssignments/write"}
    elevated_names = {"Owner", "User Access Administrator"}
    for e in events:
        if e.get("operation") in keywords:
            # naive pull from claims or properties; leave simple for now
            caller = e.get("caller") or "unknown"
            # minimal: if the log line mentions elevated roles
            msg = str(e)
            if any(name in msg for name in elevated_names):
                hits.append({"rule": "elevated_rbac_assignment", "time": e.get("time"), "caller": caller, "resource": e.get("resource")})
    return hits

def rule_keyvault_secret_ops(events: List[Dict]) -> List[Dict]:
    """Flag Key Vault secret/list/get operations (could expand later)."""
    hits = []
    suspicious_ops = {
        "Microsoft.KeyVault/vaults/secrets/get/action",
        "Microsoft.KeyVault/vaults/secrets/list/action",
    }
    for e in events:
        if e.get("operation") in suspicious_ops and (e.get("status") in (None, "Succeeded", "Success")):
            hits.append({"rule": "keyvault_secret_access", "time": e.get("time"), "caller": e.get("caller"), "resource": e.get("resource")})
    return hits

def run_all_rules(events: List[Dict]) -> List[Dict]:
    alerts = []
    for fn in (rule_elevated_rbac_assignment, rule_keyvault_secret_ops):
        alerts.extend(fn(events))
    return alerts