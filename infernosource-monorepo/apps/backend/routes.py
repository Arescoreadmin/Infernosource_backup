# apps/backend/ai_rewriting/routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import os

try:
    import openai
    OPENAI_AVAILABLE = True
    openai.api_key = os.getenv("OPENAI_API_KEY")
except ImportError:
    OPENAI_AVAILABLE = False

router = APIRouter()

class RewriteRequest(BaseModel):
    text: str = Field(..., description="Text content to be rewritten")
    tone: Optional[str] = Field("neutral", description="Desired tone (e.g., persuasive, casual, professional)")
    temperature: Optional[float] = Field(0.7, description="Creativity level for AI output")

class RewriteResponse(BaseModel):
    original: str
    rewritten: str
    tone: str
    used_ai: bool

@router.post("/rewrite", response_model=RewriteResponse, tags=["AI Rewriting"])
async def rewrite_text(request: RewriteRequest):
    """
    Rewrite text using AI (OpenAI GPT-based) or a fallback logic if unavailable.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    if OPENAI_AVAILABLE and openai.api_key:
        try:
            prompt = (
                f"Rewrite the following text in a {request.tone} tone:\n\n"
                f"{request.text}\n\n"
                "Rewritten:"
            )
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a rewriting assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=request.temperature,
                max_tokens=1000
            )
            rewritten = response['choices'][0]['message']['content'].strip()
            return RewriteResponse(
                original=request.text,
                rewritten=rewritten,
                tone=request.tone,
                used_ai=True
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"AI rewriting failed: {str(e)}")
    else:
        # Fallback dummy rewrite
        rewritten = f"[{request.tone} tone rewrite not available — dummy output]: {request.text}"
        return RewriteResponse(
            original=request.text,
            rewritten=rewritten,
            tone=request.tone,
            used_ai=False
        )
