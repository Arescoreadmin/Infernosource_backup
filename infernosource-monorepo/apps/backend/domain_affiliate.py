# apps/backend/domain_affiliate.py

from bs4 import BeautifulSoup

def embed_affiliate_links(html: str, affiliate_url: str) -> str:
    """
    Replaces all <a> tag hrefs in the given HTML with the specified affiliate URL.
    
    Parameters:
    - html (str): The raw HTML content.
    - affiliate_url (str): The affiliate link to embed in place of existing hrefs.

    Returns:
    - str: The modified HTML with updated affiliate links.
    """
    soup = BeautifulSoup(html, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        a_tag['href'] = affiliate_url
    return str(soup)
