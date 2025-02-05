import openai

chave_api="xxxxxx"

#openai.api_key= chave_api

# Criar um cliente OpenAI
client = openai.OpenAI(api_key=chave_api)

def enviar_mensagem(mensagem):
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Escolha o modelo desejado (ou gpt-4)
        messages=[{"role": "user", "content": mensagem}]
    )
    return resposta.choices[0].message.content

print(enviar_mensagem("como especialista me fale sobre comando pyhton para concatenar dois dataframes pode me ajudar"))