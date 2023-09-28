idade = int(input("Digite sua idade: "))
mes_nasc = int(input("Em que mês você nasceu? "))
ano = int(input("Em que ano estamos? "))
mes_a = int(input("Em que mês estamos? "))

if mes_a < mes_nasc:
     nasc = (ano - idade) - 1
     print(f"O ano de nascimento é: {nasc}")
else:
    nasc = ano - idade
    print(f"O ano de nascimento é {nasc}")