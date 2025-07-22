# Formatos txt e csv (trocas de informação)

# Os arquivos são essenciais por fornecer um meio de armazenar e recuperar dados
# Através da manipulação de arquivos, podemos persistir os dados além da vida útil
# de programas específicos

# Um arquivo é um container no computador, onde as informações são armazenadas em formato digital
# Em Python podemos manipular arquivos de texto e binários

# file = open('example.txt', 'r')
# file = open('example.txt', 'w')
# file = open('example.txt', 'a')

import os
import shutil
from pathlib import Path

print()
ROOT_PATH = Path(__file__)
print(f">>>> {ROOT_PATH.parent} <<<<")
print()
# Método read, readline, readlines

# read
arquivo = open("arq.txt", "r") # Caminho relativo
print(arquivo.read())
arquivo.close()

# readline
# Ele retorna linha a linha

# readlines
# Ele itera o retorno de linha a linha

# Podemos usar write() ou writelines() para escrever em um arquivo


escrita = open("teste.txt", "w")
escrita.write("Escrevendo em arquivos usando Python")
escrita.close()

# Python tambem oferece funções para gerenciar arquivos e diretorios.
# Podemos criar, renomear e excluir arquivos e diretórios usando
# os módulos 'os' e 'shutil'

