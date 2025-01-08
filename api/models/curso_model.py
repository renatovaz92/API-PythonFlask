from api import db
# Importa o objeto `db` do módulo `api`. Este objeto é geralmente uma instância da classe SQLAlchemy, usada para interagir com o banco de dados.

from ..models import formacao_model
# Importa o módulo `formacao_model` do diretório pai do pacote `models`. Este módulo contém a definição da classe `Formacao`.

class Curso(db.Model):
    # Define uma classe `Curso` que herda de `db.Model`, fazendo com que `Curso` seja um modelo do SQLAlchemy.

    __tablename__ = "curso"
    # Define o nome da tabela no banco de dados como "curso".

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    # Define uma coluna `id` na tabela, do tipo `Integer`. Esta coluna é a chave primária, autoincrementada e não pode ser nula.

    nome = db.Column(db.String(50), nullable=False)
    # Define uma coluna `nome` na tabela, do tipo `String` com um comprimento máximo de 50 caracteres. Esta coluna não pode ser nula.

    descricao = db.Column(db.String(100), nullable=False)
    # Define uma coluna `descricao` na tabela, do tipo `String` com um comprimento máximo de 100 caracteres. Esta coluna não pode ser nula.

    data_publicacao = db.Column(db.Date, nullable=False)
    # Define uma coluna `data_publicacao` na tabela, do tipo `Date`. Esta coluna não pode ser nula.

    formacao_id = db.Column(db.Integer, db.ForeignKey("formacao.id"))
    # Define uma coluna `formacao_id` na tabela, do tipo `Integer`. Esta coluna é uma chave estrangeira que referencia a coluna `id` na tabela `formacao`.

    formacao = db.relationship(formacao_model.Formacao, backref=db.backref("cursos", lazy="dynamic"))
    # Define uma relação entre a classe `Curso` e a classe `Formacao`. A propriedade `formacao` permitirá acessar a instância de `Formacao` associada a um `Curso`.
    # O argumento `backref` adiciona uma propriedade `cursos` à classe `Formacao`, permitindo acessar todos os cursos relacionados. O `lazy="dynamic"` permite
    # que a relação seja carregada de maneira dinâmica, utilizando consultas adicionais ao banco de dados quando necessário.

