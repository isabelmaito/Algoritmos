ano_nasc = int(input("Digite o ano que você nasceu:"))
ano_atual = int(input("Digite o ano atual:"))
idade_anos = ano_atual - ano_nasc
print("Idade em anos:", idade_anos)
print("Idade em meses:", idade_anos*12)
print("Idade em dias:", int(idade_anos*365.25))
print("Idade em semanas:", int(idade_anos*365.25/7))