import sqlite3
import os

pasta_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_banco = os.path.join(pasta_projeto, "database", "helpdesk.db")

conexao = sqlite3.connect(caminho_banco)

print("Conectado ao banco com sucesso!")

conexao.close()