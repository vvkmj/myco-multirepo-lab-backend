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
