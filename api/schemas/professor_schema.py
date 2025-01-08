from api import ma
from ..models import professor_model
from marshmallow import fields

class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = professor_model.Professor # model recebe a classe curso de curso_model.py
        load_instance = True
        fields = ("id", "nome", "idade") # campos para validação

    nome = fields.String(required=True) # nome tem que receber um valor String
    idade = fields.Integer(required=True) # nome tem que receber um valor String


class ProfessorFormacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = professor_model.Professor  # Supondo que há um model Professor
        load_instance = True
        fields = ("id", "nome")


