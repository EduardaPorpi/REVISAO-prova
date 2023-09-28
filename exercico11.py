print("Informe sua idade em")
idade_anos = int(input("Anos: "))
idade_meses = int(input("Meses: "))
idade_dias = int(input("Dias: "))
idade = (idade_anos * 365) + (idade_meses * 30) + idade_dias
print(f"Fazem {idade} dias que você nasceu")