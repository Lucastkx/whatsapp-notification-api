from dotenv import load_dotenv
import os
from supabase import create_client

resultado = load_dotenv()

print("Arquivo carregado?", resultado)
print("Diretório atual:", os.getcwd())



url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)
resposta = supabase.table("contatos").select("*").execute()


print(resposta.data)
print("Conexao realizada com sucesso")

#print("URL:", os.getenv("https://mnmsnfjyuwkeppvdouxw.supabase.co"))
#print("KEY:", os.getenv("sb_publishable_pOe-lei8-X0FehtC-WpxBA_1iVZg_ms"))


##enviar_mensagem = (contatos)

#def buscar_contatos():