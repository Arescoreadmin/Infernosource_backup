from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# ========== Auth Schemas ==========

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    username: EmailStr
    password: str

# ========== User Schemas ==========

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    role: Optional[str]

    class Config:
        from_attributes = True

# ========== Site Schemas ==========

class SiteBase(BaseModel):
    url: str
    title: Optional[str] = None

class SiteCreate(SiteBase):
    pass

class SiteOut(SiteBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

# ========== SessionLog Schemas ==========

class SessionLogBase(BaseModel):
    action: str

class SessionLogCreate(SessionLogBase):
    pass

class SessionLogOut(SessionLogBase):
    id: int
    user_id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# ========== ScrapedPage Schemas ==========

class PageCreate(BaseModel):
    url: str
    html_content: Optional[str] = None
    extracted_text: Optional[str] = None
    site_id: Optional[int] = None

class PageOut(PageCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
