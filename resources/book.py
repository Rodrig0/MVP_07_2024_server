import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import BookModel
from schemas import BookSchema, BookUpdateSchema

# Cria um blueprint para operações com livros
blp = Blueprint("books", __name__, description="Operações com livros")

@blp.route("/books/<string:book_id>")
class Book(MethodView):
    @blp.response(200, BookSchema, description="Consulta um livro pelo ID")
    def get(self, book_id):
        book = BookModel.query.get_or_404(book_id)
        return book
    
    @blp.response(204, BookSchema, description="Deleta um livro pelo ID")
    def delete(self, book_id):
        book = BookModel.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return {"message": "Livro deletado com sucesso."}, 204
    
    @blp.arguments(BookUpdateSchema)
    @blp.response(200, BookSchema, description="Edita um livro pelo ID")
    def put(self, book_data, book_id):
        book = BookModel.query.get(book_id)
        if book:
            book.title = book_data["title"]
            book.author = book_data["author"]
            book.read = book_data["read"]
        else:
            book = BookModel(id=book_id, **book_data)

        db.session.add(book)
        db.session.commit()

        return book

@blp.route("/books")
class BookList(MethodView):
    @blp.response(200, BookSchema(many=True), description="Consulta todos os livros")
    def get(self):
        return BookModel.query.all()
    
    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema, description="Adiciona um novo livro")
    def post(self, book_data):
        book = BookModel(**book_data)
        try:
            db.session.add(book)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Erro interno do servidor")
            
        return book, 201
