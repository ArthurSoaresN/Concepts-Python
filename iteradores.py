# Iteradores e Geradores

# Trabalhar com sequências de maneira eficiente

# Iterador

# É um objeto que contém um número contável de valores que podem ser iterados, o que significa
# que voce pode percorrer todos os valores

# Métodos especias: __next__() e __inter__()

# Uso, exemplo
# Ler arquivos grandes
# Econimizar memória evitando carregar todas as linhas do arquivo
# Itera linha a linha

class FileIterador:
    def __init__(self, filename):
        self.file = open(filename)
    
    def __iter__(self):
        return self

    def __next__(self):
        line = self.line.readline()
        pass

class MeuIterador():

    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
        