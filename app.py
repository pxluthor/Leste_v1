import streamlit as st
from menu import menu
st.selectbox(
            "Escolha sua função:",
            [None, "AGENTE", "SUPERVISÃO", "COORDENAÇÃO"],
            key="role",
        
            )

#Inicialize st.session_state.role como  vazia
if "role" not in st.session_state:
    st.session_state.role = None

elif "role" in ["AGENTE"]:
    st.session_state.role = "AGENTE"

elif "role" in ["SUPERVISÃO"]:
    st.session_state.role = "SUPERVISÃO"    

elif "role" in ["COORDENAÇÃO"]:
    st.session_state.role = "COORDENAÇÃO"      


def set_role():
    # Função de retorno de chamada para salvar a seleção de função no estado da sessão
    st.session_state.role = st.session_state.role    

# Recupere a função do estado da sessão para inicializar o widget
#st.session_state._role = st.session_state.role





st.write(st.session_state.role) 

menu() # Renderiza o menu dinâmico!




