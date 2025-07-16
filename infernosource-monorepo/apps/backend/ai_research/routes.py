from fastapi import APIRouter, Depends, HTTPException
from apps.backend.auth import get_current_user

router = APIRouter()

@router.post("/competitors")
def find_competitors(query: str, user=Depends(get_current_user)):
    # Here you would use OpenAI/SERP API for real results, this is a placeholder:
    competitors = [
        {"url": "https://example1.com", "traffic": 120000, "score": 98},
        {"url": "https://example2.com", "traffic": 90000, "score": 95},
        {"url": "https://example3.com", "traffic": 87000, "score": 91},
    ]
    return {"results": competitors}
