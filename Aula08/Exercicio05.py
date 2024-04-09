frase = input("Digite uma frase:").strip()
palavras = frase.split()
frase1 = ''

for palavra in palavras:
    frase1 = frase1 + palavra
frase2 = frase1[::-1]
if frase1 == frase2:
    palindromo = True
else:
    palindromo = False
if palindromo:
    print("É um palindromo.")
else:
    print("Não é um palindromo.")

