n = int(input().strip())

pacientes = []

for _ in range(n):
    nome, idade_str, status = input().strip().split(", ")
    idade = int(idade_str) # Converte a idade para inteiro
    pacientes.append((nome, idade, status)) # Adiciona a tupla à lista de pacientes

# --- TODO: Ordene por prioridade: urgente > idosos > demais ---

pacientes_urgentes = []
pacientes_idosos = []
pacientes_normais = []

for paciente in pacientes:
    # paciente[0] é o nome, paciente[1] é a idade, paciente[2] é o status
    
    if paciente[2] == "urgente":
        pacientes_urgentes.append(paciente)
    elif paciente[1] >= 60:
        pacientes_idosos.append(paciente)
    else:
        pacientes_normais.append(paciente)

pacientes_urgentes.sort(key=lambda p: p[1], reverse=True)

# Concatena as listas na ordem de prioridade
lista_pacientes_ordenada = []
lista_pacientes_ordenada.extend(pacientes_urgentes)
lista_pacientes_ordenada.extend(pacientes_idosos)      
lista_pacientes_ordenada.extend(pacientes_normais)      

# Extrai APENAS os nomes dos pacientes da lista ordenada de tuplas
nomes_ordenados = [paciente[0] for paciente in lista_pacientes_ordenada]

# Formata a string de saída usando ', '.join()
formatar_ordem = ", ".join(nomes_ordenados)

print(f"Ordem de Atendimento: {formatar_ordem}")