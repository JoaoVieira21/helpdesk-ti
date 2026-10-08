from flask import Flask, jsonify, send_from_directory, request, session
from werkzeug.security import check_password_hash
import sqlite3
import os

app = Flask(__name__)

app.secret_key = "chave-secreta-helpdesk"

pasta_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_banco = os.path.join(pasta_projeto, "database", "helpdesk.db")


# =========================
# PÁGINA PRINCIPAL
# =========================

@app.route("/")
def inicio():
    return send_from_directory("../frontend", "index.html")


@app.route("/style.css")
def estilo():
    return send_from_directory("../frontend", "style.css")


@app.route("/script.js")
def javascript():
    return send_from_directory("../frontend", "script.js")


# =========================
# LOGIN
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    # Abrir página de login
    if request.method == "GET":
        return send_from_directory("../frontend", "login.html")

    # Receber dados do formulário
    dados = request.get_json()

    email = dados["email"]
    senha = dados["senha"]

    # Conectar ao banco
    conexao = sqlite3.connect(caminho_banco)
    conexao.row_factory = sqlite3.Row

    cursor = conexao.cursor()

    # Procurar usuário pelo e-mail
    cursor.execute(
        "SELECT * FROM usuarios_login WHERE email = ?",
        (email,)
    )

    usuario = cursor.fetchone()

    conexao.close()

    # Verificar usuário e senha
    if usuario and check_password_hash(usuario["senha"], senha):

        session["usuario_id"] = usuario["id"]
        session["usuario_nome"] = usuario["nome"]
        session["usuario_tipo"] = usuario["tipo"]

        return jsonify({
            "sucesso": True,
            "mensagem": "Login realizado com sucesso!"
        })

    return jsonify({
        "sucesso": False,
        "mensagem": "E-mail ou senha incorretos."
    }), 401


# Arquivo CSS do login
@app.route("/login.css")
def login_css():
    return send_from_directory("../frontend", "login.css")


# Arquivo JavaScript do login
@app.route("/login.js")
def login_javascript():
    return send_from_directory("../frontend", "login.js")


# =========================
# CHAMADOS
# =========================

@app.route("/chamados", methods=["GET", "POST"])
def listar_chamados():

    # Criar novo chamado
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

    # Listar chamados
    conexao = sqlite3.connect(caminho_banco)
    conexao.row_factory = sqlite3.Row

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM chamados")

    chamados = cursor.fetchall()

    conexao.close()

    return jsonify([
        dict(chamado)
        for chamado in chamados
    ])


# =========================
# ALTERAR STATUS
# =========================

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


# =========================
# INICIAR SERVIDOR
# =========================

if __name__ == "__main__":
    app.run(debug=True)