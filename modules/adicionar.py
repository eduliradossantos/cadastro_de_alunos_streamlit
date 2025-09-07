# modules/adicionar.py
import streamlit as st
import sqlite3
import random
import os
import requests

DB_NAME = "alunos.db"

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep.replace('-', '')}/json/"
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            if "erro" in data:
                return None
            return {
                "logradouro": data.get("logradouro", ""),
                "bairro": data.get("bairro", ""),
                "cidade": data.get("localidade", ""),
                "estado": data.get("uf", "")
            }
        return None
    except:
        return None

def run():
    st.header("➕ Cadastrar Aluno")

    matricula = st.text_input("Digite a matrícula (exemplo do formato: A0021)", key="matricula").strip()
    nome = st.text_input("Digite o nome", key="nome").strip()
    n1 = st.number_input("Digite a primeira nota", min_value=0.0, max_value=10.0, step=0.1, key="n1")
    n2 = st.number_input("Digite a segunda nota", min_value=0.0, max_value=10.0, step=0.1, key="n2")

    # Endereço
    cep = st.text_input("Digite o CEP e clique em TAB", key="cep").strip()
    endereco = {}
    if cep:
        endereco = buscar_cep(cep)
        if endereco:
            st.success("Endereço encontrado!")
        else:
            st.error("CEP inválido ou não é de Recife/PE.")

    logradouro = st.text_input("Logradouro", value=endereco.get("logradouro", ""), key="logradouro")
    bairro = st.text_input("Bairro", value=endereco.get("bairro", ""), key="bairro")
    cidade = st.text_input("Cidade", value=endereco.get("cidade", ""), key="cidade")
    estado = st.text_input("Estado", value=endereco.get("estado", ""), key="estado")
    numero = st.text_input("Número", key="numero")
    complemento = st.text_input("Complemento", key="complemento")

    if st.button("Salvar"):
        if matricula and nome and cep and logradouro and bairro and cidade and estado and numero:
            try:
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO alunos (matricula, nome, n1, n2, cep, logradouro, bairro, cidade, estado, numero, complemento)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (matricula, nome, n1, n2, cep, logradouro, bairro, cidade, estado, numero, complemento))
                conn.commit()
                conn.close()
                st.success(f"Aluno {nome} cadastrado com sucesso!")
            except sqlite3.IntegrityError:
                st.error("Já existe um aluno com essa matrícula.")
        else:
            st.warning("Preencha todos os campos obrigatórios antes de salvar.")

run()
