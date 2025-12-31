import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env from project root
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found")

if not GITHUB_TOKEN:
    raise RuntimeError("GITHUB_TOKEN not found")


print("DEBUG CONFIG LOADED")
print("DEBUG OPENAI_API_KEY =", OPENAI_API_KEY)
