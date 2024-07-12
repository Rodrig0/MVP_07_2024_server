# Projeto de Lista de Leitura

## Descrição

Este projeto é uma aplicação de lista de leitura que permite adicionar, editar e excluir livros. O frontend foi desenvolvido com Vue.js e o backend com Python e Flask. Além disso, integrei a API do Google Books para buscar livros online e utilizei o Swagger para documentar a API.

## Estrutura do Projeto

- **Client-Main**
  - Contém o frontend da aplicação desenvolvido em Vue.js.
  - Principais arquivos:
    - `index.html`: Arquivo HTML principal.
    - `src/main.js`: Arquivo de configuração do Vue.js.
    - `src/App.vue`: Componente principal do Vue.js.
    - `src/components/Books.vue`: Componente responsável pela exibição e manipulação da lista de livros.

- **Server-Main**
  - Contém o backend da aplicação desenvolvido em Python e Flask.
  - Principais arquivos:
    - `app.py`: Arquivo principal do Flask onde as rotas e configurações são definidas.
    - `db.py`: Configuração do banco de dados.
    - `resources/book.py`: Definição das rotas relacionadas aos livros.
    - `models/book.py`: Modelo de dados para os livros.

- **Google Books API**
  - Integração com a API do Google Books para buscar livros online.
  - A chave da API (API Key) foi obtida na plataforma do Google Cloud.

## Integração com a API do Google Books

Para integrar a API do Google Books, segui os seguintes passos:

1. Criar um projeto no Google Cloud.
2. Habilitar a API do Google Books.
3. Gerar uma chave de API (API Key).
4. Adicionar a chave de API ao arquivo `.env` no seguinte formato:

GOOGLE_BOOKS_API_KEY=sua_chave_de_api

## Dockerização

O projeto foi dockerizado para facilitar o desenvolvimento e a implantação. Utilizei repositórios separados para o frontend e o backend, cada um com seu próprio Dockerfile.

### Dockerfiles

- **Client-Main Dockerfile**

Dockerfile

FROM node:16-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . /app
RUN npm run build
RUN npm install -g http-server
EXPOSE 5173
CMD ["http-server", "/app/dist", "-p", "5173"]

- **Server-Main Dockerfile**

Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5004
CMD ["flask", "run", "--host=0.0.0.0", "--port=5004"]

### Docker Composer

O arquivo docker-compose.yml orquestra os containers Docker para o frontend, backend e banco de dados.

version: '3.8'

services:
  server:
    build:
      context: ./server-main
    ports:
      - "5004:5004"
    environment:
      - FLASK_ENV=development
    volumes:
      - ./server-main:/app
    depends_on:
      - db

  client:
    build:
      context: ./client-main
    ports:
      - "5173:5173"
    volumes:
      - ./client-main:/app
    environment:
      - VUE_APP_API_URL=http://localhost:5004

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: books
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:


# Instruções para Executar o Servidor da Aplicação Web

Para executar o projeto, siga os passos abaixo para inicializar o servidor, que será o backend do aplicativo web. É recomendado rodá-lo na porta 5004, que é a porta configurada no frontend.

## Passos para Inicializar o Servidor

### 1. Instalar Dependências

Certifique-se de que todas as dependências estejam instaladas. No diretório `/server-main/`, execute:

pip install -r requirements.txt

#### 2. Iniciar o Servidor
Inicie o servidor Flask na porta 5004 com o comando:

flask run -p 5004

##### 3. Acessar a API
A API poderá ser acessada nos seguintes endpoints:

Listar todos os livros:

http://localhost:5004/books

Acessar um livro específico pelo ID:

http://localhost:5004/books/<string:book_id>

###### 4. Visualizar a Documentação Swagger
Para visualizar a documentação Swagger da API, acesse a URL abaixo:

http://127.0.0.1:5004/swagger-ui

Conectar ao Frontend

Após iniciar o servidor backend, siga os passos descritos no README do frontend (client-main) para inicializar o aplicativo web.

Resumo dos Passos:
Instalar dependências com pip install -r requirements.txt.
Iniciar o servidor com flask run -p 5004.
Acessar a API nos endpoints especificados.
Visualizar a documentação Swagger em http://127.0.0.1:5004/swagger-ui.
Iniciar o frontend conforme as instruções no README do frontend.
Seguindo esses passos, você conseguirá executar o servidor backend e integrá-lo com o frontend da aplicação.


## Como Rodar o Projeto com o Docker Compose

1. Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.
2. Navegue até o diretório root do projeto.
3. Execute o seguinte comando: 

docker-compose up --build

4. Acesse o frontend em http://localhost:5173 e a documentação da API em http://localhost:5004/swagger-ui.

## Rotas da API

GET /books
Retorna a lista de todos os livros.

GET /books/{id}
Retorna os detalhes de um livro específico.

POST /books
Adiciona um novo livro.

PUT /books/{id}
Atualiza os detalhes de um livro específico.

DELETE /books/{id}
Exclui um livro específico.

GET /search_books?q={query}
Busca livros na API do Google Books com base na query fornecida.

## Conclusão ##

Este projeto demonstra a integração de diferentes tecnologias e serviços para criar uma aplicação completa e dockerizada. Espero que este guia tenha sido útil e que você possa aproveitar ao máximo esta aplicação. Se tiver dúvidas, sinta-se à vontade para entrar em contato.


# Instruções para Executar o Servidor da Aplicação Web

Para executar o projeto, siga os passos abaixo para inicializar o servidor, que será o backend do aplicativo web. É recomendado rodá-lo na porta 5004, que é a porta configurada no frontend.

## Passos para Inicializar o Servidor

### 1. Instalar Dependências

Certifique-se de que todas as dependências estejam instaladas. No diretório `/server-main/`, execute:

pip install -r requirements.txt

#### 2. Iniciar o Servidor
Inicie o servidor Flask na porta 5004 com o comando:

flask run -p 5004

##### 3. Acessar a API
A API poderá ser acessada nos seguintes endpoints:

Listar todos os livros:

http://localhost:5004/books

Acessar um livro específico pelo ID:

http://localhost:5004/books/<string:book_id>

###### 4. Visualizar a Documentação Swagger
Para visualizar a documentação Swagger da API, acesse a URL abaixo:

http://127.0.0.1:5004/swagger-ui

Conectar ao Frontend

Após iniciar o servidor backend, siga os passos descritos no README do frontend (client-main) para inicializar o aplicativo web.

Resumo dos Passos:
Instalar dependências com pip install -r requirements.txt.
Iniciar o servidor com flask run -p 5004.
Acessar a API nos endpoints especificados.
Visualizar a documentação Swagger em http://127.0.0.1:5004/swagger-ui.
Iniciar o frontend conforme as instruções no README do frontend.
Seguindo esses passos, você conseguirá executar o servidor backend e integrá-lo com o frontend da aplicação.