class veiculo:
    
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Motor Ligado")
        return True

class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    pass

moto = motocicleta("Preto", "ABC-1234", 2)
moto.ligar_motor()

carro = carro("Branco", "CBA-4321", 4)
carro.ligar_motor()