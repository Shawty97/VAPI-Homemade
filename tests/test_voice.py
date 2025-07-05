import asyncio
from services import audio_service, llm_service


async def run_pipeline() -> bytes:
    transcript = await audio_service.transcribe(b"audio", {})
    response = await llm_service.generate_response(transcript, {})
    audio = await audio_service.synthesize(response, {})
    return audio


def test_voice_pipeline() -> None:
    audio = asyncio.run(run_pipeline())
    assert audio.startswith(b"LLM response")
