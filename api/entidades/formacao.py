# https://pythonacademy.com.br/blog/como-utilizar-property-no-python
# https://pythonacademy.com.br/blog/classes-e-objetos-no-python

class Formacao():
    # Definição de uma classe chamada Formacao.

    def __init__(self, nome, descricao, professores):
        # Método inicializador da classe, chamado quando uma nova instância de Formacao é criada.
        self.__nome = nome
        # Atributo privado __nome é definido pelo valor passado como argumento nome.
        self.__descricao = descricao
        # Atributo privado __descricao é definido pelo valor passado como argumento descricao.
        self.__professores = professores
        # Atributo privado __professores é definido pelo valor passado como argumento professores.

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
    # O decorador @property transforma o método descricao() em uma propriedade, permitindo acessar o valor de __descricao diretamente como um atributo.
    def descricao(self):
        return self.__descricao
        # Retorna o valor do atributo privado __descricao.

    @descricao.setter
    # O decorador @descricao.setter permite definir o valor de __descricao diretamente como um atributo, habilitando a modificação do valor de __descricao.
    def descricao(self, descricao):
        self.__descricao = descricao
        # Define o valor do atributo privado __descricao com o valor passado como argumento descricao.

    @property
    # O decorador @property transforma o método professores() em uma propriedade, permitindo acessar o valor de __professores diretamente como um atributo.
    def professores(self):
        return self.__professores
        # Retorna o valor do atributo privado __professores.

    @professores.setter
    # O decorador @professores.setter permite definir o valor de __professores diretamente como um atributo, habilitando a modificação do valor de __professores.
    def professores(self, professores):
        self.__professores = professores
        # Define o valor do atributo privado __professores com o valor passado como argumento professores.

