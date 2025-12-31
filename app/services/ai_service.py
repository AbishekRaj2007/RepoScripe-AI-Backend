from groq import Groq
from app.config import GROQ_API_KEY
from typing import Generator

client = Groq(api_key=GROQ_API_KEY)


def stream_readme(repo_url: str, style: str) -> Generator[str, None, None]:
    """
    Streams README generation token-by-token from Groq
    """

    prompt = f"""
You are an expert software engineer.

Generate a {style} GitHub README.md for the following repository:

Repository URL:
{repo_url}

Include:
- Project overview
- Features
- Tech stack
- Installation
- Usage
- Folder structure
- Future improvements
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You generate professional README files."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=1200,
        stream=True
    )

    for chunk in completion:
        if chunk.choices and chunk.choices[0].delta:
            content = chunk.choices[0].delta.content
            if content:
                yield content
