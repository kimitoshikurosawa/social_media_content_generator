# web/routes.py
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for

from modules.publisher import publish_to_facebook, publish_to_instagram, publish_to_twitter, publish_to_linkedin
from modules.scraper import scrape_multiple_sites
from modules.rss_fetcher import get_feed_data
from modules.article_generator import generate_article, generate_article_with_history
from config import SCRAPE_SITES, RSS_FEEDS
from database import session, Article

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Pour chaque thématique, générer et sauvegarder un article
        for theme in RSS_FEEDS.keys():
            rss_url = RSS_FEEDS[theme]
            # Récupération des sites à scraper sous forme de liste
            site_list = SCRAPE_SITES.get(theme, [])
            feed_articles = get_feed_data(rss_url)
            scraped_text = scrape_multiple_sites(site_list) if site_list else ""

            generated_article = generate_article(scraped_text, feed_articles)
            if not generated_article:
                print(f"La génération de l'article pour la thématique {theme} a échoué.")
                continue

            # Créer et sauvegarder l'article en base
            article_record = Article(
                category=theme,
                title=f"Article pour {theme.capitalize()}",
                content=generated_article
            )
            session.add(article_record)
        try:
            session.commit()
            print("Articles sauvegardés en base avec succès.")
        except Exception as e:
            print("Erreur lors de l'enregistrement en base :", e)
            session.rollback()
        # Après génération, redirige vers la page GET pour prévisualiser
        return redirect(url_for('main.index'))

    # Pour une requête GET, lire les articles sauvegardés, triés par date décroissante
    articles = session.query(Article).order_by(Article.created_at.desc()).all()

    # Vous pouvez regrouper par thématique pour l'affichage
    articles_by_theme = {}
    for article in articles:
        articles_by_theme.setdefault(article.category, []).append(article)

    return render_template("index.html", articles=articles_by_theme)

@main.route("/generate_by_category", methods=["POST"])
def generate_article_theme():
    # Récupérer l'historique des articles déjà publiés pour la thématique 'theme'
    # On récupère par exemple les 5 derniers titres publiés (is_published==True)
    theme = request.form.get("category")
    history_articles = (
        session.query(Article.title)
        .filter(Article.category == theme)
        .order_by(Article.published_on.desc())
        .limit(5)
        .all()
    )
    # Transforme le résultat en liste de chaînes
    history = [title for (title,) in history_articles]

    # Récupérer les données de scraping et RSS pour la thématique
    site_list = SCRAPE_SITES.get(theme, [])
    scraped_content = scrape_multiple_sites(site_list) if site_list else ""
    feed_articles = get_feed_data(RSS_FEEDS.get(theme, ""))

    # Générer un nouvel article en passant l'historique
    article_text = generate_article_with_history(scraped_content, feed_articles, history)

    # Ici, vous pouvez sauvegarder l'article dans la base avec is_published==False par exemple,
    # et l'afficher dans votre page de prévisualisation.
    new_article = Article(
        category=theme,
        title="Nouveau sujet pour " + theme.capitalize(),
        content=article_text,
        created_at=datetime.utcnow()
    )
    session.add(new_article)
    session.commit()

    return redirect(url_for("main.index"))
# routes to publish articles on Facebook, Instagram, etc.

# route for facebook publish
@main.route("/publish/facebook/<int:article_id>", methods=["POST"])
def publish_fb(article_id):
    article = session.query(Article).get(article_id)
    if not article:
        return "Article non trouvé", 404

    # Appel à la fonction de publication sur Facebook
    publish_to_facebook(article.content)
    return "Article publié sur Facebook avec succès."

# route for instagram publish

@main.route("/publish/instagram/<int:article_id>", methods=["POST"])
def publish_insta(article_id):
    article = session.query(Article).get(article_id)
    if not article:
        return "Article non trouvé", 404

    # Appel à la fonction de publication sur Instagram
    publish_to_instagram(article.content)
    return "Article publié sur Instagram avec succès."

# route for twitter publish

@main.route("/publish/twitter/<int:article_id>", methods=["POST"])
def publish_twitter(article_id):
    article = session.query(Article).get(article_id)
    if not article:
        return "Article non trouvé", 404

    # Appel à la fonction de publication sur Twitter
    publish_to_twitter(article.content)
    return "Article publié sur Twitter avec succès."

# route for linkedin publish
@main.route("/publish/linkedin/<int:article_id>", methods=["POST"])
def publish_linkedin(article_id):
    article = session.query(Article).get(article_id)
    if not article:
        return "Article non trouvé", 404

    # Appel à la fonction de publication sur LinkedIn
    publish_to_linkedin(article.content)
    return "Article publié sur LinkedIn avec succès."



