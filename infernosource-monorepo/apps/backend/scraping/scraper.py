# apps/backend/scraping/scraper.py

import requests
from bs4 import BeautifulSoup

def parse_page(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string if soup.title else ''
    description_tag = soup.find('meta', attrs={'name': 'description'})
    description = description_tag['content'] if description_tag else ''

    # Remove script and style tags
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text(separator=' ', strip=True)

    return {
        "url": url,
        "title": title,
        "description": description,
        "text": text,
        "html": response.text
    }
