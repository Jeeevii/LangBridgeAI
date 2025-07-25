import time
from app.schemas import GenerationRequest, GenerationResult
from app.mockdata import mockResearchContext, mockGeneratedVideo

def generate_video(request: GenerationRequest) -> GenerationResult:
    start = time.time()
    return GenerationResult(
        id=f"gen-{int(start)}",
        request=request,
        researchContext=mockResearchContext,
        generatedVideo=mockGeneratedVideo,
        processingTime=round(time.time() - start, 2),
        status="completed",
    )