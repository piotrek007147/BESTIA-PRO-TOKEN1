import requests
from bs4 import BeautifulSoup

def fetch(url: str, timeout: int = 10) -> BeautifulSoup:
    """Pobiera stronę i zwraca obiekt BeautifulSoup."""
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")
