import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#main
limpar_tela()

#Função é um bloco de código identificado por um nome e pode receber parâmetros

def exibir_mensagem(nome):
    print(f"Ola {nome}!")

exibir_mensagem("Jose")