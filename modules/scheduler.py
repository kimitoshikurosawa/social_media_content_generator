# modules/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def schedule_article(publication_func, article_text, publish_time):
    """
    Planifie la publication d'un article.
    publication_func: fonction à appeler pour publier l'article (ex. publish_to_facebook)
    article_text: contenu de l'article
    publish_time: datetime indiquant quand publier
    """
    scheduler.add_job(publication_func, 'date', run_date=publish_time, args=[article_text])
    print(f"Article planifié pour publication à {publish_time}")

def start_scheduler():
    scheduler.start()
