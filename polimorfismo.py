# Polimorfismo
# 
# Essa palavra significa ter muitas formas. Na programação
# significa o mesmo nome de função mas assinaturas diferentes
# sendo usado para tipos diferentes

# Exemplo: len()
# len("python")
# len([10,20,30])

# Polimorfismo precisa de herança

# Na herança, a classe filha herda os métodos da classe pai
# No entando, é possível modificar um método em uma classe filha
# herdada da classe pai. Isse é útil nos casos em que o método
# da classe pai não se encaixa perfeitamente na classe filha

class Passaro:
    def voar(self):
        print("Voando...")
    
class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro): # herança
    def voar(self):
        print("Avestruz nao pode voar")

def plano_voo(obj): #polimorfismo
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)