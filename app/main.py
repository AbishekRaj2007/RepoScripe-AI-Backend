from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.services.ai_service import stream_readme

app = FastAPI(title="RepoScribe AI Backend")

# ✅ CORS (required for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Schema ----------
class RepoRequest(BaseModel):
    repoUrl: str
    style: str


# ---------- STREAMING ENDPOINT ----------
@app.post("/generate-readme-stream")
def generate_readme_stream(repo: RepoRequest):
    """
    Streams README generation token-by-token
    """
    return StreamingResponse(
        stream_readme(repo.repoUrl, repo.style),
        media_type="text/plain"
    )
