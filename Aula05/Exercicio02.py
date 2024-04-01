idade = int(input("Digite sua idade:"))
if idade >= 5 and idade <= 7:
    print("Sua categoria é Infantil!")
elif idade >= 8 and idade <= 10:
    print("Sua categoria é Juvenil!")
elif idade >= 11 and idade <= 15:
    print("Sua categoria é Adolescente!")
elif idade >= 16 and idade <= 30:
    print("Sua categoria é Adulto!")
else:
    print("Sua categoria é Sênior!")
