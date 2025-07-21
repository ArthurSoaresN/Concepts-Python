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