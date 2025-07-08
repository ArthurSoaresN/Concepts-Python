class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): #Atributos
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):  #Métodos (Comportamentos)
        print(f"Bicicleta {self.modelo}: Buzinou")

    def parar(self):
        print(f"Bicicleta {self.modelo}: Parou")

    def correr(self):
        print(f"Bicicleta {self.modelo}: Correndo")

    def get_color(self):
        return self.cor
    
    def set_color(self, color: str):
        new_color = color
        self.cor = new_color
        print(f"Cor da {self.modelo} alterada para: {new_color}")
        return self.cor


caloi = Bicicleta("Preta", "Caloi", 2024, 1400)

caloi.buzinar()
caloi.correr()
caloi.parar()

cor_caloi = caloi.get_color()
print(f"Cor Caloi: {cor_caloi}")

caloi.set_color("Vermelha")

cor_caloi = caloi.get_color()
print(f"Cor Caloi: {cor_caloi}")

