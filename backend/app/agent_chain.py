import uuid
import time
from agent_models import GenerationRequest, GenerationResult
from workers.research_agent import run_research_agent
from workers.script_agent import run_script_agent
from workers.video_agent import run_video_agent

def run_video_generation_pipeline(request: GenerationRequest) -> GenerationResult:
    start = time.time()

    try:
        print("🔍 Running research agent...")
        research_context = run_research_agent(
            request.description,
            request.region,
            request.language
        )
        if not research_context:
            raise ValueError("No research context returned.")

        print("✍️ Running script agent...")
        script = run_script_agent(
            request.description,
            research_context
        )
        if not script:
            raise ValueError("No script generated.")

        print("🎬 Running video agent...")
        video = run_video_agent(
            script,
            request.language
        )
        if not video:
            raise ValueError("Video generation failed.")

        status = "completed"

    except Exception as e:
        print(f"❌ Pipeline failed: {e}")
        research_context = []
        script = None
        video = None
        status = "failed"

    end = time.time()

    return GenerationResult(
        id=str(uuid.uuid4()),
        request=request,
        researchContext=research_context or [],
        generatedVideo=video,
        processingTime=round(end - start, 2),
        status=status
    )

# === Standalone test run ===
if __name__ == "__main__":
    test_request = GenerationRequest(
        description="What's the best ADC in League right now? Answer in one sentence!",
        region="US",
        language="en"
    )

    result = run_video_generation_pipeline(test_request)

    print("\n=== Final Result ===")
    print("ID:", result.id)
    print("Status:", result.status)
    print("Research Context:", result.researchContext[:1] if result.researchContext else "None")
    print("Generated Video (Mocked):", result.generatedVideo if result.generatedVideo else "None")
    print("Processing Time:", result.processingTime, "seconds")
