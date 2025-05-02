from __future__ import annotations
import os, re, requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from dotenv import load_dotenv
load_dotenv()

TAG = os.getenv("AMZ_TAG")                 # np. twojnick-21
HEADERS = {"User-Agent": "Mozilla/5.0 BESTIA/1.0"}
PRODUCT_RE = re.compile(r"/dp/([A-Z0-9]{10})")
LANDING_RE = re.compile(r"[A-Z0-9]{10}")  # ASIN w HTML

def generate_affiliate_url(url: str) -> str | None:
    if "amzn.to" in url:

        try:

            url = requests.get(url, headers=HEADERS, timeout=8, stream=True,

                               allow_redirects=True).url

        except requests.RequestException:

            print("⚠️  Nie udało się rozwinąć:", url); return None
    if not PRODUCT_RE.search(url):
        print("⚠️  To nie wygląda na URL produktu:", url)




# fallback: html landing-page
try:
    html = requests.get(url, headers=HEADERS, timeout=8).text
    m = LANDING_RE.search(html)
    if m:
        asin = m.group(0)
        p2 = urlparse(f"https://www.amazon.com/dp/{asin}")
        q  = {"tag": TAG}
        return urlunparse(p2._replace(query=urlencode(q, doseq=True)))
except requests.RequestException:
    pass