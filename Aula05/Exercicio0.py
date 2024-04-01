nota1 = float(input("Valor da primeira nota:"))
nota2 = float(input("Valor da segunda nota"))

if nota1 > nota2:
    print("Esse é o maior valor:", nota1)
else:
    if nota2 > nota1:
        print("Esse é o maior valor:", nota2)
    else:
        print("As notas são iguais")
