while True:
    idade = input("Digite sua idade:")
    if idade.isdigit():
        idade = int(idade)
        break
    else:
        print("Apenas números!")
