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