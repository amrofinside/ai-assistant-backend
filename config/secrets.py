import os
from dotenv import load_dotenv

load_dotenv()
postgres_db_url = os.getenv("POSTGRES_DATABASE_URL")


