import streamlit as st
import sqlite3
import pandas as pd

def run():
    conn = sqlite3.connect("alunos.db")
    df = pd.read_sql_query("SELECT * FROM alunos", conn)
    conn.close()

    st.title("Lista de Alunos")
    st.table(df)  # ou st.table(df)

run()