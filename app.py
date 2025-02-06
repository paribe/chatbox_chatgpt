import streamlit as st
import openai

# Configuração da chave da API
chave_api = "7Y-hLrMK8R1FZlkwkRApySBKZ3crWaLT3BlbkFJosVerPDEOafdc-DRtu5MbgRh0b3mb_lqSr8lOa8fOZEvrRUtN_pUZLOUUs3U9dl3SXc0FbkhYA"
client = openai.OpenAI(api_key=chave_api)

def enviar_mensagem(mensagem):
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Escolha o modelo desejado (ou gpt-4)
        messages=[{"role": "user", "content": mensagem}]
    )
    return resposta.choices[0].message.content

# Interface Web com Streamlit
st.title("Chat com OpenAI")
st.write("Digite sua pergunta abaixo e receba uma resposta do ChatGPT.")

mensagem = st.text_area("Digite sua mensagem:")

if st.button("Enviar"):
    if mensagem.strip():
        resposta = enviar_mensagem(mensagem)
        st.subheader("Resposta:")
        st.write(resposta)
    else:
        st.warning("Por favor, digite uma mensagem antes de enviar.")