from agent_models import ResearchContext
import uuid

def run_research_agent(description: str, region: str, language: str) -> list[ResearchContext]:
    # Dummy output for now
    return [
        ResearchContext(
            id=str(uuid.uuid4()),
            category="market",
            title="Regional Ad Trends",
            summary="Trends in digital marketing for target region.",
            sources=["https://example.com/trend1", "https://example.com/trend2"],
            confidence=85
        )
    ]
