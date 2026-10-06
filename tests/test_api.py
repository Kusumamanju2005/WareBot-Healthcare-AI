from fastapi.testclient import TestClient

from src.api import app


client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction():
    response = client.post(
        "/predict",
        json={"text": "I have high temperature"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["text"] == "I have high temperature"
    assert "intent" in data
    assert isinstance(data["intent"], str)


def test_empty_text():
    response = client.post(
        "/predict",
        json={"text": ""},
    )

    assert response.status_code == 200
    assert response.json()["intent"] == "general_query"