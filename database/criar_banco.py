import sqlite3
import os

pasta_atual = os.path.dirname(os.path.abspath(__file__))

caminho_banco = os.path.join(pasta_atual, "helpdesk.db")
caminho_sql = os.path.join(pasta_atual, "database.sql")

conexao = sqlite3.connect(caminho_banco)

with open(caminho_sql, "r", encoding="utf-8") as arquivo:
    script_sql = arquivo.read()

conexao.executescript(script_sql)

conexao.close()

print("Banco de dados criado com sucesso!")