import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")