# Conhecer os decoradores e como usar

# Em python as funções são cidadãs de primeira classe

# Inner functions
# "Funções Internas"

def pai():
    print("Function Pai")

    def filho1():
        print("Function Filho1")
    
    filho1()

pai()

def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("execitando mensagem longa")
    return f"Olá tudo bom {nome}?"

def executar(funcao, nome):
    print("execuntando executar")
    return funcao(nome)

print(executar(mensagem, "Joao"))

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes") # EXEMPLO: Verificação
        funcao()
        print("Faz algo depois") # EXEMPLO: Aprovação
    return envelope

# Açucar sintatico
# O Python permite que voce use decoradores com o simbilo @
# @meu_decorador -> DECORADOR com acucar sintatico -> basta so chamar a função
def ola_mundo():
    print("Ola mundo")

ola_mundo = meu_decorador(ola_mundo) # Sem acucar sintatico
ola_mundo()

def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs) # Para não quebrar a função
        func(*args, **kwargs)
        # Pode ter um return aqui
    return envelope

@duplicar # Decorador
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")

aprender("Python")

# Introspecção
# Capacidade de um objeto saber sobre seus propios atributos em tempo de execução