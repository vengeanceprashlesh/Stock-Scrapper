import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY not found in environment variables.")
if not EMAIL_SENDER or not EMAIL_PASSWORD:
    print("Warning: Email credentials not found in environment variables.")
