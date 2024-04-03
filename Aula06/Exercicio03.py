import math

comprimento = float(input("Valor do comprimento em metros:"))
largura = float(input("Valor da largura em metros:"))
lata_de_tinta = float(input("Volume da lata de tinta em litros:"))

pe_direito = 2.80
porta = 0.80 * 2.10

parede = comprimento * largura * pe_direito
aposento = (4 * parede) - porta
litros_de_tinta = aposento / 3

quantidade_de_lata = math.ceil(litros_de_tinta / lata_de_tinta)

print("A quantidade de lata para seu aposento é de:", quantidade_de_lata)


