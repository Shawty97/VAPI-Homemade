import structlog
import time
from typing import Any, Dict

from prometheus_client import Summary

from services import audio_service, llm_service, ultra_low_latency_service

logger = structlog.get_logger()

pipeline_latency = Summary("pipeline_latency_ms", "Latency of full voice pipeline in ms")


async def run_pipeline(audio_data: bytes, config: Dict[str, Any] | None = None) -> bytes:
    """Run STT -> LLM -> TTS pipeline and return synthesized audio."""
    config = config or {}
    start = time.perf_counter()
    text = await audio_service.transcribe(audio_data, config)
    await ultra_low_latency_service.optimize()
    response = await llm_service.generate_response(text, config)
    audio = await audio_service.synthesize(response, config)
    pipeline_latency.observe((time.perf_counter() - start) * 1000)
    logger.info("pipeline_completed")
    return audio
