# apps/backend/main.py
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from apps.backend.database import SessionLocal, engine, Base
from apps.backend.models import User as UserModel

from apps.backend.auth import (
    get_current_user,
    authenticate_user,
    create_access_token,
    get_password_hash  # if used elsewhere
)
from apps.backend.schemas import (
    Token, LoginRequest, UserOut,
    PageCreate, PageOut
)

import apps.backend.crud as crud
from apps.backend.scraper import scrape_site
from apps.backend.seo_parser import analyze_seo
from apps.backend.domain_affiliate import embed_affiliate_links
from apps.backend.ai_rewriting.rewriting import rewrite_text
from apps.backend.spider.spider import crawl
from apps.backend.celery_worker import process_page_async

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Infernosource API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Health"])
def health_check():
    return {"message": "Infernosource API is healthy"}

@app.post("/token", response_model=Token, tags=["Auth"])
def login_for_access_token(form: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, form.username, form.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": create_access_token(data={"sub": user.email}), "token_type": "bearer"}

@app.get("/users/me", response_model=UserOut, tags=["Auth"])
def get_me(current_user: UserModel = Depends(get_current_user)):
    return current_user

@app.post("/scrape/", response_model=PageOut, tags=["Scraping"])
def scrape_and_process(
    page: PageCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    raw = scrape_site(page.url)
    rewritten = rewrite_text(raw)
    seo_score = analyze_seo(rewritten)
    affiliate_content = embed_affiliate_links(rewritten)

    db_page = crud.create_page(db, page.url, affiliate_content, seo_score, current_user.id)
    background_tasks.add_task(process_page_async.delay, db_page.id)
    return db_page

@app.get("/page/{page_id}", response_model=PageOut, tags=["Pages"])
def get_page(page_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    p = crud.get_page(db, page_id)
    if not p or p.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Page not found")
    return p

@app.get("/spider/", tags=["Spider"])
def run_spider(start_url: str, current_user: UserModel = Depends(get_current_user)):
    return {"spidered": crawl(start_url)}

@app.post("/tasks/process/{page_id}", tags=["Tasks"])
def trigger_process(page_id: int, current_user: UserModel = Depends(get_current_user)):
    process_page_async.delay(page_id)
    return {"status": "queued", "page_id": page_id}
