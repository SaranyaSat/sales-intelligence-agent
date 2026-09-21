import requests
from bs4 import BeautifulSoup

def ingest_url_content(url: str) -> str:
    """Fetches raw HTML data strings and cleans tags to feed context logs."""
    if not url:
        return ""
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:10000]
    except Exception as e:
        return f"[Ingestion Bypass for {url}: {str(e)}]"
