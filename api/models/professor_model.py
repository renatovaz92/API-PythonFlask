from api import db


# Importa o objeto `db` do módulo `api`. Este objeto é geralmente uma instância da classe SQLAlchemy, usada para interagir com o banco de dados.

class Professor(db.Model):
    # Define uma classe `Professor` que herda de `db.Model`, fazendo com que `Professor` seja um modelo do SQLAlchemy.

    __tablename__ = "professor"
    # Define o nome da tabela no banco de dados como "professor".

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    # Define uma coluna `id` na tabela, do tipo `Integer`. Esta coluna é a chave primária, autoincrementada e não pode ser nula.

    nome = db.Column(db.String(50), nullable=False) #, nullable=False
    # Define uma coluna `nome` na tabela, do tipo `String` com um comprimento máximo de 50 caracteres. Esta coluna não pode ser nula.

    idade = db.Column(db.Integer, nullable=False)
    # Define uma coluna `idade` na tabela, do tipo `Integer`. Esta coluna não pode ser nula.

    formacoes = db.relationship("Formacao", secondary="professor_formacao", back_populates="professores")
    # Define uma relação muitos-para-muitos entre `Professor` e `Formacao` usando a tabela associativa `professor_formacao`.
    # A propriedade `formacoes` permitirá acessar as formações associadas a um professor.
    # O argumento `back_populates="professores"` configura a relação bidirecional, permitindo que `Formacao` também tenha acesso aos professores associados.
