# web/__init__.py
import os

from flask import Flask
from database import init_db

from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("APP_SECRET")

    # On utilise le contexte de l'application pour initialiser la base
    with app.app_context():
        init_db()

    from web.routes import main
    app.register_blueprint(main)
    return app
