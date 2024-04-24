
import streamlit as st

st.set_page_config(layout="wide", page_title="Leste conecta")
st.subheader(':green[LESTE CONECTA]', divider='rainbow')
st.markdown('<h1 style="text-align: center; color: green;">BEM VINDO A PÁGINA INICIAL</h1><br>', unsafe_allow_html=True)


st.sidebar.page_link("pages/comercial.py", label="🛒 COMERCIAL")
st.sidebar.page_link("pages/financeiro.py", label="💲 FINANCEIRO")
st.sidebar.page_link("pages/suporte.py", label="🛠️ SUPORTE")
st.sidebar.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.header("CONSULTAR VIABILIDADE")
    st.link_button("VIABILIDADE", "https://www.lestetelecom.com.br/viabilidade")

with col2:
    st.header("CONSULTA FAQ")
    st.link_button("FAQ - LESTE", "https://www.lestetelecom.com.br/faq")

with col3:
    st.header("LESTE MOVEL")
    st.link_button("IR", "https://www.lestemovel.com.br/")

st.divider()

    
   
    