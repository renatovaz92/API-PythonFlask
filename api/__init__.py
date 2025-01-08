from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__) # criando a aplicação Flask
app.config.from_object('config') # definindo que o arquivo de configuração da aplicação é o config.py

db = SQLAlchemy(app) # chamando SQLALCHEMY passando a aplicação criada
ma = Marshmallow(app) # variável chamando o Marshmallow e passando pra ele nossa aplicação
migrate = Migrate(app, db) # chamando Migrate e passando a aplicação criada e o nosso banco de dados
api = Api(app) # para o módulo Api passamos como parâmetro a nossa aplicação app
jwt = JWTManager(app)



from .views import curso_views, formacao_views, professor_views, usuario_views, login_views, refresh_token_views
from .models import curso_model, formacao_model, professor_model, usuario_model

# Script de configuração principal do projeto