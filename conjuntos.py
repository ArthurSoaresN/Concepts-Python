# Conjuntos não possui objetos repetidos, usamos sets para representar conjutos
# set(lista) -> remove duplicidades
# a lista nao é retornada com garantia de ordem igual

linguagens = {"Java", "C", "C++", "JavaScript"} # set/conjunto

#Para acessar os indices ele precisa ser convertido para lista

linguagens = list(linguagens)
print(linguagens[0])
# a saida nao referenciou o indice 0 em alguns testes

# Metodos da classe set

# {}.union cocatenação de conjuntos
# {}.intersection -> Retornar a interceção de dois conjutnos: conjunto1.intersection(conjunto2)
# {}.difference -> Retorna a diferença entre dois conjuntos
# {}.symmetric_difference -> Retorna o que bão está na interceção
# {}.issubet -> returna true ou false, ele esta se um conjunto esta contido em outri
# {}.issuperset -> testa se o conjunto passado como argumento esta contido no conjunto.issuperset()
# {}.isdisjoint -> testa se dois conjuntos não estão juntos (se contem numeros em comum)
# {}.add -> adiciona elemento (Se ele não existe no conjunto)
# {}.clear -> limpar conjunto
# {}.copy -> copiar conjunto
# {}.discard -> Discartar o argumento passado 
# {}.pop -> Retira o elemento de indice 0
# {}.remove -> Difente do discard ele retornar erro ao passar um argumento inexistente
# len() -> tamanho do conjunto
# in -> Operador de pertencimento
