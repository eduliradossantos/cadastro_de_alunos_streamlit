import streamlit as st
from streamlit_option_menu import option_menu
import modules.adicionar as adicionar
import modules.listar as listar
import modules.editar as editar
import modules.deletar as deletar
import modules.home as home
import modules.agenteia as agente
import auth


auth.criar_tabela_usuarios()

def rerun():
    st.session_state["reload"] = not st.session_state.get("reload", False)

if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = ""

def logout():
    st.session_state.logado = False
    st.session_state.usuario = ""
    rerun()

if not st.session_state.logado:
    st.title("🔑 Sistema de Login")

    modo = st.radio("Escolha a ação:", ["Login", "Cadastrar usuário"])

    usuario_input = st.text_input("Usuário")
    senha_input = st.text_input("Senha", type="password")

    if modo == "Login":
        if st.button("Entrar"):
            if auth.verificar_login(usuario_input, senha_input):
                st.session_state.logado = True
                st.session_state.usuario = usuario_input
                st.success(f"Bem-vindo(a), {usuario_input}!")
                rerun()
            else:
                st.error("Usuário ou senha incorretos!")
    else:
        if st.button("Cadastrar"):
            if auth.cadastrar_usuario(usuario_input, senha_input):
                st.success("Usuário cadastrado com sucesso! Faça login agora.")
            else:
                st.error("Usuário já existe! Escolha outro nome.")
else:
    # Menu lateral
    with st.sidebar:
        st.write(f"👋 Olá, {st.session_state.usuario}")
        if st.button("Logout"):
            logout()

        escolha = option_menu(
            "Menu",
            ["Home", "Adicionar", "Listar", "Editar", "Deletar", "Agente de IA"],
            icons=["house", "plus-circle", "list-task", "pencil", "trash"],
            menu_icon="cast",
            default_index=0
        )

    # Conteúdo
    if escolha == "Home":
        home.run()
    elif escolha == "Adicionar":
        adicionar.run()
    elif escolha == "Listar":
        listar.run()
    elif escolha == "Editar":
        editar.run()
    elif escolha == "Deletar":
        deletar.run()
    elif escolha == "Agente de IA":
        agente.run()
