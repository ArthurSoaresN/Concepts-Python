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