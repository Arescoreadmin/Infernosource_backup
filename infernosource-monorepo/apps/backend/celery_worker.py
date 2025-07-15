# apps/backend/celery_worker.py

from celery import Celery
from apps.backend.database import SessionLocal
from apps.backend.crud import get_page, create_session_log
from apps.backend.models import SessionLog
import os

celery = Celery(
    "worker",
    broker=os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
)

@celery.task
def process_page_async(page_id: int):
    db = SessionLocal()
    try:
        page = get_page(db, page_id)
        if page:
            create_session_log(
                db,
                log={"action": f"processed_page {page.url}"},
                user_id=page.owner_id,
            )
    finally:
        db.close()
