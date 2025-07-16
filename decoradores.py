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