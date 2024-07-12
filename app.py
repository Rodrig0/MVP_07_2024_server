import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_smorest import Api
from dotenv import load_dotenv
import os
import logging

import models
from db import db
from resources.book import blp as BookBlueprint

# Carregar variáveis de ambiente do arquivo .flaskenv
load_dotenv("./.flaskenv")

def create_app(db_url=None):
    app = Flask(__name__)
    app.config.from_object(__name__)
    
    # Habilitar CORS (Cross-Origin Resource Sharing)
    CORS(app, resources={r'/*': {'origins': '*'}})
    
    # Rota de sanity check do serviço
    @app.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')
    
    # Configurações do Flask e da API
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "API de Lista de Leitura"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Inicializar a extensão SQLAlchemy com a aplicação
    db.init_app(app)
        
    api = Api(app)

    # Criar todas as tabelas no banco de dados
    with app.app_context():
        db.create_all()

    # Registrar o blueprint do recurso de livros
    api.register_blueprint(BookBlueprint)

    # Rota para buscar livros usando a API do Google Books
    @app.route('/search_books', methods=['GET'])
    def search_books():
        query = request.args.get('q')
        api_key = os.getenv('GOOGLE_BOOKS_API_KEY')
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}')
        if response.status_code == 200:
            logging.info(response.json())
            return jsonify(response.json())
        else:
            logging.error(f"Erro ao buscar dados da API do Google Books: {response.text}")
            return jsonify({"error": "Erro ao buscar dados da API do Google Books"}), response.status_code

    return app
