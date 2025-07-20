# backend/spider/test_spider.py

import requests
from bs4 import BeautifulSoup

def simple_scrape(url: str):
    """
    Fetches a page and extracts its title and first 500 characters of text content.
    """
    print(f"Scraping URL: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text

        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string if soup.title else "No title"
        body_text = soup.get_text(separator=' ', strip=True)[:500]

        print(f"Title: {title}")
        print(f"Content preview: {body_text}")
        return {
            "title": title,
            "preview": body_text
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

if __name__ == "__main__":
    test_url = "https://example.com"
    result = simple_scrape(test_url)
    if result:
        print("Scraping succeeded.")
    else:
        print("Scraping failed.")
