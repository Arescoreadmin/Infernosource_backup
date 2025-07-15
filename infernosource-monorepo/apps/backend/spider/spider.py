import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def is_same_domain(start_url, link):
    return urlparse(start_url).netloc == urlparse(link).netloc

def crawl(start_url: str, max_pages: int = 50):
    visited = set()
    queue = deque([start_url])
    results = []

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        try:
            response = requests.get(url, timeout=10)
            visited.add(url)
            results.append(url)
            soup = BeautifulSoup(response.content, "html.parser")
            for a_tag in soup.find_all("a", href=True):
                link = urljoin(url, a_tag["href"])
                if is_valid_url(link) and is_same_domain(start_url, link) and link not in visited:
                    queue.append(link)
        except requests.RequestException:
            continue

    return results
