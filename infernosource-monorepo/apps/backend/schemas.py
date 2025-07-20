from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List

# -------- User Schemas --------
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    role: str

    class Config:
        from_attributes = True  # Pydantic v2

# -------- Page/Site Schemas --------
class PageCreate(BaseModel):
    title: str

class PageOut(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True

# -------- Rewrite Schemas --------
class RewriteRequest(BaseModel):
    url: Optional[str] = None
    text: Optional[str] = None
    tone: Optional[str] = "Professional"
    persona: Optional[str] = "Marketer"
    urgency: Optional[str] = "Medium"
    deep_rewrite: Optional[bool] = False

class RewriteResponse(BaseModel):
    rewritten_text: str
    status: Optional[str] = "success"

# -------- Campaign Schemas --------
class CampaignCreate(BaseModel):
    name: str
    description: Optional[str] = None
    persona: Optional[str] = None
    tone: Optional[str] = None
    urgency: Optional[str] = None

class CampaignOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    persona: Optional[str]
    tone: Optional[str]
    urgency: Optional[str]

    class Config:
        from_attributes = True

# -------- Scraper Schemas --------
class ScrapeRequest(BaseModel):
    url: str
    site_id: Optional[int] = None

class ScrapedPageResponse(BaseModel):
    url: str
    html_content: Optional[str]
    extracted_text: Optional[str]
    site_id: Optional[int] = None

# -------- Analytics Example --------
class AnalyticsData(BaseModel):
    id: int
    event: str
    campaign_id: Optional[int]
    meta: Optional[dict]

    class Config:
        from_attributes = True

CampaignResponse = CampaignOut
