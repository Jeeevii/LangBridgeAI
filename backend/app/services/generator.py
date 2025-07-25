import time
import os
from datetime import datetime
from app.schemas import GenerationRequest, GenerationResult, ResearchContext, GeneratedVideo, VoiceOver
from app.mockdata import mockResearchContext, mockGeneratedVideo

# Import Bedrock service
try:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from app.aws_bedrock import BedrockService
    BEDROCK_AVAILABLE = True
except ImportError:
    BEDROCK_AVAILABLE = False
    print("Warning: AWS Bedrock not available, using mock data")

def generate_video(request: GenerationRequest) -> GenerationResult:
    start = time.time()
    
    if BEDROCK_AVAILABLE and os.getenv("USE_BEDROCK", "false").lower() == "true":
        try:
            bedrock = BedrockService()
            
            # Generate research context
            research_data = bedrock.generate_research_context(request.description, request.region)
            research_context = [ResearchContext(
                id=f"research-{int(start)}",
                **research_data
            )]
            
            # Generate video script
            script = bedrock.generate_video_script(
                request.description, 
                request.region, 
                request.language, 
                request.targetAudience
            )
            
            # Create generated video with AI content
            generated_video = GeneratedVideo(
                id=f"video-{int(start)}",
                title=f"AI Generated: {request.description}",
                description=f"Video about {request.description} for {request.region}",
                duration=180,  # 3 minutes
                thumbnailUrl="https://example.com/ai-thumbnail.jpg",
                videoUrl="https://example.com/ai-video.mp4",
                script=script,
                voiceOver=VoiceOver(
                    language=request.language,
                    accent="neutral",
                    gender="neutral"
                ),
                createdAt=datetime.now().isoformat()
            )
            
        except Exception as e:
            print(f"Bedrock error: {e}, falling back to mock data")
            research_context = mockResearchContext
            generated_video = mockGeneratedVideo
    else:
        research_context = mockResearchContext
        generated_video = mockGeneratedVideo
    
    return GenerationResult(
        id=f"gen-{int(start)}",
        request=request,
        researchContext=research_context,
        generatedVideo=generated_video,
        processingTime=round(time.time() - start, 2),
        status="completed",
    )