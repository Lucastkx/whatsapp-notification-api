from dotenv import load_dotenv
import os
import requests

load_dotenv()

def enviar_mensagem(numero, mensagem):

    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")

    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"

    payload = {
        "phone": numero,
        "message": mensagem
    }

    response = requests.post(url, json=payload)

    return response
    