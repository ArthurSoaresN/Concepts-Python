class Animal:
    def __init__(self, numero_patas, **kwargs):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs): #KWARGS para unir paramentros de dois construtores
        self.cor_bico = cor_bico
        super().__init__(**kwargs)


class Gato(Mamifero):
    def __init__(self, cor_pelo, numero_patas):
        super().__init__(cor_pelo=cor_pelo, numero_patas=numero_patas)


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, numero_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas)


gato = Gato(numero_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(numero_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)