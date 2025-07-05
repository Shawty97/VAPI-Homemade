from fastapi import APIRouter, WebSocket

from services.websocket_service import handle_websocket

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await handle_websocket(websocket)
