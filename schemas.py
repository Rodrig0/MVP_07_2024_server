from marshmallow import Schema, fields

# Esquema para serializar e desserializar os dados do livro
class BookSchema(Schema):
    id = fields.Str(dump_only=True)  # Campo de ID é somente para saída
    title = fields.Str(required=True)  # Campo título é obrigatório
    author = fields.Str(required=True)  # Campo autor é obrigatório
    read = fields.Bool(required=True)  # Campo se foi lido é obrigatório

# Esquema para atualização parcial dos dados do livro
class BookUpdateSchema(Schema):
    title = fields.Str()  # Campo título é opcional
    author = fields.Str()  # Campo autor é opcional
    read = fields.Bool()  # Campo se foi lido é opcional
