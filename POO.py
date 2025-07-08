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
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):    #Método
        print("Latido") 
    
    def dormir(self):
        self.acordado = False
        print("Dormindo...")
        
# Objeto

cao_1 = Cachorro("Dog", "Yellow", False)
cao_2 = Cachorro("Chaves", "White")
