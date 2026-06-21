from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem

contatos = buscar_contatos()

for contato in contatos[:3]:

    nome = contato["nome"]
    numero = contato["telefone"]

    mensagem = f"Olá, {nome} tudo bem com você?"

    response = enviar_mensagem(numero, mensagem)

    if response.status_code == 200:
        print(f"Mensagem enviada para {nome}")
    else:
        print(f"Erro ao enviar para {nome}")