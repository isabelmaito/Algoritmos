from random import randint

resultados = [0]*13
frequencia = [0]*13

for _ in range(30000):
    lado1 = randint(1, 6)
    lado2 = randint(1, 6)
    soma = lado1 + lado2
    resultados[soma] = resultados[soma] + 1

print(f'{resultados[lado1]}, {resultados[lado2]}')

for i in range(2, 13):
    frequencia[i] = (resultados[i] / 30000) * 100

for i in range(2, 13):
    print(f'{i} - {resultados[i]} - {frequencia[i]:6.2f}%')
