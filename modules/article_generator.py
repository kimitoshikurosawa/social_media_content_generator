# modules/article_generator.py
import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure l'API Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_article(scraped_content, feed_articles):
    """
    Construit un prompt combinant le contenu scrappé et les articles RSS,
    et demande au modèle Gemini de rédiger une publication pour réseaux sociaux.

    Les consignes demandent :
      - Un titre accrocheur
      - Une introduction concise
      - Des paragraphes clairs avec des sauts de ligne
      - Un style dynamique, direct et adapté aux réseaux sociaux
      - L'utilisation de hashtags ou emojis pertinents (optionnel)
      - Une longueur réduite (environ 200 à 300 mots maximum)
      - Une rédaction sur un seul sujet en fonction de la thématique
    """
    # Créer un résumé des informations issues du flux RSS, sans format Markdown excessif
    feed_info = "\n".join([f"{item['title']}: {item['summary']}" for item in feed_articles])

    # Nouveau prompt amélioré pour un format publication réseaux sociaux
    prompt = (
        "Vous êtes un journaliste spécialisé en tech, manga et gaming, et vous devez rédiger une publication destinée aux réseaux sociaux. "
        "Votre objectif est de produire un texte concis (entre 200 et 300 mots) et dynamique, qui soit immédiatement publiable. "
        "Le texte doit comporter un titre accrocheur, une introduction percutante, des paragraphes clairs avec des sauts de ligne, "
        "et adopter un ton moderne et direct. Vous pouvez ajouter quelques hashtags pertinents et des emojis si cela renforce l'engagement, "
        "mais n'en abusez pas. Veuillez rédiger sur un seul sujet (sélectionné à partir des informations fournies) afin de garantir la cohérence. \n\n"
        "Utilisez des retours à la ligne pour séparer les paragraphes et veillez à ce que le texte ne soit pas un bloc continu. \n\n"
        "Informations issues des données scrappées :\n"
        f"{scraped_content}\n\n"
        "Informations issues des flux RSS :\n"
        f"{feed_info}\n\n"
        "Rédigez la publication de manière cohérente, en respectant les consignes ci-dessus."
    )

    try:
        response = model.generate_content(prompt)
        article_text = response.text
        return article_text
    except Exception as e:
        print("Erreur lors de la génération de l'article :", e)
        return ""



def generate_article_with_history(scraped_content, feed_articles, history):
    """
    Construit un prompt qui intègre l'historique des articles déjà générés (provenant de la base de données)
    afin d'éviter de traiter un sujet déjà couvert, et demande au modèle de rédiger une publication pour réseaux sociaux.

    Parameters:
      - scraped_content : contenu extrait par scraping (texte brut)
      - feed_articles   : liste d'articles provenant du flux RSS (dictionnaires avec 'title' et 'summary')
      - history         : liste de chaînes représentant, par exemple, les titres des articles déjà publiés

    Returns:
      - article_text    : texte généré par Gemini, formaté
    """
    # Créer une synthèse de l'historique
    if history:
        history_summary = "\n".join([f"- {h}" for h in history])
    else:
        history_summary = "Aucun sujet précédent n'a été traité."

    # Créer un résumé des informations issues du flux RSS
    feed_info = "\n".join([f"{item['title']}: {item['summary']}" for item in feed_articles])

    # Nouveau prompt amélioré pour éviter la redondance de sujet
    prompt = (
        "Vous êtes un journaliste spécialisé en tech, manga et gaming, et vous devez rédiger une publication pour les réseaux sociaux. "
        "Votre objectif est de générer un texte concis (entre 200 et 300 mots) et dynamique, immédiatement publiable, sur un sujet unique. "
        "Il est impératif que le sujet traité soit différent de ceux déjà publiés. "
        "Voici l'historique des sujets déjà traités pour cette thématique :\n"
        f"{history_summary}\n\n"
        "À partir des informations suivantes, rédigez un nouvel article sur un sujet différent, en respectant les consignes suivantes :\n"
        "  - Un titre accrocheur\n"
        "  - Une introduction percutante\n"
        "  - Des paragraphes clairs, séparés par deux retours à la ligne\n"
        "  - Un style moderne et adapté aux réseaux sociaux (vous pouvez ajouter quelques hashtags ou emojis pertinents)\n\n"
        "Informations issues du scraping :\n"
        f"{scraped_content}\n\n"
        "Informations issues des flux RSS :\n"
        f"{feed_info}\n\n"
        "Assurez-vous de ne pas reprendre un sujet déjà abordé dans la liste ci-dessus."
    )

    try:
        response = model.generate_content(prompt)
        article_text = response.text
        return article_text
    except Exception as e:
        print("Erreur lors de la génération de l'article :", e)
        return ""