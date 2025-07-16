from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers from respective modules
from apps.backend.auth import router as auth_router
from apps.backend.routes import router as site_router
from apps.backend.seo_routes import router as seo_router
from apps.backend.scraper.routes import router as scrape_router
from apps.backend.ai_rewriting.routes import router as ai_router

from apps.backend.database import Base, engine

# ✅ Create DB tables (dev-only; Alembic should be used in production)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="InfernoSource API",
    description="Scrape, rewrite, audit, and generate websites with AI.",
    version="0.1.0",
)

# 🔓 CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Mount all routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(site_router, prefix="/sites", tags=["Sites"])
app.include_router(seo_router, prefix="/seo", tags=["SEO"])
app.include_router(scrape_router, prefix="/scrape", tags=["Scraper"])
app.include_router(ai_router, prefix="/rewrite", tags=["AI Rewriting"])
