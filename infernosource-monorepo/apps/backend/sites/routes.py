from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/sites/pages", response_model=List[schemas.PageOut])
def list_pages(db: Session = Depends(get_db)):
    return crud.get_pages(db)
