# database.py
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'articles.db')}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    category = Column(String(50))  # pour la thématique : tech, gaming, manga, etc.
    title = Column(String(255))
    content = Column(Text)
    published = Column(Boolean, default=False)
    published_at = Column(DateTime, nullable=True) # date de publication effective
    published_on = Column(String(50), nullable=True) # nom du/des réseaux sociaux
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(engine)
