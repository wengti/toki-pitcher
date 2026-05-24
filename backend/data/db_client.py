from dotenv import load_dotenv
import os

from supabase import Client, create_client

load_dotenv(override=True)


def create_supabase_client() -> Client:
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    return create_client(url, key)
