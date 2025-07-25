from pydantic import BaseModel
from typing import List, Literal

class GenerationRequest(BaseModel):
    description: str
    region: str
    language: str
    targetAudience: str | None = None

class ResearchContext(BaseModel):
    id: str
    category: str
    title: str
    summary: str
    sources: List[str]
    confidence: int

class VoiceOver(BaseModel):
    language: str
    accent: str
    gender: str

class GeneratedVideo(BaseModel):
    id: str
    title: str
    description: str
    duration: int
    thumbnailUrl: str
    videoUrl: str
    script: str
    voiceOver: VoiceOver
    createdAt: str

class GenerationResult(BaseModel):
    id: str
    request: GenerationRequest
    researchContext: List[ResearchContext]
    generatedVideo: GeneratedVideo
    processingTime: float
    status: Literal["completed", "processing", "failed"]

class ExportResponse(BaseModel):
    downloadUrl: str