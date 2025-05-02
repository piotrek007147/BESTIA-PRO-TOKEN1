import random, time
import requests
from bs4 import BeautifulSoup

def fetch(url: str, retries: int = 3, backoff: float = 2.0) -> BeautifulSoup:
    """
    Pobiera URL i zwraca BeautifulSoup.
    Przy błędach sieci/HTTP (5xx, 429 itp.) ponawia maks. `retries` razy
    z rosnącym opóźnieniem (`backoff` · nr próby + losowy jitter 0-1 s).
    """
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, timeout=10,
                             headers={"User-Agent": "Mozilla/5.0 BESTIA"})
            r.raise_for_status()
            return BeautifulSoup(r.text, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"[WARN] {e}  (próba {attempt}/{retries})")
            if attempt == retries:           # ostatnia próba – kończymy
                raise
            wait = backoff * attempt + random.uniform(0, 1)
            time.sleep(wait)
