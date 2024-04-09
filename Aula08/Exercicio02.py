data = input("Digite a data dd/mm/aaaa:")
info = data.split("/")
dia = info[0]
mes = info[1]
ano = info[2]
data_invertida = ano + mes + dia
print(data, " - ", data_invertida)