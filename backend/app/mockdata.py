from app.schemas import ResearchContext, GeneratedVideo, VoiceOver
from datetime import datetime

mockResearchContext = [
    ResearchContext(
        id="1",
        category="Cultural Analysis",
        title="Japanese Advertising Preferences",
        summary="Japanese consumers respond well to subtle emotional storytelling...",
        sources=["Dentsu Advertising Trends 2024", "Japan Marketing Association", "Cultural Consumer Insights"],
        confidence=94,
    ),
    # ... Add remaining entries (2–4)
]

mockGeneratedVideo = GeneratedVideo(
    id="video-001",
    title="EcoStride Japan - Urban Harmony",
    description="A minimalist 30-second ad...",
    duration=30,
    thumbnailUrl="/placeholder.svg?height=400&width=600",
    videoUrl="/placeholder.svg?height=400&width=600",
    script="Scene opens with a runner in Tokyo...",
    voiceOver=VoiceOver(language="Japanese", accent="Tokyo Standard", gender="Female"),
    createdAt=datetime.utcnow().isoformat(),
)