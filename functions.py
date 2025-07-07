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

