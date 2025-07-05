from fastapi import WebSocket
import structlog

logger = structlog.get_logger()


async def handle_websocket(ws: WebSocket) -> None:
    await ws.accept()
    logger.info("websocket_connected")
    try:
        while True:
            data = await ws.receive_bytes()
            await ws.send_bytes(data)
    except Exception as e:  # pragma: no cover - simple example
        logger.error("websocket_error", error=str(e))
    finally:
        await ws.close()
        logger.info("websocket_disconnected")
