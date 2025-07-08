class veiculo:
    
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Motor Ligado")
        return True
    
    def __str__(self):
        pass

class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado): #Sobrescrevendo
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Esta carregado' if self.carregado else 'Não esta carregado'}")

moto = motocicleta("Preto", "ABC-1234", 2)
moto.ligar_motor()

carro = carro("Branco", "CBA-4321", 4)
carro.ligar_motor()

caminhao = caminhao("Cinza", "LKK-9999", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()