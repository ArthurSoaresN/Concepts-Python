def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    
    reservas_confirmadas = []
    reservas_rejeitadas = []
    
    tamanho = len(reservas_solicitadas)
    
    for i in range(tamanho):
      if reservas_solicitadas[i] in quartos_disponiveis:
        reservas_confirmadas.append(reservas_solicitadas[i])
      else:
        reservas_rejeitadas.append(reservas_solicitadas[i])
      
    
    

    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos: 
    

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, reservas_confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, reservas_rejeitadas)))

# Chamada da função principal
processar_reservas()