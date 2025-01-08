from flask import request, url_for
# Importa os objetos 'request' e 'url_for' do módulo Flask.
# 'request' é usado para acessar os dados da requisição atual.
# 'url_for' é usado para gerar URLs para as rotas definidas na aplicação Flask.

def paginate(model, schema):
    # Define uma função chamada 'paginate' que aceita dois parâmetros: 'model' e 'schema'.
    # 'model' é o modelo do banco de dados (ORM) que será paginado.
    # 'schema' é o esquema de serialização (provavelmente do Marshmallow) que será usado para serializar os dados.

    page = int(request.args.get('page', 1))
    # Obtém o parâmetro 'page' da URL da requisição. Se não estiver presente, usa o valor padrão 1.
    # Converte o valor para um inteiro e armazena na variável 'page'.

    per_page = int(request.args.get('per_page', 3))
    # Obtém o parâmetro 'per_page' da URL da requisição. Se não estiver presente, usa o valor padrão 3.
    # Converte o valor para um inteiro e armazena na variável 'per_page'.

    page_obj = model.query.paginate(page=page, per_page=per_page)
    # Usa o método 'paginate' do SQLAlchemy para realizar a paginação dos dados.
    # 'page' e 'per_page' são passados como argumentos para especificar a página atual e o número de itens por página.
    # O resultado é um objeto de paginação armazenado na variável 'page_obj'.

    next = url_for(request.endpoint,
                   page=page_obj.next_num if page_obj.has_next else page_obj.page, per_page=per_page, **request.view_args)
    # Gera a URL para a próxima página.
    # 'url_for' usa 'request.endpoint' para obter o endpoint atual da requisição.
    # 'page' é definido como 'page_obj.next_num' se houver uma próxima página, caso contrário, usa a página atual.
    # 'per_page' é mantido constante.
    # '**request.view_args' adiciona quaisquer argumentos adicionais da URL atual.
    # A URL gerada é armazenada na variável 'next'.

    prev = url_for(request.endpoint,
                   page=page_obj.prev_num if page_obj.has_prev else page_obj.page, per_page=per_page, **request.view_args)
    # Gera a URL para a página anterior.
    # 'url_for' usa 'request.endpoint' para obter o endpoint atual da requisição.
    # 'page' é definido como 'page_obj.prev_num' se houver uma página anterior, caso contrário, usa a página atual.
    # 'per_page' é mantido constante.
    # '**request.view_args' adiciona quaisquer argumentos adicionais da URL atual.
    # A URL gerada é armazenada na variável 'prev'.
    return {
        'total':page_obj.total,
        'pages':page_obj.pages,
        'next':next,
        'prev':prev,
        'results':schema.dump(page_obj.items)
    }
