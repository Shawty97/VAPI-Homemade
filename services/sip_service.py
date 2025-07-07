import structlog
from typing import Optional
from prometheus_client import Counter

logger = structlog.get_logger()

outbound_calls_total = Counter("outbound_calls_total", "Number of outbound calls")


async def initiate_call(to_number: str, tenant_id: Optional[str] = None) -> None:
    """Simulate initiating an outbound SIP call."""
    logger.info("initiate_call", to_number=to_number, tenant=tenant_id)
    outbound_calls_total.inc()
    # Placeholder for real SIP integration

