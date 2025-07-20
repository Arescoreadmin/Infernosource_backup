# backend/celery_worker.py

from celery import Celery

# Change the broker URL if you use Redis, RabbitMQ, etc.
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_BACKEND_URL = "redis://localhost:6379/1"

celery_app = Celery(
    "infernosource_worker",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL
)

@celery_app.task
def add(x, y):
    return x + y

@celery_app.task
def scrape_url_task(url):
    # Placeholder logic for scraping (real logic goes here)
    print(f"Scraping {url} in background (celery)")
    return f"Scraped data from {url}"

if __name__ == "__main__":
    # Optional: test with celery -A backend.celery_worker worker --loglevel=info
    result = add.delay(2, 3)
    print(f"Add result: {result.get(timeout=10)}")
