from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class SEORequest(BaseModel):
    html: str

class SEOResponse(BaseModel):
    title: Optional[str]
    meta_description: Optional[str]
    keywords: List[str] = []

@router.get("/test", tags=["SEO"])
def seo_test():
    """Check SEO route status."""
    return {"status": "seo route active"}

@router.post("/analyze", response_model=SEOResponse, tags=["SEO"])
def analyze_seo(request: SEORequest = Body(...)):
    """
    Dummy SEO analysis logic (replace with real HTML parsing/SEO audit later).
    """
    # Placeholder logic for extracting mock SEO data
    mock_title = "Sample Title"
    mock_description = "Sample meta description"
    mock_keywords = ["sample", "seo", "keywords"]

    return SEOResponse(
        title=mock_title,
        meta_description=mock_description,
        keywords=mock_keywords
    )
