import streamlit as st
import sqlite3

DB_NAME = "alunos.db"

def run():
    st.header("✏️ Editar Aluno")

    # Conectar ao banco e buscar alunos
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT matricula, nome FROM alunos ORDER BY nome")
    alunos = cursor.fetchall()
    conn.close()

    if not alunos:
        st.warning("Nenhum aluno cadastrado para editar.")
        return

    # Selecionar aluno pelo nome
    nomes = [f"{matricula} - {nome}" for matricula, nome in alunos]
    selecionado = st.selectbox("Selecione o aluno para editar", nomes)
    matricula_selecionada = selecionado.split(" - ")[0]

    # Buscar dados do aluno selecionado
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos WHERE matricula=?", (matricula_selecionada,))
    aluno = cursor.fetchone()
    conn.close()

    if aluno:
        # Desempacotar dados do aluno
        (matricula, nome, n1, n2, cep, logradouro, bairro, cidade, estado, numero, complemento) = aluno

        st.subheader("Dados do Aluno")

        # Criar colunas para edição
        col1, col2 = st.columns(2)
        with col1:
            nome_novo = st.text_input("Nome", value=nome)
            n1_novo = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1, value=n1)
            n2_novo = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1, value=n2)
            cep_novo = st.text_input("CEP", value=cep)
        with col2:
            logradouro_novo = st.text_input("Logradouro", value=logradouro)
            bairro_novo = st.text_input("Bairro", value=bairro)
            cidade_novo = st.text_input("Cidade", value=cidade)
            estado_novo = st.text_input("Estado", value=estado)
            numero_novo = st.text_input("Número", value=numero)
            complemento_novo = st.text_input("Complemento", value=complemento)

        # Botão para salvar alterações
        if st.button("Salvar Alterações"):
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE alunos SET
                    nome=?, n1=?, n2=?, cep=?, logradouro=?, bairro=?, cidade=?, estado=?, numero=?, complemento=?
                WHERE matricula=?
            """, (
                nome_novo, n1_novo, n2_novo, cep_novo, logradouro_novo, bairro_novo,
                cidade_novo, estado_novo, numero_novo, complemento_novo, matricula_selecionada
            ))
            conn.commit()
            conn.close()
            st.success(f"Aluno {nome_novo} atualizado com sucesso!")
