from fastapi import FastAPI
import structlog

from routers.health import router as health_router
from routers.websocket_router import router as websocket_router

logger = structlog.get_logger()

app = FastAPI(title="VAPI-Homemade")

@app.on_event("startup")
async def startup_event() -> None:
    logger.info("startup")

app.include_router(health_router)
app.include_router(websocket_router)


