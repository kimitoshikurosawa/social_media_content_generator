# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration IMAP pour Gmail
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993

# Flux RSS par thématique
RSS_FEEDS = {
    "tech": "https://news.google.com/rss/search?q=technologies",
    "gaming": "https://news.google.com/rss/search?q=gaming",
    "manga": "https://news.google.com/rss/search?q=manga+anime"
}

# Sites à scraper par thématique (remplacez par vos URLs cibles)
SCRAPE_SITES = {
    "tech": [
        os.getenv("SCRAPE_TECH_1", "https://techcrunch.com/"),
        os.getenv("SCRAPE_TECH_2", "https://www.theverge.com/tech")
    ],
    "gaming": [
        os.getenv("SCRAPE_GAMING_1", "https://www.ign.com/"),
        os.getenv("SCRAPE_GAMING_2", "https://www.gamespot.com/")
    ],
    "manga": [
        os.getenv("SCRAPE_MANGA_1", "https://www.animenewsnetwork.com/"),
        os.getenv("SCRAPE_MANGA_2", "https://myanimelist.net/")
    ]
}

# Configuration Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configuration Facebook
FB_PAGE_ID = os.getenv("FB_PAGE_ID")
FB_ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")

# Autres configurations (par exemple, planning de publication) peuvent être ajoutées ici
