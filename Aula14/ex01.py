def bichos (cab, pe):
    coelhos = (pe - (2 * cab))/2
    patos = (cab - coelhos)

    print(f"Total de coelhos: {coelhos}")
    print(f"Total de patos: {patos}")

x = int(input("Digite seu RA: "))
cab = x
pe = (x * 3)+3

print(f"Quantidade total de cabeças é {cab}")
print(f"Quantidade total de pés é {pe}")

bichos(cab, pe)