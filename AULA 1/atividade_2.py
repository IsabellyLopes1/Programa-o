import streamlit as st

st.title(" Cadastro de Usuário")

nome = st.text_input("Digite seu nome completo:")

idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, value=18)

aceitou_termos = st.checkbox("Li e aceito os termos de uso")

botao_enviar = st.button("Cadastrar")

if botao_enviar:

    if aceitou_termos:
        st.success("Cadastro realizado com sucesso!")
        st.write(f"**Nome:** {nome}")
        st.write(f"**Idade:** {idade} anos")
    else:
        st.error("Você precisa aceitar os termos de uso para continuar.")