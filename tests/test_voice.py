import asyncio
from services.pipeline_service import run_pipeline


def test_voice_pipeline() -> None:
    audio = asyncio.run(run_pipeline(b"audio"))
    assert audio.startswith(b"LLM response")
