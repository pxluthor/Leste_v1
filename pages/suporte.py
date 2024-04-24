import pandas as pd
import streamlit as st
import pygsheets
import os


st.set_page_config(layout="wide", page_title="Leste conecta")
st.subheader(':green[LESTE CONECTA]', divider='rainbow')
st.markdown('<h1 style="text-align: center; color: green;">PROCEDIMENTOS - SUPORTE TÉCNICO</h1><br>', unsafe_allow_html=True)


@st.cache_data()
def load_data():
    credenciais = pygsheets.authorize(service_file=os.getcwd() + "/cred.json")
    base_dados = "https://docs.google.com/spreadsheets/d/1kCa7pftxJlu6xstnhwErElqe-bHkHKyLXjI7X9gdbVY"
    arquivo = credenciais.open_by_url(base_dados)

     # Carregar dados da aba SUPORTE
    aba_suporte = arquivo.worksheet_by_title("SUPORTE") 
    data_suporte = aba_suporte.get_all_values() 
    df_suporte = pd.DataFrame(data_suporte[1:], columns=data_suporte[0]) 
    df_suporte = df_suporte.drop('', axis=1, errors='ignore')  # Remover colunas vazias
    df_suporte.set_index('INDEX', inplace=True)

    return df_suporte

df_suporte = load_data()

st.sidebar.page_link("pages/home.py", label="HOME")
st.sidebar.page_link("pages/comercial.py", label="COMERCIAL")
st.sidebar.page_link("pages/financeiro.py", label="FINANCEIRO")
st.sidebar.divider()
    

st.sidebar.header('PESQUISAR SUPORTE')

select_solicity_suport = st.sidebar.multiselect('Selecione o motivo do contato!', df_suporte['SOLICITAÇÃO'].unique(),key="suporte")

if select_solicity_suport:
    df_filtrado = df_suporte[df_suporte['SOLICITAÇÃO'].isin(select_solicity_suport)]
else:
    df_filtrado = df_suporte

text_filtred =  df_filtrado['SOLICITAÇÃO'].iloc[0] 

if not df_filtrado.empty: #(empty retorna True se o df estiver vazio, 'significa que será executado se o Df filtros_dados não estiver vazio )
        
    st.markdown(f'<span style="font-size:25px;font-weight: bold">:green[{text_filtred}]</span>', unsafe_allow_html=True) 
    st.markdown('<br>', unsafe_allow_html=True)
               
       
    st.info('DESCRIÇÃO', icon="ℹ️")
    descricao = df_filtrado['DESCRIÇÃO'].iloc[0]  # Apenas o primeiro resultado, se houver vários
    st.write(descricao)
    st.divider()

        
    st.warning('REQUISITOS', icon="⚠️")
    requisitos = df_filtrado['REQUISITOS'].iloc[0]  # Apenas o primeiro resultado, se houver vários
    st.write(requisitos)
    st.divider()

        
    st.success('AÇÃO', icon="✅")
    acao = df_filtrado['AÇÃO'].iloc[0]  # Apenas o primeiro resultado, se houver vários
    st.write(acao)
    st.divider()

        
    st.error('COMENTARIO', icon="🚨")
    comentario = df_filtrado['COMENTARIO'].iloc[0]  # Apenas o primeiro resultado, se houver vários
    st.code(comentario)
    st.divider()

    st.subheader('FECHAMENTO') # Exibindo os requisitos de forma estruturada
    fechamento = df_filtrado['FECHAMENTO'].iloc[0]  # Apenas o primeiro resultado, se houver vários
    st.write(fechamento) 
else:
    #st.markdown("Escreva a solicitação no campo de busca! ")
    text_filtred =  "Escreva a solicitação no campo de busca! " 
    st.write(text_filtred)    