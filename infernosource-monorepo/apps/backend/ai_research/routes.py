from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

class ResearchQuery(BaseModel):
    topic: str
    competitor: Optional[str] = None

class ResearchInsight(BaseModel):
    title: str
    summary: str

class ResearchResponse(BaseModel):
    topic: str
    insights: List[ResearchInsight]

@router.get("/test", tags=["AI Research"])
def ai_research_test():
    """Check AI Research route status."""
    return {"status": "ai research route active"}

@router.post("/insights", response_model=ResearchResponse, tags=["AI Research"])
def get_research_insights(query: ResearchQuery):
    """
    Dummy AI research (replace with actual LLM research/integration).
    """
    mock_insights = [
        ResearchInsight(
            title=f"Latest trends in {query.topic}",
            summary=f"Summary about new trends in {query.topic} for {query.competitor or 'the industry'}."
        ),
        ResearchInsight(
            title=f"Key competitors for {query.topic}",
            summary=f"Competitor analysis for {query.competitor or query.topic}."
        ),
    ]
    return ResearchResponse(
        topic=query.topic,
        insights=mock_insights
    )
