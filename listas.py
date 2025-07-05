import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_type(argumento, nome_variavel: str):
    tipo = type(argumento)
    print(f"Classe de {nome_variavel} é: {tipo}")

# main
limpar_tela()

frutas = []
show_type(frutas, "frutas")

lista1 = list()

show_type(lista1, "lista1")
print()
print("lista1 foi criado com list()")
print("frutas foi criado com []")
print()

print("Adicionando maça a lista frutas usando append: frutas.append")
frutas.append("Maça")
print("imprimindo o indice 0:")
print(frutas[0]) #Maça

numeros = [1,2,3,4,5,6,7,8,9]
numeros_pares = []
numeros_impares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print()
print(numeros)
print(numeros_pares)
print(numeros_impares)

# list() é uma classe
# Metodos

# [].append para adicionar elementos na lista
# [].clear para limpar a lista
# [].copy para copiar lista (pode ser usado para imutabilidade da lista original)
# [].count contar quantos vezes um objeto aparece na lista
# [].extend para cocatenar listas lista.extend(lista2)
# [].index mostra o indice da primeira ocorrencia do objeto passado como argumento / lista.index(argumento) -> indice
# [].pop adicionar elementos com a estrutura de PILHA (Last in First Out)
# [].remove para remover o elemento passado com argumento
# [].reverse inveter a lista
# [].sort ordenar lista lista.sort(tipo de ordenação)

# Trupla - "Irmã da lista"

# São estruturas de dados que são imutáveis enquanto as listas são mutáveis
# Podemos criar Truplas usando a classe tuple ou usando parenteses lista = ()
# Boa pratica: Colocar , no final do ultimo elemento da tuple para o python identificar que o () não se trata de precedencia de operadores
# Python usa a , final para identificar tuple

numeros_tuple = (1,2,3,4,)

show_type(numeros_tuple, "numeros_tuple")
print(numeros_tuple)

#Acessando elemento
print(numeros_tuple[0])

#fatiamento
# trupla[2:0]
# trupla[1:3]

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

#matriz imutavel