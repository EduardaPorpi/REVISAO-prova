qnt = int(input("Quantas maçãs foram compradas? "))
if qnt >=12:
    valor = qnt * 1.00
    print(f"Foram compradas {qnt} maçãs a R$1,00 cada totalizando R${valor:.2f} ")
else:
    valor = qnt * 1.30
    print(f"Foram compradas {qnt} maçãs a R$1,30 cada totalizando R${valor:.2f}")