
## SELOEDU 
Este projeto foi construido usando Python e Flask, para  a implementação inicial, seguindo o especificado nas atividades.
---

# 1 atividade-desenvolvimento-web
```
Nesta atividade, você irá implementar as rotas iniciais da aplicação SELOEDU, iniciaremos  pelo gerenciamento de usuários.

A estrutura da tabela deve seguir a definição:        users = [{"id": "id","nome": "nome","email": "email", "perfil": "perfil","status": "status"}]

GET /                           Retorna uma mensagem de boas-vindas.
GET /users                      Lista todos os usuários.
GET /id_user/{id}               Retorna usuário pelo ID ou erro se não encontrado.
POST /add_user                  Adiciona um novo usuário.
DELETE /delete_user/{id}        Remove usuário pelo ID.
PUT /update_user/{id}           Atualiza os dados de um usuário existente.
```


Recife, 09 de Setembro de 2025

---

# 2 atividade-desenvolvimento-web
```
Nesta atividade, você deverá atualizar a aplicação para criar uma nova página users.html que exiba uma tabela com informações dos usuários. O foco é apenas na renderização dos dados, sem estilização nesta etapa. Para isso, siga as orientações:

users = [{"id": id, "nome": "nome", "email": "email", "perfil": "perfil", "status": "status"}]
Obs: A tabela users deve conter pelo menos 7 registros

SELOEDU/
 ├── app.py          
 └── templates/      
      └── index.html
Criar o arquivo users.html dentro da pasta templates/.
Definir no app.py uma rota /users que envie uma lista de dicionários com os usuários.
Renderizar a tabela no users.html para a exibindo os campos: .
Manter a organização da estrutura do projeto conforme já trabalhado em sala de aula.

```

Recife, 11 de Setembro de 2025

---

# 3 atividade-desenvolvimento-web
```
A DevwebSolutions está lançando a SELOEDU, uma aplicação web voltada para o gerenciamento de treinamentos. A equipe de desenvolvimento precisa estruturar as interfaces iniciais do sistema e a navegação entre elas, criando a base para futuras funcionalidades.

O sistema deverá conter:

Página inicial (home.html)

Exibir a mensagem de boas-vindas: "Bem-vindo ao SELOEDU – Seu gerenciador de aplicação de treinamentos."
Exibir a label "Faça login para acessar o painel."

Exibir um botão com a label "Entrar"

Página inicial (login.html)

Exibir o título Login.
Ter os campos E-mail e Senha.
Disponibilizar o botão Entrar, que ao ser acionado redireciona para a página inicial (simulação de login neste momento).

Requisitos

Criar as interfaces (HTML) com as definições acima.
Garantir a interação entre as telas: o botão da página inicial deve levar para o login, e o botão de login deve retornar para a home.
Usar apenas HTML, CSS e Flask para renderizar as páginas.
Não utilizar frameworks de estilização (Bootstrap, Tailwind, etc.).

Entrega

O projeto deve ser mantido no GitHub.
A entrega no Classroom será o link do repositório GitHub contendo a estrutura abaixo.

Estrutura do projeto

SELOEDU/
├── static/
│   └── custom.css  
├── templates/
│   ├── auth/
│   │   └── login.html
│   └── home.html
└── app.py

```
Recife, 17 de Setembro de 2025

Atividades: Prof° **Jose Mauricio Matapi da Silva** 

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
python app.py ou
flask run
```

---


## A API estará disponível em:
 
http://127.0.0.1:5000





Recife, 09 de Setembro de 2025

**Antônio Macena** [LinkedIn](https://www.linkedin.com/in/antonio-macena/)