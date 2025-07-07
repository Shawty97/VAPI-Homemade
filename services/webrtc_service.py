from dataclasses import dataclass
import structlog

logger = structlog.get_logger()

@dataclass
class SessionDescription:
    sdp: str
    type: str

async def handle_offer(sdp: str, type_: str) -> SessionDescription:
    """Process a WebRTC offer and return an answer placeholder."""
    logger.info("handle_offer", type=type_)
    # Placeholder for full aiortc-based SDP negotiation
    # Here we simply echo the SDP to demonstrate the flow
    return SessionDescription(sdp=sdp, type="answer")
