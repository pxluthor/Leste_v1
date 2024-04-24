import streamlit as st
from auth import app_login, app_login2, app_login1




    
  
# AGENTE
def authenticated_menu():
    app_login()


#SUPERVISOR
def authenticated_menu2():
    app_login1()        


#COORDENAÇÂO
def authenticated_menu3():
    app_login2()    


def unauthenticated_menu():

   pass
 


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    
    if "role" not in st.session_state or st.session_state.role is None:

        pass

    elif st.session_state.role == "AGENTE":
        authenticated_menu()

    elif st.session_state.role == "SUPERVISÃO":
        authenticated_menu2()
    
    elif st.session_state.role == "COORDENAÇÃO":
        authenticated_menu3()





      
    

def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
      
        st.switch_page("app.py")
        
    menu()