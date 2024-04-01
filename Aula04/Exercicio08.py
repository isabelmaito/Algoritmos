deposito = int(input("Digite o valor do depósito:"))
juros = float(input("Digite a taxa de juros:")) /100
rendimento = deposito * juros
total = deposito + rendimento
print(f"Valor do rendimento: R${rendimento:.2f}")
print(f"Valor total do rendimento: R${total:.2f}")