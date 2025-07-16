from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from apps.backend import auth, routes, seo_routes
from apps.backend.database import engine
from apps.backend.scraping import models as scraping_models
from apps.backend.models import Base as core_base
from apps.backend.celery_worker import process_page_async

# Initialize FastAPI app
app = FastAPI(title="InfernoSource API", version="0.1.0")

# Set up CORS
origins = ["*"]  # You can restrict this to specific domains in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/")
def health_check():
    return JSONResponse(content={"status": "ok"})

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(routes.router, tags=["Pages"])
app.include_router(seo_routes.router, prefix="/seo", tags=["SEO"])

# Create all DB tables (if not using Alembic)
core_base.metadata.create_all(bind=engine)
scraping_models.Base.metadata.create_all(bind=engine)
