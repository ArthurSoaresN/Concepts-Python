# Conjunto não ordenado de pares
# Chave: Valor
# As chaves são imutáveis

# Dicionários são delimitados por chaves e contem uma lista de pares separados por vigulas

import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


#main
limpar_tela()

pessoa = {
    "nome": "Jose",
    "idade": 20
}

pessoa2 = dict(nome= "Carlos", idade = 22)
# Usando o construtor dict

pessoa["telefone"] = "7499658256"
# Adcionando uma chave no dicionário pessoa

print(pessoa)
print(pessoa2)

# Para acessar o conteudo de uma chave

print(pessoa["nome"])

# Sobre-escrevendo

pessoa["nome"] = "Marcos"

print(pessoa)