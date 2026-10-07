import sqlite3
import os

pasta_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_banco = os.path.join(pasta_projeto, "database", "helpdesk.db")

conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

cursor.execute("""
    INSERT INTO usuarios (nome, email, setor)
    VALUES (?, ?, ?)
""", ("João Pedro", "joao@empresa.com", "TI"))

conexao.commit()
conexao.close()

print("Usuário cadastrado com sucesso!")