perg = "s"
while perg == "s":
    num = int(input("Informe um número: "))
    num2 = int(input("Informe um número: "))
    num3 = int(input("Informe um número: "))

    if num > num2:
        if num > num3:
            print(f"O maior é {num}")
        else:
            print(f"O maior é {num3}")
    else:
        if num2 > num3:
            print(f"O maior é {num2}")
        else:
            print(f"O maior é {num3}")
    perg = input("Deseja repetir atividade? ")
else:
    print("Obrigada!")
