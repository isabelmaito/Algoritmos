from random import randint

m = []
l = []
for y in range(4):
    for x in range(4):
        l.append(randint(1,100))
    m.append(l)
    l = []
print(m)
soma = 0

for i in range(4):
    soma = soma + m[i][i]
print(f'{soma=}')