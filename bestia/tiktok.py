from bestia.core import fetch

def run_tiktok_bot():
    soup = fetch("https://example.com")
    print("👀  Tytuł testowy z TikTok-bota:", soup.h1.text.strip())
