from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import database models so SQLAlchemy sees them all
from apps.backend import models
from apps.backend.database import Base, engine

# Import routers from respective modules
from apps.backend.auth import router as auth_router
from apps.backend.routes import router as site_router
from apps.backend.seo_routes import router as seo_router
from apps.backend.scraper.routes import router as scrape_router
from apps.backend.ai_rewriting.routes import router as ai_router
from apps.backend.ai_research.routes import router as ai_research_router
from apps.backend.branding.routes import router as branding_router
from apps.backend.analytics.routes import router as analytics_router

# Create DB tables (for dev, Alembic for prod)
Base.metadata.create_all(bind=engine)

# The app instance that Uvicorn expects
app = FastAPI(
    title="InfernoSource API",
    description="Scrape, rewrite, audit, and generate websites with AI.",
    version="0.1.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(site_router, prefix="/sites", tags=["Sites"])
app.include_router(seo_router, prefix="/seo", tags=["SEO"])
app.include_router(scrape_router, prefix="/scrape", tags=["Scraper"])
app.include_router(ai_router, prefix="/rewrite", tags=["AI Rewriting"])
app.include_router(ai_research_router, prefix="/ai_research", tags=["AI Research"])
app.include_router(branding_router, prefix="/branding", tags=["Branding"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
