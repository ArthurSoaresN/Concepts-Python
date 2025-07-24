# Formatos txt e csv (trocas de informação)

# Os arquivos são essenciais por fornecer um meio de armazenar e recuperar dados
# Através da manipulação de arquivos, podemos persistir os dados além da vida útil
# de programas específicos

# Um arquivo é um container no computador, onde as informações são armazenadas em formato digital
# Em Python podemos manipular arquivos de texto e binários

# file = open('example.txt', 'r')
# file = open('example.txt', 'w')
# file = open('example.txt', 'a')

import csv
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


# Manipulação

# os.mkdir()
# os.remove()
# os.rename()
# shutil.move()

# Tratamento de erros em Python c/ exceções

# FileNotFoundError: Quando não encontra o arquivo no diretório especificado
# PermissionErro: Quando a tentativa de manipular o arquivo falha por falta de permissão
# IOError: Erro geral de E/S (Ex: falta de espaço)
# UnicodeDecodeError: Erro de decodificação de dados em um arquivo de texto usando codificação inadequada
# UnicodeEncodeError: Erro quando tenta codificar dados em uma determinada codificação ao gravar em um arquivo de texto
# IsADirectoryErro: Tentativa de abrir um diretório e não um arquivo

print()
try:
    arquivo3 = open("meu_arquivo.txt")
except FileNotFoundError as exc:
    print("Erro:")
    print(exc)

# BOAS PRATICAS

# BLOCO WITH

# Context manager, para trabalhar com arquivos de forma segura
# garantir o fechamento do arquivo

# VERIFICAR

# Verificação se o arquivo foi aberto com sucesso ou não

# CODIFICAÇÃO

# Usar a codificação correta
# with open(ROOT_PATH/'arquivo-utf-8.txt'm encondig="utf-8") as arquivo:


# ARQUIVO CSV

# formato de arquivo usado para armazenar dados tabulares
# (Comma Separated Values)   
# Python fornece o modulo csv
# usar csv.reader e csv.writer para manipular arquivos CSV
# usar o argumento newline no metodo open()