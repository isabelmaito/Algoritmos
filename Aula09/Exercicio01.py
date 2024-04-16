lista = []
for i in range(10):
    valor = int(input(f'Digite o valor {i+i}:'))
    lista.append(valor)

print(lista[::-1])

for i in range(9, -1, -1):
    print(lista[i], end=',')

print()

lista.reverse()
print(lista)