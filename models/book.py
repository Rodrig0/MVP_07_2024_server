from db import db

# Modelo de dados para a tabela de livros
class BookModel(db.Model):
    __tablename__ = "books"  # Nome da tabela no banco de dados

    # Definição das colunas da tabela
    id = db.Column(db.Integer, primary_key=True)  # Coluna de ID, chave primária
    title = db.Column(db.String(80), unique=True, nullable=False)  # Coluna de título, deve ser única e não pode ser nula
    author = db.Column(db.String(80), nullable=False)  # Coluna de autor, não pode ser nula
    read = db.Column(db.Boolean, nullable=False, default=False)  # Coluna de status de leitura, não pode ser nula, valor padrão é False
