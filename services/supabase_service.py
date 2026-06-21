from dotenv import load_dotenv
import os
from supabase import create_client

load_dotenv()

def buscar_contatos():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    supabase = create_client(url, key)

    resposta = supabase.table("contatos").select("*").execute()

    return resposta.data 