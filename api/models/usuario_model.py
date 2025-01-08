from api import db
from passlib.hash import pbkdf2_sha256


# Importa o objeto `db` do módulo `api`. Este objeto é geralmente uma instância da classe SQLAlchemy, usada para interagir com o banco de dados.

class Usuario(db.Model):
    # Define uma classe `Professor` que herda de `db.Model`, fazendo com que `Professor` seja um modelo do SQLAlchemy.

    __tablename__ = "usuario"
    # Define o nome da tabela no banco de dados como "professor".

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    # Define uma coluna `id` na tabela, do tipo `Integer`. Esta coluna é a chave primária, autoincrementada e não pode ser nula.

    nome = db.Column(db.String(50), nullable=False)
    # Define uma coluna `nome` na tabela, do tipo `String` com um comprimento máximo de 50 caracteres. Esta coluna não pode ser nula.

    email = db.Column(db.String(100), nullable=False)
    # Define uma coluna `idade` na tabela, do tipo `Integer`. Esta coluna não pode ser nula.

    senha = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean)
    api_key = db.Column(db.String(100), nullable=True)

    def encriptar_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    def ver_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)


