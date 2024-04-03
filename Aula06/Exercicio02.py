preco = float(input("Preço:"))

if preco <= 1000:
    print(f"Valor total com desconto de 10% R$:{preco - (preco * 10/100):.2f}")

elif preco <= 5000:
    print(f"Valor total com desconto de 20% R$:{preco - (preco * 20/100):.2f}")

else:
    print(f"Valor total com desconto de 30% R$:{preco - (preco * 30/100):.2f}")
