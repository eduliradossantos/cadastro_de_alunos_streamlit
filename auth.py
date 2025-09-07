import sqlite3
import hashlib

DB_NAME = "alunos.db"  # mesmo banco do app

# Criar tabela de usuários
def criar_tabela_usuarios():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Cadastrar novo usuário
def cadastrar_usuario(usuario, senha):
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha_hash))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False  # Usuário já existe

# Verificar login
def verificar_login(usuario, senha):
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha_hash))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None
