# InfernoSource Backend

This is the backend API for the InfernoSource MVP.
Built with **FastAPI** for rapid modular development.

---

## 📦 Project Structure

- `main.py` — FastAPI entry point with all routes registered
- `models.py` — SQLAlchemy ORM models
- `schemas.py` — Pydantic models for request/response validation
- `crud.py` — CRUD utility functions for database operations
- `database.py` — DB engine and session management
- `utils.py` — Shared utility functions (passwords, tokens, etc.)
- `api/` — Miscellaneous or root API endpoints
- `scraper/` — Scraping module with its own API routes
- `ai_rewriting/` — AI rewriting API routes
- `seo_routes.py` — SEO analysis endpoints
- `branding/` — Brand/identity endpoints
- `analytics/` — Analytics endpoints
- `ai_research/` — AI research endpoints
- `scripts/` — Dev/test scripts and DB seeding
- `spider/` — Raw CLI or prototype spidering tools
- `scraping/` — Low-level scraping utilities

---

## 🚀 Development

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
