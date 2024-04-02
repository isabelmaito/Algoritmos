lado_1 = float(input("Lado 1:"))
lado_2 = float(input("Lado 2:"))
lado_3 = float(input("Lado 3:"))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    # Avaliar tipo de triângulo
    if lado_1 == lado_2 == lado_3:
        print("Triângulo Equilátero")
    elif lado_1 == lado_2 or lado_3 == lado_2 or lado_3 == lado_1:
        print("Triângulo Isósceles")
    else:
        print("Trângulo Escaleno")
else:
    print("Os lados fornecidos não formam um triângulo!")