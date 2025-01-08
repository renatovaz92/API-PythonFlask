# o objetivo do service é ter um arquivo específico para interagir com o SQLALCHEMY, bem como seus métodos

from ..models import formacao_model
from api import db
from .professor_service import listar_professor_id

def cadastrar_formacao(formacao):
    #formacao_bd = formacao_model.Formacao(nome=formacao.nome, descricao=formacao.descricao)
    #for i in formacao.professores:
    #    professor = listar_professor_id(i)
    #    formacao_bd.professores.append(professor)
    #for i in formacao.professores:
    #    professor = listar_professor_id(i)
    #    if professor not in formacao_bd.professores:
    #       formacao_bd.professores.append(professor)
    db.session.add(formacao)
    db.session.commit()
    return formacao

def listar_formacoes():
    formacoes = formacao_model.Formacao.query.all()
    return formacoes

def listar_formacao_id(id):
    formacao = formacao_model.Formacao.query.filter_by(id=id).first()
    return formacao

def listar_formacao_nome(nome):
    formacao_nome = formacao_model.Formacao.query.filter_by(nome=nome).first()
    return formacao_nome

def atualiza_formacao(formacao_anterior, formacao_novo):
    formacao_anterior.nome = formacao_novo.nome
    formacao_anterior.descricao = formacao_novo.descricao
    for i in formacao_novo.professores:
        professor = listar_professor_id(i)
        formacao_anterior.professores.append(professor)
    db.session.commit()

def remove_formacao(formacao):
    db.session.delete(formacao)
    db.session.commit()