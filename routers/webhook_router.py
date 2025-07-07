from fastapi import APIRouter, Depends
from pydantic import BaseModel

from services.webhook_service import handle_webhook
from services.security import verify_api_key

router = APIRouter(prefix="/api")

class WebhookEvent(BaseModel):
    type: str
    payload: dict | None = None

@router.post("/webhook")
async def webhook(event: WebhookEvent, _: None = Depends(verify_api_key)) -> dict:
    await handle_webhook(event.dict())
    return {"status": "received"}
