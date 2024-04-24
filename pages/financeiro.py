import pandas as pd
import streamlit as st
import pygsheets
import os
import streamlit as st



st.set_page_config(layout="wide", page_title="Leste conecta")
st.subheader(':green[LESTE CONECTA]', divider='rainbow')
st.markdown('<h1 style="text-align: center; color: green;">PROCEDIMENTOS - FINANCEIRO</h1><br>', unsafe_allow_html=True)

@st.cache_data()
def load_data():
    credenciais = pygsheets.authorize(service_file=os.getcwd() + "/cred.json")
    base_dados = "https://docs.google.com/spreadsheets/d/1kCa7pftxJlu6xstnhwErElqe-bHkHKyLXjI7X9gdbVY"
    arquivo = credenciais.open_by_url(base_dados)

    # Carregar dados da aba FINANCEIRO
    aba_financy = arquivo.worksheet_by_title("FINANCEIRO") 
    data_financy = aba_financy.get_all_values() 
    df_financy = pd.DataFrame(data_financy[1:], columns=data_financy[0]) 
    df_financy = df_financy.drop('', axis=1, errors='ignore')  # Remover colunas vazias
    df_financy.set_index('INDEX', inplace=True)

    return df_financy

df_financy = load_data()

st.sidebar.page_link("pages/home.py", label="HOME")
st.sidebar.page_link("pages/comercial.py", label="COMERCIAL")
st.sidebar.page_link("pages/suporte.py", label="SUPORTE")
st.sidebar.divider()

st.sidebar.header('PESQUISAR FINANCEIRO')
select_solicity2 = st.sidebar.multiselect('Selecione o motivo do contato!', df_financy['SOLICITAÇÃO'].unique())

if select_solicity2:
    df_filtrado = df_financy[df_financy['SOLICITAÇÃO'].isin(select_solicity2)]
else:
    df_filtrado = df_financy

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
    st.write("Escreva a solicitação no campo de busca!")
