import os
from fastapi import Header, HTTPException, status


async def verify_api_key(x_api_key: str = Header(...)) -> None:
    """Validate the API key from request headers."""
    expected = os.getenv("API_KEY")
    if not expected or x_api_key != expected:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")

