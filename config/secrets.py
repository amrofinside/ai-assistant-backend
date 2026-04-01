import os
from dotenv import load_dotenv

load_dotenv()
postgres_host = os.getenv("POSTGRES_HOST")
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_db = os.getenv("POSTGRES_DB")
postgres_port = os.getenv("POSTGRES_PORT")

