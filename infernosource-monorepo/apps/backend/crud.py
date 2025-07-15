# apps/backend/crud.py

from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    """
    Retrieve a user by their email.
    """
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, email: str, password: str):
    """
    Create a new user with the given email and raw password.
    Returns the created User model instance.
    """
    hashed_password = pwd_context.hash(password)
    db_user = models.User(email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    """
    Verify a user's credentials.
    Returns the user if successful, or None if invalid.
    """
    user = get_user_by_email(db, email)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user

def create_page(db: Session, url: str, content: str, seo_score: int, owner_id: int):
    """
    Create a new Page record.
    """
    db_page = models.Page(
        url=url,
        content=content,
        seo_score=seo_score,
        owner_id=owner_id
    )
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page

def get_page(db: Session, page_id: int):
    """
    Retrieve a Page by its ID.
    """
    return db.query(models.Page).filter(models.Page.id == page_id).first()
