from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# ===============================
# ✅ User Schemas
# ===============================

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    role: str

    class Config:
        from_attributes = True


# ===============================
# ✅ Token Schemas
# ===============================

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None


# ===============================
# ✅ Site Schemas
# ===============================

class SiteCreate(BaseModel):
    name: str
    url: str

class SiteOut(BaseModel):
    id: int
    name: str
    url: str
    owner_id: int

    class Config:
        from_attributes = True


# ===============================
# ✅ Session Log Schemas
# ===============================

class SessionLogOut(BaseModel):
    id: int
    user_id: int
    action: str
    timestamp: datetime
    details: Optional[str] = None

    class Config:
        from_attributes = True


# ===============================
# ✅ Scraping Schemas
# ===============================

class ScrapeRequest(BaseModel):
    url: str
    site_id: int

class ScrapedPageResponse(BaseModel):
    id: int
    url: str
    html_content: Optional[str]
    css_content: Optional[str]
    js_content: Optional[str]
    text_content: Optional[str]

    class Config:
        from_attributes = True


# ===============================
# ✅ AI Rewriting Schemas
# ===============================

class RewriteRequest(BaseModel):
    content: str
    tone: Optional[str] = "neutral"
    purpose: Optional[str] = "general"

class RewriteResponse(BaseModel):
    original: str
    rewritten: str
