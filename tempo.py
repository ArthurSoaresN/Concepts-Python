# modulo datetime

import datetime

d = datetime.date(2023, 7, 9) #ano, mes, dia
print(d)
print(datetime.datetime.today())

# Manipulando datas com timedelta
# Operação matematica com datas

data = datetime.datetime(2025, 7, 21, 1, 30)
data2 = data + datetime.timedelta(weeks=1)
print(data)
print(data2)

data_atual = datetime.datetime.now()
tempo_estimado1 = 30
tempo_estimado2 = 45
tempo_estimado3 = 60   


print(
    f"Agora são {data_atual}, "
    f"tempo estimado para entrega é de: {data_atual + datetime.timedelta(minutes=tempo_estimado1)}"
)

print(
    f"Agora são {data_atual}, "
    f"tempo estimado para entrega é de: {data_atual + datetime.timedelta(minutes=tempo_estimado2)}"
)

print(
    f"Agora são {data_atual}, "
    f"tempo estimado para entrega é de: {data_atual + datetime.timedelta(minutes=tempo_estimado3)}"
)

# Conversão e formatação de datas com strftime e strptime
# parse -> conversão

print(data_atual.strftime("%d/%m/%Y")) # Dia/Mes/Ano

data_atual_Brasil = data_atual.strftime("%d/%m/%Y %H:%M")
mascara_ptbr = "%d/%m/%Y %H: %M"

print(
    f"Agora são {data_atual_Brasil}, "
    f"tempo estimado para entrega é de: {(data_atual + datetime.timedelta(minutes=tempo_estimado2)).strftime('%d/%m/%Y %H:%M')}"
)