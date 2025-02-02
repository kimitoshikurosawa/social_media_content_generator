# Social Media Content Generator

Ce projet est une application open source qui permet de générer des articles pour réseaux sociaux en combinant du contenu scrappé et des flux RSS. Il utilise l'API Gemini pour la génération de texte et intègre une interface web Flask pour la prévisualisation et la publication sur diverses plateformes (Facebook, Instagram, LinkedIn, etc.).

## Fonctionnalités

- Récupération de contenu via scraping et flux RSS
- Génération d'articles concis et publiables en tenant compte de l'historique des sujets déjà traités
- Interface web pour prévisualiser les articles par thématique
- Publication sur réseaux sociaux via des routes dédiées
- Base de données SQLite pour sauvegarder les articles avec des champs comme `is_published` et `published_on`

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/kimitoshikurosawa/social_media_content_generator.git
   
2. Créez un environnement virtuel et installez les dépendances :
    ```bash
    cd social-media-content-generator
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. Créez un fichier .env à la racine avec vos variables d'environnement (voir .env.example pour la liste) :
    ```bash
    cp .env.example .env
   
4. Lancez l'application :
    ```bash
    python web/run.py
      
## Utilisation

1. Rendez-vous sur http://localhost:5000 pour accéder à l'interface web
2. Cliquez sur "Générer" pour obtenir des articles
3. Prévisualisez les articles et cliquez sur "Publier" pour les partager sur les réseaux sociaux
4. Consultez la base de données SQLite pour voir les articles sauvegardés
5. Modifiez les paramètres de scraping et de génération dans `config.py`
6. Personnalisez le design de l'interface web en modifiant les templates HTML dans `web/templates`
7. Ajoutez des routes pour d'autres réseaux sociaux dans `web/routes.py`
8. Ameliorez la génération de texte en utilisant la documentation de l'API Gemini (https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb)
9. Intégrez des services tiers pour enrichir le contenu généré (ex. API de traduction, de génération d'images, etc.)
10. Déployez l'application sur un serveur pour automatiser la publication d'articles

## Contribution

Consultez le fichier CONTRIBUTING.md pour savoir comment contribuer à ce projet.

## Licence

Ce projet est distribué sous la licence MIT. Pour plus d'informations, consultez le fichier LICENSE.
