def sacar(valor) -> None:
    saldo = int(valor)
    print(saldo)


sacar(500)

teste = sacar(20)

print(teste)

x = 10
y = 100

status = 1 if x >= y else 0

print(status)

nome = "Arthur"

for i in range(len(nome)):
    print(nome[i].upper(), end=' ')
print()