from flask import Flask, jsonify, send_from_directory, request
import sqlite3
import os

app = Flask(__name__)

pasta_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_banco = os.path.join(pasta_projeto, "database", "helpdesk.db")


@app.route("/")
def inicio():
    return send_from_directory("../frontend", "index.html")


@app.route("/style.css")
def estilo():
    return send_from_directory("../frontend", "style.css")


@app.route("/script.js")
def javascript():
    return send_from_directory("../frontend", "script.js")


@app.route("/chamados", methods=["GET", "POST"])
def listar_chamados():

    if request.method == "POST":

        dados = request.get_json()

        titulo = dados["titulo"]
        descricao = dados["descricao"]
        prioridade = dados["prioridade"]

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
            titulo,
            descricao,
            prioridade,
            "Aberto",
            1,
            "João Pedro"
        ))

        conexao.commit()
        conexao.close()

        return jsonify({
            "mensagem": "Chamado aberto com sucesso!"
        })

    conexao = sqlite3.connect(caminho_banco)
    conexao.row_factory = sqlite3.Row

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM chamados")

    chamados = cursor.fetchall()

    conexao.close()

    return jsonify([dict(chamado) for chamado in chamados])

@app.route("/chamados/<int:id>", methods=["PUT"])
def atualizar_status(id):

    dados = request.get_json()
    novo_status = dados["status"]

    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE chamados
        SET status = ?
        WHERE id = ?
    """, (novo_status, id))

    conexao.commit()
    conexao.close()

    return jsonify({
        "mensagem": "Status atualizado com sucesso!"
    })
if __name__ == "__main__":
    app.run(debug=True)