from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from app.schemas import GenerationRequest, GenerationResult, ExportResponse
from app.services.generator import generate_video

# Load environment variables
load_dotenv()

app = FastAPI()

# Class for Request Body for a prompt of type string
class PromptRequest(BaseModel):
    prompt: str

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

@app.post("/bedrock")
def bedrock_prompt(request: PromptRequest):
    """Send prompt to Bedrock and return response"""
    try:
        from app.aws_bedrock import BedrockService
        
        bedrock = BedrockService()
        response = bedrock.generate_content(request.prompt)
        return {"success": True, "response": response}
    except Exception as e:
        return {"success": False, "error": str(e)}

# Run the app directly (for dev use)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

@app.post("/brightdata")
def brightdata_prompt(request: PromptRequest):
    """Send prompt to Brightdata and return response"""
    try:
        from app.brightdata import BrightdataService

        brightdata = BrightdataService()
        response = brightdata.generate_content(request.prompt)
        return {"success": True, "response": response}
    except Exception as e:
        return {"success": False, "error": str(e)}