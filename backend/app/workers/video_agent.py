from agent_models import GeneratedVideo, VoiceOver
from datetime import datetime
import uuid

def run_video_agent(script: str, language: str) -> GeneratedVideo:
    return GeneratedVideo(
        id=str(uuid.uuid4()),
        title="Auto-Generated Video",
        description="A video generated using AI agents.",
        duration=120,
        thumbnailUrl="https://placehold.co/600x400",
        videoUrl="https://example.com/video.mp4",
        script=script,
        voiceOver=VoiceOver(language=language, accent="neutral", gender="male"),
        createdAt=datetime.utcnow().isoformat()
    )
