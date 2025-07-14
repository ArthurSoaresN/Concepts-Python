# Interfaces definem o que uma classe deve fazer
# e não como fazer "Padrão"

# ABC - modulo

# Usamos para definir classes abstratas

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod   
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    pass

controle = ControleTV()
controle.ligar()
controle.desligar()

