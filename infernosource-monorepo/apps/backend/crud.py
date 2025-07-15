from sqlalchemy.orm import Session
from apps.backend import models, schemas
from apps.backend.auth import get_password_hash
from apps.backend.scraping.models import ScrapedPage

# ========== User CRUD ==========

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ========== Site CRUD ==========

def create_site(db: Session, site: schemas.SiteCreate, user_id: int):
    db_site = models.Site(**site.dict(), owner_id=user_id)
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

def get_sites(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Site).offset(skip).limit(limit).all()

# ========== Session Log CRUD ==========

def create_session_log(db: Session, log: schemas.SessionLogCreate, user_id: int):
    db_log = models.SessionLog(**log.dict(), user_id=user_id)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_session_logs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SessionLog).offset(skip).limit(limit).all()

# ========== Scraped Page CRUD ==========

def create_page(db: Session, url: str, content: str, seo_score: float, created_by: int):
    db_page = ScrapedPage(
        url=url,
        content=content,
        seo_score=seo_score,
        owner_id=created_by
    )
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page

def get_page(db: Session, page_id: int):
    return db.query(ScrapedPage).filter(ScrapedPage.id == page_id).first()
