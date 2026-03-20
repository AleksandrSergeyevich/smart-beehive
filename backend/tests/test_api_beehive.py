from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_get_beehive_status_ok():
    response = client.get("/api/v1/beehives/1/status")
    assert response.status_code == 200
    data = response.json()
    assert "temperature" in data
    assert "humidity" in data
    assert "weight" in data


def test_get_beehive_status_not_found():
    response = client.get("/api/v1/beehives/999/status")
    assert response.status_code == 404


def test_list_beehives():
    response = client.get("/api/v1/beehives/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
