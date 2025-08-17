from src.rules import run_all_rules

def test_rules_return_list():
    events = [{"operation": "Microsoft.KeyVault/vaults/secrets/get/action",
               "time": "2025-08-10T12:00:00Z",
               "caller": "alice@contoso.com",
               "resource": "/subscriptions/xxx/resourceGroups/rg/providers/Microsoft.KeyVault/vaults/kv"}]
    alerts = run_all_rules(events)
    assert isinstance(alerts, list)
    assert any(a["rule"] == "keyvault_secret_access" for a in alerts)