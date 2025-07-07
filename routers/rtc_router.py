from fastapi import APIRouter, Depends
from pydantic import BaseModel

from services.webrtc_service import handle_offer, SessionDescription
from services.security import verify_api_key

router = APIRouter(prefix="/api")


class RTCOffer(BaseModel):
    sdp: str
    type: str


@router.post("/rtc")
async def rtc(offer: RTCOffer, _: None = Depends(verify_api_key)) -> dict:
    answer: SessionDescription = await handle_offer(offer.sdp, offer.type)
    return {"sdp": answer.sdp, "type": answer.type}
