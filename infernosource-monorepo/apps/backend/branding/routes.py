from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class BrandingRequest(BaseModel):
    company_name: str
    tagline: Optional[str] = None

class BrandingResponse(BaseModel):
    brand_colors: dict
    logo_url: str
    tagline: Optional[str]

@router.get("/test", tags=["Branding"])
def branding_test():
    """Check Branding route status."""
    return {"status": "branding route active"}

@router.post("/generate", response_model=BrandingResponse, tags=["Branding"])
def generate_branding(request: BrandingRequest):
    """
    Dummy branding generator (replace with real logic or AI service later).
    """
    mock_colors = {
        "primary": "#FF8C42",
        "background": "#131313",
        "accent": "#FFFFFF"
    }
    logo_url = f"/static/{request.company_name.lower().replace(' ', '_')}_logo.png"
    return BrandingResponse(
        brand_colors=mock_colors,
        logo_url=logo_url,
        tagline=request.tagline or f"{request.company_name} – Ignite Your Brand!"
    )
