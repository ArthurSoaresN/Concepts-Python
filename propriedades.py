# Propriedades

# com o property() do Python, voce pode criar atributos gerenciados em suas classes (propriedades)
# sem alterar a API publica da classe

class Foo:
    def __init__ (self, x=None):
        self._x = x
    
    @property # Propriedade
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, valor):
        self._x += valor

    @x.deleter
    def x(self):
        self._x = -1
    
foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
    
# Elas são a chave para criar atributos "inteligentes" em suas classes, 
# que parecem variáveis comuns por fora, mas por trás dos panos, executam código (métodos).