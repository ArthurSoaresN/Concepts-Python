# Paradigma POO

# Forma de solucionar os problemas através do código
# Abstração de problemas em objetos do mundo real, facilitando o entendimento do código
# e tornando mais fácil de modular e extensível.

# Conceitos Chaves:
# Classes e Objetos

# Classes

# Define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente. 
# Já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos pela classe.

#Classe
class Cachorro:
    def __init__(self, nome, cor, acordado = True): # Construtor
        #Inicialização
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        #Alterações
        print("Destruindo instância")
    
    def latir(self):    #Método
        print(f"Latido do cão: {self.nome}") 
    
    def dormir(self):
        self.acordado = False
        print("Dormindo...")
        
# Objeto

cao_1 = Cachorro("Dog", "Yellow", False)
cao_2 = Cachorro("Chaves", "White")

cao_1.latir()

# Método construtor (Método inicializador)
# ele é executado quando uma nova instância da classe é criada. Inicalização do estado do Objeto -> __init__

# Método destrutor
# Em Python não é tão necessário por ter coletor de lixo que lida com o gerenciamneto da memória automaticamente
# a declaração é __del__
# em linguagens de baixo nível é necessário liberar a memória dos objetos que não estão sendo mais usados
# Em python ele é útil para realizar uma determinada ação antes de liberar a memória que está sendo usada

# Conceito de Herança
# É a capacidade de uma classe filha derivar ou herdar as caracteríticas e comportamentos da classe pai(base)

# Benefícios
# Representa bem os relacionamentos do mundo real
# Reutilização de código
# É de natureza transitiva

class A:    #pai
    pass    
class B(A): #filha
    pass

# Herança simples
# Quando uma classe filha herda apenas uma classe pai, ela é chamada de herança simples

# Herança múltipla
# Quando uma classe filha herda de várias classes pai

class C(A, B):
    pass