preco = float(input("Preço:"))
codigo = int(input("Código de Origem:"))
origem_1 = 1
origem_2 = 2
origem_3 = 3
origem_4 = 4
origem_5 = 5

if codigo == origem_1:
    print(f"Procedência Sul R$:{preco * 1.11:.2f}")
elif codigo == origem_2:
    print(f"Procedência Norte R$: {preco * 1.13:.2f}")
elif codigo == origem_3:
    print(f"Procedência Nordeste R$: {preco * 1.09:.2f}")
elif codigo == origem_4:
    print(f"Procedência Centro-Oeste R$: {preco * 1.12:.2f}")
elif codigo == origem_5:
    print(f"Procedência Sudeste R$: {preco * 1.18:.2f}")
else:
    print("Esse código não existe.")
