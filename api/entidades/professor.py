# https://pythonacademy.com.br/blog/como-utilizar-property-no-python
# https://pythonacademy.com.br/blog/classes-e-objetos-no-python

class Professor():
    # Definição de uma classe chamada Professor.

    def __init__(self, nome, idade):
        # Método inicializador da classe, chamado quando uma nova instância de Professor é criada.
        self.__nome = nome
        # Atributo privado __nome é definido pelo valor passado como argumento nome.
        self.__idade = idade
        # Atributo privado __idade é definido pelo valor passado como argumento idade.

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
    def idade(self):
        return self.__idade
        # Retorna o valor do atributo privado __idade.

    @idade.setter
    # O decorador @idade.setter permite definir o valor de __idade diretamente como um atributo, habilitando a modificação do valor de __idade.
    def idade(self, idade):
        self.__idade = idade
        # Define o valor do atributo privado __idade com o valor passado como argumento idade.
