lista = []
for i in range(5):
    lista.append(int(input(f'Entre com o valor {i}:')))

print(f'O maior valor é {max(lista)}')
print(f'E sua posição é {lista.index(max(lista))}')