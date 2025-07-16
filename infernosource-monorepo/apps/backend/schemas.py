from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    role: str

    class Config:
        orm_mode = True

class CompetitorQuery(BaseModel):
    idea: Optional[str] = None
    competitor_url: Optional[HttpUrl] = None

class ScrapeRequest(BaseModel):
    url: str

class ScrapedPageResponse(BaseModel):
    url: str
    html_content: Optional[str]
    extracted_text: Optional[str]

class RewriteRequest(BaseModel):
    url: Optional[str] = None
    text: Optional[str] = None

class RewriteResponse(BaseModel):
    rewritten_text: str
    status: Optional[str] = "success"
