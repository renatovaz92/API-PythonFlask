from flask_restful import Resource # importando recurso | vai definir de acordo com a requisição que o cliente vai fazer para o servidor
from api import api # importe pra mim do módulo api o api
from ..schemas import professor_schema
from flask import request, make_response, jsonify
from ..entidades import professor
from ..services import professor_service
from ..models.professor_model import Professor
from ..paginate import paginate
from flask_jwt_extended import jwt_required


# https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

class ProfessorList(Resource):
    #@jwt_required()
    def get(self):
        #professores = professor_service.listar_professores()
        ps = professor_schema.ProfessorSchema(many=True)
        #return make_response(fs.jsonify(professores), 200)
        return paginate(Professor,ps)

    #@jwt_required()
    def post(self):
        fs = professor_schema.ProfessorSchema() # referenciar o professorSchema para trabalhar com a validação de dados
        validate = fs.validate(request.json) # em uma variavel passamos o método validate passando o request.json
        if validate:
            return make_response(jsonify(validate), 400) # se houve algum erro ele vai mostar a resposta e o código 400
        else:
            # se não houver erro, vou recuperar os campos da nossa requisição via json
            nome = request.json["nome"]
            idade = request.json["idade"]

            nova_professor = professor.Professor(nome=nome,idade=idade) # preenhcer o novo professor pegando os novos valores da requisição
            resultado = professor_service.cadastrar_professor(nova_professor) # chamando o service passando o nova_professor
            x = fs.jsonify(resultado) # em uma variável qualquer, guardamos o resultado da requisição
            return make_response(x, 201)

class ProfessorDetail(Resource):
    @jwt_required()
    def get(self, id):
        professor = professor_service.listar_professor_id(id)
        if professor is None:
            return make_response(jsonify("Professor não foi encontrado."), 404)
        fs = professor_schema.ProfessorSchema()
        return make_response(fs.jsonify(professor), 200)

    @jwt_required()
    def put(self, id):
        professor_bd = professor_service.listar_professor_id(id)
        if professor_bd is None:
            return make_response(jsonify("Professor não foi encontrada."), 404)
        fs = professor_schema.ProfessorSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]
            nova_professor = professor.Professor(nome=nome,idade=idade)
            professor_service.atualiza_professor(professor_bd,nova_professor)
            professor_atualizado = professor_service.listar_professor_id(id)
            return make_response(fs.jsonify(professor_atualizado), 200)

    @jwt_required()
    def delete(self,id):
        professor_bd = professor_service.listar_professor_id(id)
        if professor_bd is None:
            return make_response(jsonify("Professor não foi encontrado."), 404)
        professor_service.remove_professor(professor_bd)
        return make_response("Professor excluída com sucesso!", 200)



api.add_resource(ProfessorList, '/professores')
api.add_resource(ProfessorDetail, '/professores/<int:id>')