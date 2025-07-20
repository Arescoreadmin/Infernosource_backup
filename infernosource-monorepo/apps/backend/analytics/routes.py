from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class AnalyticsRequest(BaseModel):
    campaign_id: int

class Metric(BaseModel):
    name: str
    value: float

class AnalyticsResponse(BaseModel):
    campaign_id: int
    metrics: List[Metric]
    last_updated: Optional[str]

@router.get("/test", tags=["Analytics"])
def analytics_test():
    """Check Analytics route status."""
    return {"status": "analytics route active"}

@router.post("/metrics", response_model=AnalyticsResponse, tags=["Analytics"])
def get_metrics(request: AnalyticsRequest):
    """
    Dummy analytics fetch (replace with real DB/stats later).
    """
    # Placeholder metrics
    metrics = [
        Metric(name="CTR", value=0.073),
        Metric(name="Impressions", value=1200),
        Metric(name="Clicks", value=88),
        Metric(name="Conversions", value=9)
    ]
    return AnalyticsResponse(
        campaign_id=request.campaign_id,
        metrics=metrics,
        last_updated="2025-07-19T00:00:00Z"
    )
