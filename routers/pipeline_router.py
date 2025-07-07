from fastapi import APIRouter, Depends, File, UploadFile, Response

from services.pipeline_service import run_pipeline
from services.security import verify_api_key

router = APIRouter(prefix="/api")


@router.post("/voice-pipeline")
async def voice_pipeline(file: UploadFile = File(...), _: None = Depends(verify_api_key)) -> Response:
    """Run the voice pipeline for an uploaded audio file."""
    audio_data = await file.read()
    output = await run_pipeline(audio_data, {})
    return Response(content=output, media_type="audio/wav")
