"""
Azure Activity Log Parser.

Loads and normalizes Azure Activity Logs from JSON exports into a consistent format
for downstream rule evaluation.
"""
from __future__ import annotations
from typing import List, Dict, Any
import json


def load_activity_logs(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    # Accept eitehr an object of "value" (Azure export) or a plain list
    if isinstance(raw, dict) and "value" in raw:
        events = raw["value"]
    else:
        events = raw
    # Normalize minimal fields we need
    norm = []
    for e in events:
        props = e.get("properties", {}) or {}
        norm.append({
            "time": e.get("eventTimestamp") or props.get("eventTimestamp") or e.get("time"),
            "operation": e.get("operationName", {}).get("value") or e.get("operationName") or props.get("operationName"),
            "category": e.get("category", {}).get("value") or e.get("category") or props.get("category"),
            "status": props.get("status") or e.get("status"),
            "caller": props.get("caller") or e.get("caller") or (e.get("claims", {}) or {}).get("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"),
            "resource": (e.get("resourceId") or props.get("resourceId") or e.get("resourceUri")),
            "claims": e.get("claims") or {},
        })
    return norm