from flask_restful import Resource # importando recurso | vai definir de acordo com a requisição que o cliente vai fazer para o servidor
from api import api # importe pra mim do módulo api o api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service
import uuid


# https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

class UsuarioList(Resource):

    def post(self):
        us = usuario_schema.UsuarioSchema() # referenciar o professorSchema para trabalhar com a validação de dados
        validate = us.validate(request.json) # em uma variavel passamos o método validate passando o request.json
        if validate:
            return make_response(jsonify(validate), 400) # se houve algum erro ele vai mostar a resposta e o código 400
        else:
            # se não houver erro, vou recuperar os campos da nossa requisição via json
            nome = request.json["nome"]
            email = request.json["email"]
            senha = request.json["senha"]
            is_admin = request.json["is_admin"]
            api_key = str(uuid.uuid4())

            novo_usuario = usuario.Usuario(nome=nome,email=email,senha=senha,is_admin=is_admin,api_key=api_key) # preenhcer o novo professor pegando os novos valores da requisição
            resultado = usuario_service.cadastrar_usuario(novo_usuario) # chamando o service passando o nova_professor
            x = us.jsonify(resultado) # em uma variável qualquer, guardamos o resultado da requisição
            return make_response(x, 201)


api.add_resource(UsuarioList, '/usuario')
