from fastapi import APIRouter, Depends
from apps.backend.auth import get_current_user
from apps.backend.schemas import CompetitorQuery
import openai

router = APIRouter()

@router.post("/competitors")
def find_competitors(query: CompetitorQuery, user=Depends(get_current_user)):
    if query.idea and query.competitor_url:
        prompt = (
            f"Given this business idea: '{query.idea}' and competitor site: '{query.competitor_url}', "
            "list the top 3 competitor websites (with their URLs only)."
        )
    elif query.idea:
        prompt = (
            f"Given this business idea: '{query.idea}', "
            "list the top 3 competitor websites (with their URLs only)."
        )
    elif query.competitor_url:
        prompt = (
            f"Given this competitor site: '{query.competitor_url}', "
            "list the top 3 similar competitor websites (with their URLs only)."
        )
    else:
        return {"error": "Please provide either an idea or a competitor_url."}
    
    # You must have your OpenAI API key set as an environment variable
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful web business analyst."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.3,
    )
    text = response.choices[0].message['content']
    competitors = []
    for line in text.split('\n'):
        if 'http' in line:
            url = line.strip().split(' ')[-1]
            competitors.append({"url": url})
    return {"results": competitors}
