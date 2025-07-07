from fastapi.testclient import TestClient
from app import app
import os

client = TestClient(app)


def test_rtc_endpoint() -> None:
    os.environ["API_KEY"] = "testkey"
    resp = client.post(
        "/api/rtc",
        headers={"X-API-Key": "testkey"},
        json={"sdp": "offer", "type": "offer"},
    )
    assert resp.status_code == 200
    assert resp.json()["type"] == "answer"
