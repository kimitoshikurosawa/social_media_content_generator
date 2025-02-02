# modules/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_content(url):
    """
    Scrape le contenu d'un site web à partir d'une URL donnée.
    Extrait le texte de tous les paragraphes <p>.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Bot/1.0; +http://example.com/bot)"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            paragraphs = soup.find_all("p")
            content = "\n".join(p.get_text() for p in paragraphs)
            return content
        else:
            print(f"Erreur lors de la récupération de la page {url}: {response.status_code}")
            return ""
    except Exception as e:
        print(f"Exception lors du scraping de {url}: {e}")
        return ""

def scrape_multiple_sites(url_list):
    """
    Scrape plusieurs sites à partir d'une liste d'URLs et retourne
    le contenu combiné.
    """
    all_content = ""
    for url in url_list:
        content = scrape_content(url)
        if content:
            all_content += f"\n---\nContenu extrait de {url}:\n" + content
    return all_content
