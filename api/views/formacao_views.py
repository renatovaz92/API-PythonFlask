from flask_restful import Resource # importando recurso | vai definir de acordo com a requisição que o cliente vai fazer para o servidor
from api import api # importe pra mim do módulo api o api
from ..schemas import formacao_schema
from flask import request, make_response, jsonify
from ..entidades import formacao
from ..services import formacao_service
from ..paginate import paginate
from ..models.formacao_model import Formacao
from ..models import professor_model,formacao_model
from flask_jwt_extended import jwt_required
from ..decorator import api_key_required
import logging


# https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

class FormacaoList(Resource):
    #@jwt_required()
    @api_key_required
    def get(self):
        #formacoes = formacao_service.listar_formacoes()
        fs = formacao_schema.ListaFormacao(many=True)
        #return make_response(fs.jsonify(formacoes), 200)
        return paginate(Formacao,fs)

    #@jwt_required()
    def post(self):
        fs = formacao_schema.FormacaoSchema() # referenciar o FormacaoSchema para trabalhar com a validação de dados
        validate = fs.validate(request.json) # em uma variavel passamos o método validate passando o request.json
        if validate:
            return make_response(jsonify(validate), 400) # se houve algum erro ele vai mostar a resposta e o código 400
        else:
            logging.info("Request JSON: %S", request.json)
            # se não houver erro, vou recuperar os campos da nossa requisição via json
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            professores = request.json["professores"]

            professor_objs = [professor_model.Professor.query.get(prof["id"]) for prof in professores]
            print(professor_objs)

            #nova_formacao = formacao.Formacao(nome=nome,descricao=descricao,professores=professores)
            nova_formacao = formacao_model.Formacao(
                nome=nome,
                descricao=descricao,
                professores=professor_objs
            )
            # preenhcer o novo formacao pegando os novos valores da requisição
            formacao_service.cadastrar_formacao(nova_formacao)
            formacao_nome = formacao_service.listar_formacao_nome(nome)
            fn = formacao_schema.ListaFormacao()
            return make_response(fn.jsonify(formacao_nome), 200)

class FormacaoDetail(Resource):
    @jwt_required()
    def get(self, id):
        formacao = formacao_service.listar_formacao_id(id)
        if formacao is None:
            return make_response(jsonify("Formação não foi encontrada."), 404)
        fs = formacao_schema.ListaFormacao()
        return make_response(fs.jsonify(formacao), 200)

    @jwt_required()
    def put(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify("Formação não foi encontrada."), 404)

        fs = formacao_schema.FormacaoAtualizaSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            professores = request.json["professores"]
            nova_formacao = formacao.Formacao(nome=nome,descricao=descricao,professores=professores)
            formacao_service.atualiza_formacao(formacao_bd,nova_formacao)
            formacao_atualizado = formacao_service.listar_formacao_id(id)
            return make_response(fs.jsonify(formacao_atualizado), 200)

    @jwt_required()
    def delete(self,id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify("Formação não foi encontrada."), 404)
        formacao_service.remove_formacao(formacao_bd)
        return make_response("Formação excluída com sucesso!", 200)



api.add_resource(FormacaoList, '/formacoes')
api.add_resource(FormacaoDetail, '/formacoes/<int:id>')