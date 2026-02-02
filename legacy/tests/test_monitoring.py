import json
import os

def test_grafana_dashboard_exists():
    path = "monitoring/grafana/dashboards/gateway_overview.json"
    assert os.path.exists(path), f"Dashboard file not found at {path}"

def test_grafana_dashboard_is_valid_json():
    path = "monitoring/grafana/dashboards/gateway_overview.json"
    with open(path, "r") as f:
        data = json.load(f)
    assert data["title"] == "Gateway Overview"
    assert data["uid"] == "gateway-overview"

def test_grafana_provisioning_config():
    path = "monitoring/grafana/provisioning/dashboards/dashboard.yml"
    assert os.path.exists(path)
    with open(path, "r") as f:
        content = f.read()
    assert "/var/lib/grafana/dashboards" in content
