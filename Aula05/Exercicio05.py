import math

valor_a = float(input("Digite valor de a:"))
if valor_a == 0:
    print("A equação não é de 2º grau!")

else:
    valor_b = float(input("Digite valor de b:"))
    valor_c = float(input("Digite valor de c:"))

    delta = valor_b**2 - (4 * valor_a * valor_c)
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        resposta_unica = - valor_b / (2 * valor_a)
        print("A equação possui apenas uma raíz real:", resposta_unica)
    else:
        resposta_1 = (- valor_b + math.sqrt(delta))/(2 * valor_a)
        resposta_2 = (- valor_b - math.sqrt(delta))/(2 * valor_a)
        print(f"A equação possui duas raízes reais: \n\t x1= {resposta_1:.2f} \n\t x2= {resposta_2:.2f}")
