from bestia.core import fetch

def run_tiktok_bot():
    soup = fetch("https://httpbin.org/html")
    print("👀  Tytuł testowy z TikTok-bota:", soup.h1.text.strip())
