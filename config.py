# aqui definimos todas as propriedades de configuração
DEBUG = True # modo de debug seja igual a true

# configurando informações do banco de dados
USERNAME = 'root'
PASSWORD = '#'
SERVER = 'localhost'
DB = 'api_flask'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY="aplicacao_flask"