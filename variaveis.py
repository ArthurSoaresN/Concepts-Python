# Atributos do objetos

# Todos os objetos nascem com o mesmo numero de atributos de classe 
# e de instancia são diferentes para cada objeto (cada objeto tem uma copia)
# Ja os atributos de classe são compartilhados entre os objetos

class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self)->str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
aluno1 = Estudante("Joao", "11")
print(aluno1)

aluno1.escola = "Escola 1"
# !=
Estudante.escola = "Escola"
print(aluno1)