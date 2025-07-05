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

# Dicionarios aninhados
# Podem armazenar qualquer tipo de objeto python como valor, desde que chave seja imutavel

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 20},
    "giovana@gmail.com": {"nome": "Giovana", "idade": 22},
    "jorge@gmail.com": {"nome": "Jorge", "idade": 25}, #virgula no final
}

print(type(contatos))

def show_info(email: str):
    if email in contatos:
        info = contatos[email]
        print(f"Informações para {email}:")
        print(f"  Nome: {info['nome']}")
        print(f"  Idade: {info['idade']}")
    else:
        print(f"Erro: O email '{email}' não foi encontrado nos contatos.")

show_info("jorge@gmail.com")