import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
MONGO_DB = os.getenv("MONGO_DB", "test")
MONGO_HOST = os.getenv("MONGO_HOST", "0.0.0.0")
MONGO_PORT = os.getenv("MONGO_PORT", 27020)
MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
