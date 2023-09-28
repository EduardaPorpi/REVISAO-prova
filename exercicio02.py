perg = "s"
while perg == "s" or perg == "S":
    num = int(input("Digite um número: "))
    while num == 0:
        num = int(input("O número precisa ser diferente de zero. Tente novamente: "))
    if num > 0:
        print(f"{num} é POSITIVO")
    else:
        print(f"{num} é NEGATIVO")
    perg = input("Deseja continuar? ")
else:
    print("Obrigada!")