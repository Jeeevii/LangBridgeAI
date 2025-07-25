from app.schemas import ResearchContext, GeneratedVideo, VoiceOver
from datetime import datetime

mockResearchContext = [
    ResearchContext(
        id="1",
        category="Cultural Analysis",
        title="Japanese Advertising Preferences",
        summary=(
            "Japanese consumers respond well to subtle emotional storytelling, "
            "minimalist aesthetics, and emphasis on quality craftsmanship. "
            "Seasonal references and group harmony themes are particularly effective."
        ),
        sources=["Dentsu Advertising Trends 2024", "Japan Marketing Association", "Cultural Consumer Insights"],
        confidence=94,
    ),
    ResearchContext(
        id="2",
        category="Product Research",
        title="Running Shoe Marketing in Japan",
        summary=(
            "Japanese running shoe ads focus on technical innovation, comfort during long commutes, "
            "and integration with urban lifestyle. Emphasis on precision engineering and attention to detail resonates strongly."
        ),
        sources=["Nike Japan Campaign Analysis", "Asics Marketing Strategy", "Japanese Sports Retail Data"],
        confidence=89,
    ),
    ResearchContext(
        id="3",
        category="Trend Analysis",
        title="Current Japanese Consumer Trends",
        summary=(
            "Sustainability consciousness is rising among Japanese millennials. Health and wellness trends emphasize "
            "balance and mindfulness. Urban consumers value products that enhance their daily routines."
        ),
        sources=["Japan Consumer Behavior Report 2024", "Sustainability Trends Japan", "Urban Lifestyle Survey"],
        confidence=91,
    ),
    ResearchContext(
        id="4",
        category="Competitive Analysis",
        title="Eco-Friendly Product Positioning",
        summary=(
            "Successful eco-friendly products in Japan emphasize long-term value, quality materials, "
            "and subtle environmental messaging. Avoid aggressive green marketing in favor of understated sustainability benefits."
        ),
        sources=["Green Marketing Japan", "Sustainable Brand Analysis", "Consumer Preference Studies"],
        confidence=87,
    ),
]
mockGeneratedVideo = GeneratedVideo(
    id="video-001",
    title="EcoStride Japan - Urban Harmony",
    description="A minimalist 30-second ad...",
    duration=15,
    thumbnailUrl="/placeholder.svg?height=400&width=600",
    videoUrl="/placeholder.svg?height=400&width=600",
    script="Scene opens with a runner in Tokyo...",
    voiceOver=VoiceOver(language="Japanese", accent="Tokyo Standard", gender="Female"),
    createdAt=datetime.utcnow().isoformat(),
)