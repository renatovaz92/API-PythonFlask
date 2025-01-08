# https://pythonacademy.com.br/blog/como-utilizar-property-no-python
# https://pythonacademy.com.br/blog/classes-e-objetos-no-python

class Usuario():
    # Definição de uma classe chamada Usuario.

    def __init__(self, nome, email, senha, is_admin, api_key):
        # Método inicializador da classe, chamado quando uma nova instância de Professor é criada.
        self.__nome = nome
        # Atributo privado __nome é definido pelo valor passado como argumento nome.
        self.__email = email
        # Atributo privado __idade é definido pelo valor passado como argumento idade.
        self.__senha = senha
        self.__is_admin = is_admin
        self.__api_key = api_key

    @property
    # O decorador @property transforma o método nome() em uma propriedade, permitindo acessar o valor de __nome diretamente como um atributo.
    def nome(self):
        return self.__nome
        # Retorna o valor do atributo privado __nome.

    @nome.setter
    # O decorador @nome.setter permite definir o valor de __nome diretamente como um atributo, habilitando a modificação do valor de __nome.
    def nome(self, nome):
        self.__nome = nome
        # Define o valor do atributo privado __nome com o valor passado como argumento nome.

    @property
    # O decorador @property transforma o método idade() em uma propriedade, permitindo acessar o valor de __idade diretamente como um atributo.
    def email(self):
        return self.__email
        # Retorna o valor do atributo privado __idade.

    @email.setter
    # O decorador @idade.setter permite definir o valor de __idade diretamente como um atributo, habilitando a modificação do valor de __idade.
    def email(self, email):
        self.__email = email
        # Define o valor do atributo privado __idade com o valor passado como argumento idade.

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self,is_admin):
        self.__is_admin = is_admin

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self,api_key):
        self.__api_key = api_key
