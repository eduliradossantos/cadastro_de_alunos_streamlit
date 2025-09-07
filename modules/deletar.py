# modules/deletar.py
import streamlit as st
import sqlite3

DB_NAME = "alunos.db"

def run():
    st.header("🗑️ Deletar Aluno")

    # Conectar ao banco e buscar alunos
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT matricula, nome FROM alunos ORDER BY nome")
    alunos = cursor.fetchall()
    conn.close()

    if not alunos:
        st.warning("Nenhum aluno cadastrado para deletar.")
        return

    # Criar lista de nomes e matrículas para validação
    nomes_matriculas = {f"{matricula}": nome for matricula, nome in alunos}
    nomes_matriculas.update({nome: nome for matricula, nome in alunos})

    # Input para digitar aluno
    aluno_input = st.text_input("Digite a matrícula ou o nome do aluno que deseja deletar")

    if st.button("Deletar Aluno"):
        aluno_input = aluno_input.strip()
        if aluno_input in nomes_matriculas:
            # Buscar matrícula correspondente
            matricula_deletar = aluno_input if aluno_input in nomes_matriculas and aluno_input.startswith("A") else None
            if not matricula_deletar:
                # Buscar matrícula pelo nome
                for matricula, nome in nomes_matriculas.items():
                    if nome == aluno_input:
                        matricula_deletar = matricula
                        break

            if matricula_deletar:
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM alunos WHERE matricula=?", (matricula_deletar,))
                conn.commit()
                conn.close()
                st.success(f"Aluno {aluno_input} deletado com sucesso!")
            else:
                st.error("Não foi possível encontrar a matrícula do aluno.")
        else:
            st.error("Aluno não encontrado. Digite corretamente o nome ou matrícula.")
