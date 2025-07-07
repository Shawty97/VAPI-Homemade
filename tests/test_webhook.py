from fastapi.testclient import TestClient
from app import app
import os

client = TestClient(app)


def test_webhook_endpoint() -> None:
    os.environ["API_KEY"] = "testkey"
    resp = client.post(
        "/api/webhook",
        headers={"X-API-Key": "testkey"},
        json={"type": "test", "payload": {"msg": "hello"}},
    )
    assert resp.status_code == 200
    assert resp.json() == {"status": "received"}
