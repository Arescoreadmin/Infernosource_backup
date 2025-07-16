from fastapi import APIRouter, Depends
from apps.backend.auth import get_current_user

router = APIRouter()

@router.get("/summary")
def analytics_summary(site_id: int, user=Depends(get_current_user)):
    # Placeholder for analytics logic
    return {"visitors": 123, "pageviews": 456, "bounce_rate": "57%"}
