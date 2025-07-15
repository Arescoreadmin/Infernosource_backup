# apps/backend/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from apps.backend import crud, schemas, database

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----- USERS -----
@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.get("/users/", response_model=list[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

# ----- SITES -----
@router.post("/sites/", response_model=schemas.SiteOut)
def create_site(site: schemas.SiteCreate, db: Session = Depends(get_db)):
    return crud.create_site(db=db, site=site)

@router.get("/sites/", response_model=list[schemas.SiteOut])
def read_sites(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_sites(db, skip=skip, limit=limit)

# ----- SESSION LOGS -----
@router.post("/session-logs/", response_model=schemas.SessionLogOut)
def create_session_log(log: schemas.SessionLogCreate, db: Session = Depends(get_db)):
    return crud.create_session_log(db=db, log=log)

@router.get("/session-logs/", response_model=list[schemas.SessionLogOut])
def read_session_logs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_session_logs(db, skip=skip, limit=limit)
