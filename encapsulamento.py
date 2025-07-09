# Encapsulamento

# Proteção aos dados
# Ele descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade
# Isso impõe restrições ao acesso direto as variáveis e métodos e pode evitar a modificação acidental de dados
# Para evitar alterações acidentais, a variável de um objeto só pode ser alterado pelo método desse objeto

# Exemplo:
# Atributo privado
# - saldo: float

# Atributo não privado
# + depositar
# + sacar

# Recurso privado terá underline em seu nome, o interpretador não irá garantir sua proteção
# mas sim sua convenção

class Conta:
    def __init__(self, saldo, numero_agencia):
        self._saldo = saldo
        self.numero_agencia = numero_agencia
    
    def depositar(self, valor):
        self._saldo += valor #Encapsulamento

    def sacar(self, valor):
        self._saldo -= valor #Encapsulamento

    def get_saldo(self):
        return self._saldo



conta = Conta(100, "0001")
print(conta.numero_agencia)
print(conta.get_saldo()) # Proteçã de dados, imprimindo o saldo por um método

    