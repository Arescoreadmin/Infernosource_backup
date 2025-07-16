from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ========== USERS ==========
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, email: str, password: str, full_name: str = "", role: str = "user"):
    hashed_password = pwd_context.hash(password)
    db_user = models.User(
        email=email,
        hashed_password=hashed_password,
        full_name=full_name,
        role=role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user


# ========== SITES ==========
def create_site(db: Session, name: str, url: str, owner_id: int):
    site = models.Site(name=name, url=url, owner_id=owner_id)
    db.add(site)
    db.commit()
    db.refresh(site)
    return site


def get_site_by_url(db: Session, url: str):
    return db.query(models.Site).filter(models.Site.url == url).first()


# ========== PAGES ==========
def create_scraped_page(db: Session, site_id: int, url: str, html_content: str, extracted_text: str):
    page = models.ScrapedPage(
        site_id=site_id,
        url=url,
        html_content=html_content,
        extracted_text=extracted_text
    )
    db.add(page)
    db.commit()
    db.refresh(page)
    return page


def get_page(db: Session, page_id: int):
    return db.query(models.ScrapedPage).filter(models.ScrapedPage.id == page_id).first()


# ========== SESSION LOGS ==========
def create_session_log(db: Session, user_id: int, action: str, details: str = None):
    log = models.SessionLog(
        user_id=user_id,
        action=action,
        details=details
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
