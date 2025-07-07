from fastapi.testclient import TestClient
from app import app
import os

client = TestClient(app)


def test_voice_pipeline_api() -> None:
    os.environ["API_KEY"] = "testkey"
    resp = client.post(
        "/api/voice-pipeline",
        headers={"X-API-Key": "testkey"},
        files={"file": ("audio.wav", b"audio", "audio/wav")},
    )
    assert resp.status_code == 200
    assert resp.content.startswith(b"LLM response")
