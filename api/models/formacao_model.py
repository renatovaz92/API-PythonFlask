from api import db
# Importa o objeto `db` do módulo `api`. Este objeto é geralmente uma instância da classe SQLAlchemy, usada para interagir com o banco de dados.

from .professor_model import Professor

# Importa a classe `Professor` do módulo `professor_model` que está no mesmo pacote.

professor_formacao = db.Table('professor_formacao',
                              # Define uma tabela associativa `professor_formacao` para a relação muitos-para-muitos entre `Professor` e `Formacao`.
                              db.Column('professor_id', db.Integer, db.ForeignKey('professor.id'), primary_key=True,
                                        nullable=False),
                              # Define a coluna `professor_id` como chave estrangeira que referencia a coluna `id` da tabela `professor`. Esta coluna é uma parte da chave primária composta e não pode ser nula.
                              db.Column('formacao_id', db.Integer, db.ForeignKey('formacao.id'), primary_key=True,
                                        nullable=False))
# Define a coluna `formacao_id` como chave estrangeira que referencia a coluna `id` da tabela `formacao`. Esta coluna é uma parte da chave primária composta e não pode ser nula.

class Formacao(db.Model):
    # Define uma classe `Formacao` que herda de `db.Model`, fazendo com que `Formacao` seja um modelo do SQLAlchemy.

    __tablename__ = "formacao"
    # Define o nome da tabela no banco de dados como "formacao".

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    # Define uma coluna `id` na tabela, do tipo `Integer`. Esta coluna é a chave primária, autoincrementada e não pode ser nula.

    nome = db.Column(db.String(50), nullable=False)
    # Define uma coluna `nome` na tabela, do tipo `String` com um comprimento máximo de 50 caracteres. Esta coluna não pode ser nula.

    descricao = db.Column(db.String(100), nullable=False)
    # Define uma coluna `descricao` na tabela, do tipo `String` com um comprimento máximo de 100 caracteres. Esta coluna não pode ser nula.

    professores = db.relationship(Professor, secondary="professor_formacao", back_populates="formacoes")
    # Define uma relação muitos-para-muitos entre `Formacao` e `Professor` usando a tabela associativa `professor_formacao`.
    # A propriedade `professores` permitirá acessar os professores associados a uma formação.
    # O argumento `back_populates="formacoes"` configura a relação bidirecional, permitindo que `Professor` também tenha acesso às formações associadas.
