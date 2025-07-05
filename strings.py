palavra = "PyThOn"

print(palavra.upper())
print(palavra.lower())
print(palavra.title())

palavra2 = "         Python    "

print(palavra2.strip())
#remove espaço das strings
print(palavra2.lstrip())
print(palavra2.rstrip())
#left and right

palavra3 = "Teste"
print(palavra3.center(10, "!"))
print(".".join(palavra3))

#format

PI = 3.14159

print(f"Valor de PI formantando com .2f: {PI:.2f}")
print(f"Valor de PI: {PI}")

print("Nome: %s Idade: %d" % ("Jose", 18))
print("Nome {} Idade: {}".format("Carlos", 22))

#Fatiamento de strings
#Retornar partes da string

Nome = "Jose Carvalho"

print(Nome[0]) #Acessando por indice
print(Nome[10:]) # Tirou os 10 primeiros elementos e imprimiu o resto
print(Nome[:10]) # Imprimiu os primeiros 10 elementos da string
print(Nome[-1]) # Acessando os indices com numeros negativos
print(Nome[::-1]) #Inverte a String

#Strings triplas/multiplas
#Util para criar menus

nome1 = "Louise"

Tripla = f'''Essa é a primeira linha
Essa é na segunda linha
Essa é a Terceira linha
Nome informado by {nome1}'''

print(Tripla)