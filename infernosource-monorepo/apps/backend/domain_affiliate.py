# backend/domain_affiliate.py

from urllib.parse import urlparse

AFFILIATE_DOMAINS = {
    "amazon.com": "https://amzn.to/your-affiliate-id",
    "example.com": "https://example.com/affiliate-link",
    # Add more domains and links as needed
}

def get_affiliate_link(url: str) -> str:
    """
    Return an affiliate link for the given URL's domain, if supported.
    """
    parsed = urlparse(url)
    domain = parsed.netloc.lower().replace("www.", "")
    return AFFILIATE_DOMAINS.get(domain, url)  # Return original URL if not found

def inject_affiliate_links(html: str) -> str:
    """
    Dummy function to 'inject' affiliate links into anchor tags in provided HTML.
    (Real logic would use an HTML parser and more advanced link rewriting.)
    """
    for domain, affiliate_link in AFFILIATE_DOMAINS.items():
        html = html.replace(f'href="https://{domain}"', f'href="{affiliate_link}"')
    return html

if __name__ == "__main__":
    test_url = "https://amazon.com/product/abc"
    print("Affiliate link:", get_affiliate_link(test_url))
    test_html = '<a href="https://amazon.com">Amazon</a>'
    print("Injected HTML:", inject_affiliate_links(test_html))
