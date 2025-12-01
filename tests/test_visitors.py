from datetime import datetime

from fastapi.testclient import TestClient

from siscadv.main import app


client = TestClient(app)


def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_register_and_list_visitor():
    payload = {
        "name": "Maria Silva",
        "document": "ID123456",
        "purpose": "Reunião",
    }

    post_response = client.post("/visitors", json=payload)
    assert post_response.status_code == 201
    created = post_response.json()

    assert created["name"] == payload["name"]
    assert created["document"] == payload["document"]
    assert created["purpose"] == payload["purpose"]
    assert datetime.fromisoformat(created["registered_at"]) <= datetime.utcnow()

    list_response = client.get("/visitors")
    assert list_response.status_code == 200
    visitors = list_response.json()
    assert len(visitors) >= 1
    assert any(v["document"] == payload["document"] for v in visitors)
