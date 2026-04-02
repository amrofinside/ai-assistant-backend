import os
from dotenv import load_dotenv

load_dotenv()
postgres_db_url = os.getenv("POSTGRES_DATABASE_URL")
resend_api_key = os.getenv("RESEND_API_KEY")

