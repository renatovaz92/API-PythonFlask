from flask_restful import Resource # importando recurso | vai definir de acordo com a requisição que o cliente vai fazer para o servidor
from api import api # importe pra mim do módulo api o api
from ..schemas import formacao_schema
from flask import request, make_response, jsonify
from ..entidades import formacao
from ..services import formacao_service
from ..paginate import paginate
#from ..models.formacao_model import Formacao
from ..models import professor_model,formacao_model
from flask_jwt_extended import jwt_required
import logging

class FormacaoList(Resource):
    def post(self):
        fs = formacao_schema.FormacaoSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            logging.info("Request JSON: %s", request.json)
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            professores = request.json["professores"]

            professor_objs = [professor_model.Professor.query.get(prof["id"]) for prof in professores]
            logging.info("Professor Objects: %s", professor_objs)

            nova_formacao = formacao_model.Formacao(
                nome=nome,
                descricao=descricao,
                professores=professor_objs
            )
            logging.info("New Formacao: %s", nova_formacao)
            formacao_service.cadastrar_formacao(nova_formacao)
            formacao_nome = formacao_service.listar_formacao_nome(nome)
            fn = formacao_schema.ListaFormacao()
            return make_response(fn.jsonify(formacao_nome), 200)

