# Metodos de classe estão ligados a classe e não ao objeto.
# Eles têm acesso ao estado da classe, pois recebem um parâmetro
# que aponta para a classe e não para a instância do objeto.

# Metodos estáticos não recebe um primeiro argumento
# Ele tambem é um metodo vinculado a classe e não ao 
# objeto da classe. Este método não pode acessar ou modificar o estado
# da classe. Ele está presente em uma classe porque faz sentido
# que o método esteja presente na classe

# Metodo de classe pode acessar ou modificar o estado
# graças ao primeiro argumento que se referencia

# Geralmente usamos metodos estaticos para criar funções
# utilitárias

ANO_ATUAL = 2025

class Pessoa:
    def __init__(self, nome: None, idade: None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_por_data_nascimento(self, ano, dia ,mes, nome):
        idade = ANO_ATUAL - ano
        return Pessoa(nome, idade)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18

p1 = Pessoa.criar_por_data_nascimento(1994, 13, 5, "Carlos")
print(p1.nome, p1.idade)

print(Pessoa.maior_de_idade(18)) 
print(Pessoa.maior_de_idade(12)) 