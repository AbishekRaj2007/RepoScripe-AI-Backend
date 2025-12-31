from pydantic import BaseModel

class RepoRequest(BaseModel):
    owner: str
    repo:str