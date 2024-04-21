from random import randint

m, l = [], []

for y in range(5):
    for x in range(5):
        l.append(randint(1,100))
    m.append(l)
    l = []
print(m)

soma = 0
quantidade = 0

for y in range(0,5,2):
    for x in range(5):
        soma = soma + m[y][x]
        quantidade = quantidade + 1

media = soma / quantidade
print(f'{media=}')
