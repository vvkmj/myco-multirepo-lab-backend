import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data

def test_status_endpoint_schema():
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "order-processor"
    assert data["version"] == "1.4.0"
    assert data["status"] == "operational"
    assert "dependencies" in data
    assert data["dependencies"]["database"] == "connected"
    assert data["dependencies"]["cache"] == "connected"
    assert isinstance(data["uptime_seconds"], int)
    assert data["uptime_seconds"] >= 0
    assert data["environment"] == "production"

def test_frontend_contract_compatibility():
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    data = response.json()
    # Contract fields required by myco-multirepo-lab-frontend App.jsx:
    required_frontend_fields = ["service", "version", "status", "dependencies", "uptime_seconds"]
    for field in required_frontend_fields:
        assert field in data, f"Missing required frontend contract field: {field}"

