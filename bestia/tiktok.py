from bs4 import BeautifulSoup
import requests, random, time

def fetch(url: str, retries: int = 3, backoff: float = 2.0) -> BeautifulSoup:
    """Pobiera URL z prostym retry + back-off."""
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, timeout=10,
                             headers={"User-Agent": "Mozilla/5.0 BESTIA"})
            r.raise_for_status()
            return BeautifulSoup(r.text, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"[WARN] {e}  (próba {attempt}/{retries})")
            if attempt == retries:
                raise
            time.sleep(backoff * attempt + random.uniform(0, 1))

def get_shop_title(shop_url: str) -> str:
    """Zwraca tytuł sklepu z TikTok Shop."""
    soup = fetch(shop_url)
    return soup.select_one("h1.shop-title").text.strip()

# 🔥  Funkcja, której szuka main.py
def run_tiktok_bot() -> None:
    """Demo-bot – pobiera i wypisuje tytuł przykładowego sklepu."""
    title = get_shop_title("https://www.tiktok.com/@example/shop")
    print("👀  Tytuł testowy z TikTok-bota:", title)
