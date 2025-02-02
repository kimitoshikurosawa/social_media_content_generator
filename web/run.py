# run.py
from web import create_app
from database import init_db  # Fonction qui crée les tables

# Initialiser la base de données
init_db()

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
