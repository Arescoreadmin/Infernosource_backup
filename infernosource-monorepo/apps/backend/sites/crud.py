from sqlalchemy.orm import Session
from .models import Page

def get_pages(db: Session):
    return db.query(Page).all()
