# atividade-desenvolvimento-web
SELOEDU 
Este projeto foi construido usando Python e FastAPI, para  a implementação inicial, conforme especificado na atividade.
```
Nesta atividade, você irá implementar as rotas iniciais da aplicação SELOEDU, iniciaremos  pelo gerenciamento de usuários.

A estrutura da tabela deve seguir a definição:        users = [{"id": "id","nome": "nome","email": "email", "perfil": "perfil","status": "status"}]

GET /                                      Retorna uma mensagem de boas-vindas.
GET /todos                            Lista todos os usuários.
GET /id_user/{id}                  Retorna usuário pelo ID ou erro se não encontrado.
POST /add_user                    Adiciona um novo usuário.
DELETE /delete_user/{id}    Remove usuário pelo ID.
PUT /update_user/{id}         Atualiza os dados de um usuário existente.
```
---
Atividade: Implementação das rotas de Usuários - Prof° **Jose Mauricio Matapi da Silva** [LinkedIn]()


# Como rodar o projeto

Clone este repositório:

```
git clone https://github.com/<SEU_USUARIO>/seloedu-api.git
cd seloedu-api
```

# Crie e ative um ambiente virtual:

```
python -m venv aula
# Linux/Mac
source aula/bin/activate
# Windows
aula\Scripts\activate
```

# Instale as dependências:

```
pip install -r requirements.txt
```

# Rode o servidor:

```
uvicorn app:app --reload
```

---


## A API estará disponível em:
 
http://127.0.0.1:8000

##E a documentação interativa no Swagger UI:

http://127.0.0.1:8000/docs



Recife, 09 de Setembro de 2025

**Antônio Macena** [LinkedIn](https://www.linkedin.com/in/antonio-macena/)