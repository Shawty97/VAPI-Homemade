from fastapi import FastAPI, Response
import structlog
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from routers.health import router as health_router
from routers.websocket_router import router as websocket_router
from routers.call_router import router as call_router

logger = structlog.get_logger()


app = FastAPI(title="VAPI-Homemade")

@app.on_event("startup")
async def startup_event() -> None:
    logger.info("startup")

app.include_router(health_router)
app.include_router(websocket_router)
app.include_router(call_router)


@app.get("/metrics")
async def metrics() -> Response:
    """Prometheus metrics endpoint."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


