from fastapi import FastAPI, HTTPException

app = FastAPI(title="SELOEDU")

# Base de dados inicial em memória
users = [
    {"id": "1", "nome": "Alice", "email": "alice@email.com", "perfil": "admin", "status": "ativo"},
    {"id": "2", "nome": "Bruno", "email": "bruno@email.com", "perfil": "aluno", "status": "inativo"},
]

# Rota raiz
@app.get("/")
def welcome():
    return {"mensagem": "Bem-vindo à API SELOEDU"}

# Listar todos os usuários
@app.get("/todos")
def listar_usuarios():
    return {"usuarios": users}

# Buscar usuário por ID
@app.get("/id_user/{id}")
def buscar_usuario(id: str):
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Adicionar usuário
@app.post("/add_user")
def adicionar_usuario(user: dict):
    for u in users:
        if u["id"] == user["id"]:
            raise HTTPException(status_code=400, detail="ID já existente")
    users.append(user)
    return {"mensagem": "Usuário adicionado com sucesso", "usuario": user}

# Deletar usuário
@app.delete("/delete_user/{id}")
def deletar_usuario(id: str):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return {"mensagem": "Usuário removido com sucesso"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Atualizar usuário
@app.put("/update_user/{id}")
def atualizar_usuario(id: str, novo_user: dict):
    for index, user in enumerate(users):
        if user["id"] == id:
            users[index].update(novo_user)
            return {"mensagem": "Usuário atualizado com sucesso", "usuario": users[index]}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
