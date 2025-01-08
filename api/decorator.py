from functools import wraps
from flask_jwt_extended import get_jwt,verify_jwt_in_request
from flask import make_response,jsonify,request
from .services.usuario_service import listar_usuario_api_key

# Define um decorador chamado `admin_required` que será usado para proteger funções específicas.
def admin_required(fn):
    # Preserva o nome e a documentação da função decorada (mantém a "identidade" da função original).
    @wraps(fn)
    # Define a função wrapper que será executada no lugar da função decorada.
    def wrapper(*args, **kwargs):
        # Verifica se existe um token JWT válido na requisição atual.
        verify_jwt_in_request()

        # Obtém as informações (claims) do token JWT da requisição atual.
        claims = get_jwt()
        # Verifica se o campo 'rules' no token indica que o usuário tem permissão de administrador.
        if claims['rules'] != 'admin':
            # Se não for administrador, retorna uma resposta com mensagem de erro e código HTTP 403 (proibido).
            return make_response(jsonify(mensagem="Apenas administradores tem acesso ao recurso."), 403)
        else:
            # Se for administrador, chama a função original com os argumentos passados.
            return fn(*args, **kwargs)

    # Retorna o wrapper para substituir a função original pela versão protegida.
    return wrapper

def api_key_required(fn):
    @wraps(fn)

    def wrapper(*args, **kwargs):
        api_key = request.args.get('api_key')
        if api_key and listar_usuario_api_key(api_key):
            return fn(*args,**kwargs)
        else:
            return make_response(jsonify(mensagem="Necessário API KEY válido."), 401)
    return wrapper
