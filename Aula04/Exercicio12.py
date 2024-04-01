degrau_cm = float(input("Valor da altura do degrau em cm:"))
altura_metros = float(input("Valor da altura em metro:"))
degrau_metros = degrau_cm / 100
qtd_degraus = altura_metros / degrau_metros

print("Quantidade de degraus:", qtd_degraus)