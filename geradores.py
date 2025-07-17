# Geradores

# São tipos especiais de iteradores, ao contrário das listas ou outros iteráveis
# não armazenam todos os seus valores na memória
# São definidos usando funções regulares, mas não returna valores usando "return" utilizam "yield"

# Caracteristicas

# Uma vez que um item gerado é consumido, ele é esquicido e não pode ser acessado de novo
# O estado interno de um gerador é mantido entre chamadas
# A execução de um gerador é pausado na declaração "yield" e retoma dai na proxima vez que for chamado