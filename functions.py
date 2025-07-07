import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#main
limpar_tela()

#Função é um bloco de código identificado por um nome e pode receber parâmetros

def exibir_mensagem(nome:str):
    print(f"Ola {nome}!")

exibir_mensagem("Jose")

def imprimir_pi(pi: float = 3.14):
    print(f"Valor definido para Pi: {pi}")

imprimir_pi()
imprimir_pi(3.14159)

#(*args e **kwargs)
# tuple e dicionario

#Positonal Only
#Por posição
# def function (arg1,arg2,arg3):


#Keyword Only
# def function (*, arg1, arg2):
# Precisa atribuir os valores aos nomes

#Hibrido
# def function (arg1, agr2, /, *, arg3, arg4):

# Em Python as functions são cidadãs de primeira classe, podemos usá-las como valor

def somar(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def executar(a,b,function):
    resultado = function(a,b)
    print(f"Resultado da operação: {resultado}")

executar(10,5,somar)
executar(10,5,subtrair)

# Em python para usar as variaveis globais no escopo das functions, usa-se a palavra reservada "global"
# Não é considerada uma boa prática em python

salario = 2000

def salario_bonus(bonus):
    global salario
    salario = salario + bonus
    return salario

aumento = salario_bonus(400)
print(aumento)
print(salario) # Modificar o valor da variavel dentro do escopo da função, algo como o uso de ponteiros em C

#teste
def funcao(*args, **kw):
    print("args:", args)
    print("kw:", kw)

funcao("python", 2022, curso="dio")