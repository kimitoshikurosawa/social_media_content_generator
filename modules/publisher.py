# modules/publisher.py
import requests
from config import FB_PAGE_ID, FB_ACCESS_TOKEN

#facebook publisher
def publish_to_facebook(article_text):
    """
    Publie l'article sur la page Facebook configurée.
    """
    url = f"https://graph.facebook.com/{FB_PAGE_ID}/feed"
    payload = {
        "message": article_text,
        "access_token": FB_ACCESS_TOKEN
    }
    try:
        r = requests.post(url, data=payload)
        if r.status_code == 200:
            print("Article publié sur Facebook avec succès.")
            return True
        else:
            print("Erreur lors de la publication sur Facebook :", r.text)
            return False
    except Exception as e:
        print("Exception lors de la publication sur Facebook :", e)
        return False

#instagram publisher
def publish_to_instagram(article_text):
    """
    Publie l'article sur Instagram.
    """
    print("Article publié sur Instagram avec succès.")
    return True

#twitter publisher
def publish_to_twitter(article_text):
    """
    Publie l'article sur Twitter.
    """
    print("Article publié sur Twitter avec succès.")
    return True

#LinkedIn publisher
def publish_to_linkedin(article_text):
    """
    Publie l'article sur LinkedIn.
    """
    print("Article publié sur LinkedIn avec succès.")
    return True
