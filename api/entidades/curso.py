# https://pythonacademy.com.br/blog/como-utilizar-property-no-python
# https://pythonacademy.com.br/blog/classes-e-objetos-no-python

class Curso():
    # Definição de uma classe chamada Curso.

    def __init__(self, nome, descricao, data_publicacao, formacao):
        # Método inicializador da classe, chamado quando uma nova instância de Curso é criada.
        self.__nome = nome
        # Atributo privado __nome é definido pelo valor passado como argumento nome.
        self.__descricao = descricao
        # Atributo privado __descricao é definido pelo valor passado como argumento descricao.
        self.__data_publicacao = data_publicacao
        # Atributo privado __data_publicacao é definido pelo valor passado como argumento data_publicacao.
        self.__formacao = formacao
        # Atributo privado __formacao é definido pelo valor passado como argumento formacao.

    @property
    # O decorador @property transforma o método nome() em uma propriedade. Isso permite acessar o valor de __nome diretamente como um atributo.
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
    # O decorador @property transforma o método data_publicacao() em uma propriedade, permitindo acessar o valor de __data_publicacao diretamente como um atributo.
    def data_publicacao(self):
        return self.__data_publicacao
        # Retorna o valor do atributo privado __data_publicacao.

    @data_publicacao.setter
    # O decorador @data_publicacao.setter permite definir o valor de __data_publicacao diretamente como um atributo, habilitando a modificação do valor de __data_publicacao.
    def data_publicacao(self, data_publicacao):
        self.__data_publicacao = data_publicacao
        # Define o valor do atributo privado __data_publicacao com o valor passado como argumento data_publicacao.

    @property
    # O decorador @property transforma o método formacao() em uma propriedade, permitindo acessar o valor de __formacao diretamente como um atributo.
    def formacao(self):
        return self.__formacao
        # Retorna o valor do atributo privado __formacao.

    @formacao.setter
    # O decorador @formacao.setter permite definir o valor de __formacao diretamente como um atributo, habilitando a modificação do valor de __formacao.
    def formacao(self, formacao):
        self.__formacao = formacao
        # Define o valor do atributo privado __formacao com o valor passado como argumento formacao.