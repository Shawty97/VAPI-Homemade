from fastapi.testclient import TestClient
from app import app
import os

client = TestClient(app)


def test_outbound_call_authorized() -> None:
    os.environ["API_KEY"] = "testkey"
    resp = client.post(
        "/api/outbound-call",
        headers={"X-API-Key": "testkey"},
        json={"to_number": "+1234567890"},
    )
    assert resp.status_code == 200
    assert resp.json() == {"status": "initiated"}


def test_outbound_call_unauthorized() -> None:
    os.environ["API_KEY"] = "testkey"
    resp = client.post(
        "/api/outbound-call",
        headers={"X-API-Key": "wrong"},
        json={"to_number": "+1234567890"},
    )
    assert resp.status_code == 401
