from api import ma
from ..models import curso_model
from marshmallow import fields



class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = curso_model.Curso # model recebe a classe curso de curso_model.py
        load_instance = True
        fields = ("id", "nome", "descricao","data_publicacao","formacao") # campos para validação
        #fields = ("id", "nome", "descricao", "data_publicacao", "formacao","_links")  # se eu quisesse utilizar o HATEOAS

    nome = fields.String(required=True) # nome tem que receber um valor String
    descricao = fields.String(required=True) # nome tem que receber um valor String
    data_publicacao = fields.Date(required=True) # nome tem que receber um valor Date
    formacao = fields.Nested('FormacaoSchema', required= True, only=("id","nome"))

#    _links = ma.Hyperlinks(
#        {
#            "get":ma.URLFor("cursodetail",id="<id>"),
#           "put":ma.URLFor("cursodetail",id="<id>"),
#            "delete":ma.URLFor("cursodetail",id="<id>")
#        }
#    )

class CursoAtualizacoesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = curso_model.Curso # model recebe a classe curso de curso_model.py
        load_instance = True
        fields = ("id", "nome", "descricao","data_publicacao","formacao") # campos para validação

    nome = fields.String(required=True) # nome tem que receber um valor String
    descricao = fields.String(required=True) # nome tem que receber um valor String
    data_publicacao = fields.Date(required=True) # nome tem que receber um valor Date
    formacao = fields.String(required=True)


