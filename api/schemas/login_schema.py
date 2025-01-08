from api import ma
from ..models import usuario_model
from marshmallow import fields

class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.Usuario # model recebe a classe curso de curso_model.py
        load_instance = True
        fields = ("id", "nome", "email","senha") # campos para validação

    nome = fields.String(required=False) # nome tem que receber um valor String
    email = fields.String(required=True) # nome tem que receber um valor String
    senha = fields.String(required=True)


