import requests
from app.config import GITHUB_TOKEN

GITHUB_API_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Folders we don't want
IGNORE_DIRS = {
    ".git",
    "node_modules",
    "venv",
    "__pycache__",
    ".github"
}


def fetch_repo_files(owner: str, repo: str) -> list[str]:
    """
    Fetch all file paths from a GitHub repository recursively.
    """
    files = []
    _fetch_recursive(owner, repo, "", files)
    return files


def _fetch_recursive(owner: str, repo: str, path: str, files: list):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/contents/{path}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return

    data = response.json()

    for item in data:
        name = item["name"]

        # Ignore junk directories
        if item["type"] == "dir" and name in IGNORE_DIRS:
            continue

        if item["type"] == "file":
            files.append(item["path"])

        elif item["type"] == "dir":
            _fetch_recursive(owner, repo, item["path"], files)
