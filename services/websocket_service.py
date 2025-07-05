from fastapi import WebSocket
import structlog
import time
from typing import Set

from prometheus_client import Gauge, Summary
from services import audio_service, llm_service, ultra_low_latency_service

connections_gauge = Gauge("active_websockets", "Number of active websocket connections")
stt_latency_summary = Summary("stt_latency_ms", "Latency of STT in ms")

logger = structlog.get_logger()

active_connections: Set[WebSocket] = set()


async def handle_websocket(ws: WebSocket) -> None:
    await ws.accept()
    active_connections.add(ws)
    connections_gauge.set(len(active_connections))
    logger.info("websocket_connected", active=len(active_connections))
    try:
        while True:
            data = await ws.receive_bytes()
            start = time.perf_counter()
            text = await audio_service.transcribe(data, {})
            stt_latency_summary.observe((time.perf_counter() - start) * 1000)
            await ultra_low_latency_service.optimize()
            response_text = await llm_service.generate_response(text, {})
            audio = await audio_service.synthesize(response_text, {})
            await ws.send_bytes(audio)
    except Exception as e:  # pragma: no cover - simple example
        logger.error("websocket_error", error=str(e))
    finally:
        active_connections.discard(ws)
        connections_gauge.set(len(active_connections))
        await ws.close()
        logger.info("websocket_disconnected", active=len(active_connections))
