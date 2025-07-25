from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import GenerationRequest, GenerationResult, ExportResponse
from app.services.generator import generate_video

app = FastAPI()

# Enable CORS for frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change to prod domain if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate", response_model=GenerationResult)
def generate(request: GenerationRequest):
    return generate_video(request)

@app.get("/export/{video_id}", response_model=ExportResponse)
def export_video(video_id: str, format: str):
    return ExportResponse(downloadUrl=f"https://example.com/exports/{video_id}.{format}")

# Run the app directly (for dev use)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
