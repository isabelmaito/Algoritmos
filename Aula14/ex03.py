x = input("Digite um numero: ")


def soma(args):
    total = 0
    for i in args:
        total += int(i)
    return total


print(f"A soma dos números é: {soma(x)}")


def mult(args):
    total = 1
    for i in args:
        total *= int(i)
    return total


print(f"A multiplicação dos números é: {mult(x)}")
