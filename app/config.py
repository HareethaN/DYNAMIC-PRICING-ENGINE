import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/pricing")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
