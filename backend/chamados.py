import sqlite3
import os

pasta_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_banco = os.path.join(pasta_projeto, "database", "helpdesk.db")

conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

cursor.execute("""
    INSERT INTO chamados (
        titulo,
        descricao,
        prioridade,
        status,
        usuario_id,
        atendente
    )
    VALUES (?, ?, ?, ?, ?, ?)
""", (
    "Computador não liga",
    "O computador não apresenta imagem ao pressionar o botão de ligar.",
    "Alta",
    "Aberto",
    1,
    "João Pedro"
))

conexao.commit()
conexao.close()

print("Chamado cadastrado com sucesso!")

conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

cursor.execute("SELECT * FROM chamados")

chamados = cursor.fetchall()

print("\nChamados cadastrados:")

for chamado in chamados:
    print(chamado)

conexao.close()