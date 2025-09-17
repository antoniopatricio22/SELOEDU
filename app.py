from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base de dados inicial em memória
users = [
    {"id": "1", "nome": "Alice", "email": "alice@email.com", "perfil": "admin", "status": "ativo"},
    {"id": "2", "nome": "Bruno", "email": "bruno@email.com", "perfil": "aluno", "status": "inativo"},
    {"id": "3", "nome": "Carlos", "email": "carlos@email.com", "perfil": "professor", "status": "ativo"},
    {"id": "4", "nome": "Diana", "email": "diana@email.com", "perfil": "aluno", "status": "ativo"},
    {"id": "5", "nome": "Eduardo", "email": "eduardo@email.com", "perfil": "admin", "status": "inativo"},
    {"id": "6", "nome": "Fernanda", "email": "fernanda@email.com", "perfil": "professor", "status": "ativo"},
    {"id": "7", "nome": "Gabriel", "email": "gabriel@email.com", "perfil": "aluno", "status": "ativo"},
]

@app.route("/")
def welcome():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("auth/login.html")

@app.route("/users")
def listar_usuarios():
    return render_template("users.html", usuarios=users)

@app.route("/id_user/<id>")
def buscar_usuario(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)
    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route("/add_user", methods=["POST"])
def adicionar_usuario():
    user = request.json
    for u in users:
        if u["id"] == user.get("id"):
            return jsonify({"erro": "ID já existente"}), 400
    users.append(user)
    return jsonify({"mensagem": "Usuário adicionado com sucesso", "usuario": user})

@app.route("/delete_user/<id>", methods=["DELETE"])
def deletar_usuario(id):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return jsonify({"mensagem": "Usuário removido com sucesso"})
    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route("/update_user/<id>", methods=["PUT"])
def atualizar_usuario(id):
    novo_user = request.json
    for index, user in enumerate(users):
        if user["id"] == id:
            users[index].update(novo_user)
            return jsonify({"mensagem": "Usuário atualizado com sucesso", "usuario": users[index]})
    return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
