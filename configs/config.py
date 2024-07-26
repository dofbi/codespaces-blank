import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Charger les URLs depuis le fichier urls.txt
def load_urls(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

URLs = load_urls('urls.txt')

# Paramètres de configuration
MODEL_NAME = os.getenv("MODEL_NAME", "phi3")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 7500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
