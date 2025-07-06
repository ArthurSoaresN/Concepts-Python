eventos = {}

n = int(input().strip()) # .strip() remove espaços extras no início/fim, int() converte para número

for _ in range(n):
    linha = input().strip()
    
    # Divide a string no primeiro ", " encontrado (vírgula seguida de espaço)
    # Ex: "Lucas, Fotografia" -> ["Lucas", "Fotografia"]
    partes = linha.split(', ', 1) # O '1' garante que ele divida apenas uma vez
    
    nome_participante = partes[0] 
    tema_escolhido = partes[1]
    
    # Se o 'tema_escolhido' já existe como chave no dicionário 'eventos':
    if tema_escolhido in eventos:
        # Adiciona o 'nome_participante' à lista de participantes daquele tema
        eventos[tema_escolhido].append(nome_participante)
    else:
        # Se o 'tema_escolhido' não existe, cria uma nova entrada no dicionário
        # e a associa a uma nova lista contendo o primeiro participante daquele tema
        eventos[tema_escolhido] = [nome_participante]

# Loop pelos itens do dicionário (pares chave-valor)
for tema, participantes_lista in eventos.items():
    # Usa ', '.join(participantes_lista) para transformar a lista de nomes
    # em uma string única separada por vírgula e espaço (ex: "Lucas, Carlos")
    print(f"{tema}: {', '.join(participantes_lista)}")