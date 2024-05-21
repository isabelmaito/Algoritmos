def ePrimo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def testePrimo(n):
    primo = 0
    for i in range(n + 1):
        if ePrimo(i):
            primo += 1
    return primo


def somaPrimo(n):
    total = 0
    for i in range(n+1):
        if ePrimo(i):
            total += i
    return total


entrada = int(input("Digite um número: "))

print(f"O número {entrada} {"é" if ePrimo(entrada) else "não é"} primo")
print(f"De 0 até {entrada} tem {testePrimo(entrada)} números primos")
print(f"A soma desses números é {somaPrimo(entrada)}")
