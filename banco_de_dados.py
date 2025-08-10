# Coleção organizada de informações estruturadas, armazenadas eletronicamente
# em um sistema de computador

# Tipos mais usados: relacional e não relacional
# Relacional: Organizado em tabelas, com colunas e linhas com relação entre si
# Exemplo: SQL Server, ORACLE DataBase, MySQL

# Tabelas: São dados organizados logicamente em formato de linha e coluna
#   ------------------------------------------
#  | ID | NOME | SOBRENOME | EMAIL | CADASTRO |
#   ------------------------------------------

# Estrutura rigida no padrão

# DBMS (DataBase Management System): Software para acessar, manipular e monitorar
# um sistema de banco de dados

# Conceitos Básicos

# Relacionais (SQL) / Não Relacionais (NoSQL) / Orientado a Objetos / Hierárquico

# SGBD (Criação e manipulação da banco de dados) Ex: MySQL
# Create, Read, Update, Delete

# Relacionamento entre Tabelas
# Linguagem de Consulta Estruturada
# Integridade referencial
# Normalização de dados
# Segurança
# Flexibilidade e extensibilidade
# Suporte a transações ACID

# ACID

# Atomicidade
# Consistencia
# Isolamento
# Durabilidade

# SQL - Structured Query Language

# Sintaxe Basica: Nomenclatura
# Os nomes devem começar cm Cactere sublinhado
# Os nomes podem conter letras, numeros e caractes de sublinhado (_)
# Sensibilidade a maiusculas e minusculas

# Modelos: MER E DER

# MER é representado atraves de diagramas chamadados diagramas entidade-relacionamento (DER)
# Entidades são nomeados com substantivos concretos ou abstratos que representam forma clara
# sua função dentro do dominio, exemplo: Usuario
# Atributos: Caracteristicas ou propriedades das entidades

# Ex:

# CREATE TRABLE usuarios (
# id INT, 
# nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
# email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail do usuário',
# endereco VARCHAR(50) NOT NULL COMMENT 'Endereço do usuariom
# data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuario');

# INSENT INFO USUARIOS (id, nome, email, data_nascimento, endereco) VALUES (1, "Pamela", "pamela@email.com", "1993-07-05", "Avenida 1");

# SELECT = FROM 'usuarios'
# UPDATE {{tabela}} set {{coluna 1}} WHERE {{condição}}
# DELETE FROM {{tabela}} WHERE {{condição}}
# ALTER TABLE para modificar a estrutura de uma tabela
# DROP TABLE para remover uma tabela existente

# CHAVE PRIMARIA E ESTRANGEIRAS

# Chave primaria: identifica exclusivamente, não pode conter valores null
# uma tabela pode ter apenas uma PRIMARY KEY

# CREATE TABLE {{tabela}} ( ID PRIMARY KEY AUTOINCREMENT,...);

# Chave estrangeira: Usada para estabelecer e manter a integridade dos dados entre tabelas relacionadas
# Pode ser NULL ( registro orfão ), é possivel ter mais de uma em uma tabela
# FOREIGN KEY 

# Normalização de Dados
# Processo para organizar a estrutura de um banco de dados relacional de forma
# a eliminar redundancias e anomalias, garantindo a consistencai e integridade dos dados

# INNER JOIN "INTERSEÇÂO"

# Retorna apenas as linhas que contem as correspondencia de ambas as tabelas envolvidas na junção 

# LEFT JOIN "CONJUNTO A + INTERSEÇÂO"

# Retorna todas as linhas da tabela a esquerda da junção e as linhas correspondentes da tabela a direita

# RIGHT JOIN "CONJUNTO B + INTERSEÇÃO"

# Retorna as tabelas a direita da junção e as linhas correspondentes da tabela a esquerda

# FULL JOIN "A + B"

# Retorna todas as linahas de ambas as tabelas

# Funções Agregadas

# COUNT: Conta o numero de registros
# SUM: Soma os valores de uma coluna numerica
# AVG: Calcula a media dos valores de uma coluna numerica
# MIN: Retorna o valor minimo de uma coluna
# MAX: Retorna o valor máximo de uma coluna

# AGRUPAMENTO DE RESULTADOS

# SELECT...
# FROM...
# GROUP BY

# ORDENAÇÃO
# Order by

# NoSQL:
# Not Only SQL
# BD relacional: escalabilidade vertical (hardware)
# BD NoSql: escalabilidade horizontal (aperfeiçoando conforme a demanda)

# Introdução aos Bancos de dados Relacionais:

# Coleções de dados organizados (de maneira elotronica pelo contexto)
# Tipos: relacionais, não relacionasi e Orientado a Objetos

# Papel do SGDB
# Software para gerenciamento do Banco de Dados

# Banco de Dados Ralacional é um tipo que organiza os dados em tabelas
# Chave Primária -> ID para unicidade dos registros
# Chave Estrangeira -> Aponta para a chave primária criando um relacionamento entre dados
# Exemplo: Conexão de Pedidos (Feitos pelos Clientes) com os Clientes

# PYTHON DB API

# Usado para fazer a conexão com o Banco de Dados
# PSYCOPG -> Driver para trabalhar com banco de dados

import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect("clientes.db")
print(conexao)

# Cursor é o objeto que temos que recuperar para mexer no banco de dados

cursor = conexao.cursor()

# Criando tabela
# cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')

# A criação da tabela virou comentário para não criar outra tabela ao executar



# Inserção de registros

"""

data = ('Joao', 'joao@hotmai.com')
cursor.execute('INSERT INTO clientes(nome, email) VALUES (?,?)', data)
conexao.commit()

"""
# Atualizando registros

def criar_tabela(conexao, cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome,email)
    cursor.execute('INSERT INTO clientes(nome, email) VALUES (?,?)', data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=?, WHERE id=?', data)
    conexao.commit()

# A operação DELETE do SQL é usada para remover registros
# data = (id,)
# cursor.execute('DELETE FROM clientes WHERE id=?', data)

# Inserindo registro em lote
# Exemplo:
# cliente = (nome, email)
# data = [cliente1, cliente2, cliente2, cliente3... , cliente n]
# com menos commits, mais economia

# Consultas com unico resultado
# metedo fetchone() serve para recuperar um unico registro de resultado
# retorna o mais próximo ou None

# Alterando o row_factory
# cursor.row_factoty = sqlite3.row

# Gerenciamento de transações

try:
    cursor.execute("INSERT INTO minha_tabela(?,?)", (1, 'abc'))
    conexao.commit()
except Exception as erro:
    print(f"{erro}")
    conexao.rollback()
