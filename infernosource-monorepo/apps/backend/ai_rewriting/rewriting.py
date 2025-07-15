# apps/backend/ai_rewriting/rewriting.py

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rewrite_text(content: str, style: str = "Clear, friendly marketing tone") -> str:
    """
    Rewrite given content using OpenAI with specified style.
    """
    prompt = f"Rewrite the following content in a {style}:\n\n{content}"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional copywriter AI."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()
