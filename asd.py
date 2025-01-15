import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print(f"GOOGLE_API_KEY: {GOOGLE_API_KEY}")
