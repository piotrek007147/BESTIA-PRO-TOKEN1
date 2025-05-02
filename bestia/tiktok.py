from __future__ import annotations
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

from .core import fetch   # fetch() już masz w bestia/core.py


def get_shop_title(shop_url: str) -> str | None:
    """
    Zwraca tytuł sklepu z TikTok Shop (<h1.shop-title>) lub None,
    jeżeli elementu nie ma.
    """
    soup: BeautifulSoup = fetch(shop_url)
    node = soup.select_one("h1.shop-title")
    if node is None:                         # brak nagłówka
        print(f"⚠️  Nie znaleziono <h1.shop-title> na stronie: {shop_url}")
        return None
    return node.text.strip()


# 🔥 Funkcja, której szuka main.py
def run_tiktok_bot() -> None:
    """Demo-bot: pobiera i wypisuje tytuł przykładowego sklepu."""
    title = get_shop_title("https://www.tiktok.com/@example/shop")
    if title:
        print("👀  Tytuł testowy z TikTok-bota:", title)
    else:
        print("❌  Nie udało się pobrać tytułu – sprawdź selektor lub URL")
