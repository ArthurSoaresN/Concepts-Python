# Conjunto não ordenado de pares
# Chave: Valor
# As chaves são imutáveis

# Dicionários são delimitados por chaves e contem uma lista de pares separados por vigulas

pessoa = {
    "nome": "Jose",
    "idade": 20
}

pessoa2 = dict(nome= "Carlos", idade = 22)
# Usando o construtor dict

pessoa["telefone"] = "7499658256"
# Adcionando uma chave no dicionário pessoa

print(pessoa)