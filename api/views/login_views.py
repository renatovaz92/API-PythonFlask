from flask_restful import Resource # importando recurso | vai definir de acordo com a requisição que o cliente vai fazer para o servidor
from api import api,jwt # importe pra mim do módulo api o api
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services import usuario_service
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta


# https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

class LoginList(Resource):

    @jwt.additional_claims_loader
    def add_claims_to_access_token(identity):
        usuario_token = usuario_service.listar_usuario_id(identity)
        if usuario_token.is_admin:
            rules = 'admin'
        else:
            rules = 'user'

        return {'rules':rules}

    def post(self):
        ls = login_schema.LoginSchema() # referenciar o professorSchema para trabalhar com a validação de dados
        validate = ls.validate(request.json) # em uma variavel passamos o método validate passando o request.json
        if validate:
            return make_response(jsonify(validate), 400) # se houve algum erro ele vai mostar a resposta e o código 400
        else:
            # se não houver erro, vou recuperar os campos da nossa requisição via json
            email = request.json["email"]
            senha = request.json["senha"]

            usuario_bd = usuario_service.listar_usuario_email(email)

            if usuario_bd and usuario_bd.ver_senha(senha):
                access_token = create_access_token(
                    identity=usuario_bd.id,
                    expires_delta=timedelta(seconds=100)
                )

                refresh_token = create_refresh_token(
                    identity=usuario_bd.id
                )
                return make_response(jsonify({
                    'access_token':access_token,
                    'refresh_token':refresh_token,
                    'message':'Login realizado com sucesso.'
                }),200)

            return make_response(jsonify({
                'message':'As credenciais estão inválidas.'
            }),401)


api.add_resource(LoginList, '/login')
