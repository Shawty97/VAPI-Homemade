from fastapi import APIRouter
import structlog

logger = structlog.get_logger()

router = APIRouter()


@router.get("/health")
async def health() -> dict:
    logger.info("health_check")
    return {"status": "healthy"}
