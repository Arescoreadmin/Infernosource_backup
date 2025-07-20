# backend/scraping/utils.py

import requests
from bs4 import BeautifulSoup

def fetch_html(url: str) -> str:
    """
    Fetch raw HTML from a URL.
    """
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def extract_text_from_html(html: str) -> str:
    """
    Extracts and returns the plain text from HTML.
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator=' ', strip=True)

def extract_title_from_html(html: str) -> str:
    """
    Extracts the title from HTML.
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.string.strip() if soup.title and soup.title.string else ""

if __name__ == "__main__":
    url = "https://example.com"
    html = fetch_html(url)
    title = extract_title_from_html(html)
    text = extract_text_from_html(html)
    print("Title:", title)
    print("Text preview:", text[:200])
