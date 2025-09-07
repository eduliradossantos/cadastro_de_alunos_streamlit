# modules/home.py
import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.stats import norm


DB_NAME = "alunos.db"

def run():
    with st.container():
        st.title("📚 Sistema de Cadastro de Alunos")
        st.header("Bem-vindo! Use o menu lateral para acessar as opções para adicionar, editar, listar e deletar.")
        st.write("Caso queira ver a análise dos dados, clique no **Dashboard** abaixo.")

    with st.expander("Dashboard"):
        conn = sqlite3.connect(DB_NAME)
        df = pd.read_sql_query("SELECT * FROM alunos", conn)
        conn.close()

        # --- Criar coluna da média ---
        df["media"] = (df["n1"] + df["n2"]) / 2

        # --- Métricas com st.metric ---
        total_alunos = len(df)
        maior_nota = df["media"].max()
        menor_nota = df["media"].min()
        media_geral = round(df["media"].mean(), 2)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total de Alunos", total_alunos)
        col2.metric("Maior Média", maior_nota)
        col3.metric("Menor Média", menor_nota)
        col4.metric("Média Geral", media_geral)

        # --- Gráfico de distribuição com curva de sino ---
        st.subheader("Distribuição das Médias (Curva de Sino)")

        # Histogram
        hist_data = np.histogram(df["media"], bins=10)
        x_hist = hist_data[1]  # bin edges
        y_hist = hist_data[0]  # counts

        # Ajustar bin center para Plotly
        x_center = (x_hist[:-1] + x_hist[1:]) / 2

        # Curva de sino (normal)
        mu, sigma = df["media"].mean(), df["media"].std()
        x_curve = np.linspace(df["media"].min(), df["media"].max(), 200)
        y_curve = norm.pdf(x_curve, mu, sigma) * len(df) * (x_hist[1]-x_hist[0])  # scale para histogram

        # Criar figura
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x_center, y=y_hist, name="Histograma", marker_color="#636EFA", opacity=0.7))
        fig.add_trace(go.Scatter(x=x_curve, y=y_curve, mode="lines", name="Curva Normal", line=dict(color="#EF553B", width=3)))

        fig.update_layout(
            xaxis_title="Média",
            yaxis_title="Quantidade de Alunos",
            template="plotly_dark",
            legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99)
        )

        st.plotly_chart(fig)

