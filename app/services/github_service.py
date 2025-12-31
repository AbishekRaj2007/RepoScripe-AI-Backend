import requests
from app.config import GITHUB_TOKEN

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def fetch_repo_files(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    res = requests.get(url, headers=HEADERS)

    if res.status_code != 200:
        raise Exception("Failed to fetch repository contents")

    data = res.json()
    return [item["path"] for item in data if item["type"] == "file"]
