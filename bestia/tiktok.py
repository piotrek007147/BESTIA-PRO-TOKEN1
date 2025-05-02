from bs4 import BeautifulSoup
from .core import fetch


def get_shop_title(shop_url: str) -> str | None:
    """
    Zwraca tytuł sklepu z TikTok Shop (<h1.shop-title>) lub None,
    jeśli elementu nie ma.
    """
    soup: BeautifulSoup = fetch(shop_url)
    node = soup.select_one("h1.shop-title")
    if node is None:
        print(f"⚠️  Nie znaleziono <h1.shop-title> na stronie: {shop_url}")
        return None
    return node.text.strip()


def run_tiktok_bot() -> None:
    """Demo-bot: pobiera i wypisuje tytuł przykładowego sklepu."""
    title = get_shop_title("https://www.tiktok.com/@example/shop")
    if title:
        print("👀  Tytuł testowy z TikTok-bota:", title)
    else:
        print("❌  Nie udało się pobrać tytułu – sprawdź selektor lub URL")
