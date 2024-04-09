v = 0
frase = input("Digite uma frase:")

for vogal in "AEIOUaeiou":
   v = v + frase.count(vogal)

print(f"A frase têm {v} vogal(is).")