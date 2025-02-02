# modules/rss_fetcher.py
import feedparser

def get_feed_data(feed_url):
    """Récupère et parse un flux RSS, retourne une liste d'articles (titre, résumé, lien)."""
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary if hasattr(entry, "summary") else ""
        })
    return articles
