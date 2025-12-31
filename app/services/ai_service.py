from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_readme(file_list: str) -> str:
    prompt = f"""
You are an expert software engineer.
Generate a professional README.md for the following GitHub repository.

Include:
- Project overview
- Features
- Tech stack
- Installation
- Usage
- Folder structure
- Future improvements

Repository files:
{file_list}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate professional README files."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
