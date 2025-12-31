from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.services.ai_service import generate_readme
from app.services.github_service import fetch_repo_files

app = FastAPI(title="RepoScribe AI Backend")


# ---------- Schemas ----------
class RepoInput(BaseModel):
    files: List[str]


class RepoRequest(BaseModel):
    owner: str
    repo: str


# ---------- Routes ----------
@app.post("/generate-readme")
def generate(repo: RepoInput):
    file_list = "\n".join(repo.files)
    readme = generate_readme(file_list)
    return {"readme": readme}


@app.post("/generate-from-github")
def generate_from_github(repo: RepoRequest):
    files = fetch_repo_files(repo.owner, repo.repo)
    readme = generate_readme("\n".join(files))
    return {"readme": readme}
