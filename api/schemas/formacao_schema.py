from api import ma
from ..models import formacao_model
from marshmallow import fields
from ..schemas import curso_schema, professor_schema


class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    #professores = ma.Nested(professor_schema.ProfessorSchema, many=True)
    #professores = fields.List(fields.Nested(professor_schema.ProfessorSchema, many=True))
    class Meta:
        model = formacao_model.Formacao # model recebe a classe curso de curso_model.py
        load_instance = True
        fields = ("id", "nome", "descricao", "cursos","professores") # campos para validação

    nome = fields.String(required=True) # nome tem que receber um valor String
    descricao = fields.String(required=True) # nome tem que receber um valor String
    cursos = fields.List(fields.Nested(curso_schema.CursoSchema,only=("id","nome")))
    professores = fields.List(fields.Nested(professor_schema.ProfessorFormacaoSchema,only=("id","nome")))

class ListaFormacao(ma.SQLAlchemyAutoSchema):
    professores = ma.Nested(professor_schema.ProfessorSchema, many=True)
    class Meta:
        model = formacao_model.Formacao # model recebe a classe curso de curso_model.py
        load_instance = True
        fields = ("id", "nome", "descricao", "cursos","professores") # campos para validação

    nome = fields.String(required=True) # nome tem que receber um valor String
    descricao = fields.String(required=True) # nome tem que receber um valor String
    cursos = fields.List(fields.Nested(curso_schema.CursoSchema,only=("id","nome")))

class FormacaoAtualizaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = formacao_model.Formacao # model recebe a classe curso de curso_model.py
        load_instance = True
        fields = ("id", "nome", "descricao", "cursos","professores") # campos para validação

    nome = fields.String(required=True) # nome tem que receber um valor String
    descricao = fields.String(required=True) # nome tem que receber um valor String
    cursos = fields.List(fields.Nested(curso_schema.CursoSchema,only=("id","nome")))




