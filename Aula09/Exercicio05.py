from random import randint

resultados = [0]*7
frequencia = [0]*7
print(resultados)

for _ in range(6000):
    lado = randint(1, 6)
    resultados[lado] = resultados[lado] + 1

for i in range(1, 7):
    frequencia[i] = (resultados[i] / 6000) * 100

for i in range(1, 7):
    print(f'{i} - {resultados[i]} - {frequencia[i]:6.2f}%')