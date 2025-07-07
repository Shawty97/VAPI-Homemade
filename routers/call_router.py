from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.sip_service import initiate_call
from services.security import verify_api_key

router = APIRouter(prefix="/api")


class CallRequest(BaseModel):
    to_number: str
    tenant_id: str | None = None


@router.post("/outbound-call")
async def outbound_call(req: CallRequest, _: None = Depends(verify_api_key)) -> dict:
    await initiate_call(req.to_number, req.tenant_id)
    return {"status": "initiated"}
