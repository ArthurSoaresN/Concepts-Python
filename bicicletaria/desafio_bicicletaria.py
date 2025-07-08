class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): #Atributos
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):  #Métodos
        print(f"Bicicleta {self.modelo}: Buzinou")

    def parar(self):
        print(f"Bicicleta {self.modelo}: Parou")



caloi = Bicicleta("Preta", "Caloi", 2024, 1400)

caloi.buzinar()