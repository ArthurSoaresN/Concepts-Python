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