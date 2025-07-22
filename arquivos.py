# Formatos txt e csv (trocas de informação)

# Os arquivos são essenciais por fornecer um meio de armazenar e recuperar dados
# Através da manipulação de arquivos, podemos persistir os dados além da vida útil
# de programas específicos

# Um arquivo é um container no computador, onde as informações são armazenadas em formato digital
# Em Python podemos manipular arquivos de texto e binários

# file = open('example.txt', 'r')
# file = open('example.txt', 'w')
# file = open('example.txt', 'a')

# Método read, readline, readlines

# -*- coding: utf-8 -*-

arquivo = open("arq.txt", "r") # Caminho relativo
print(arquivo.read())
arquivo.close()