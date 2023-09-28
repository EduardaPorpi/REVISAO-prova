pergunta = 0
while pergunta != "3":
    num = int(input("Digite um número: "))
    pergunta = input("Digite 1 para mostrar o antecessor, 2 para mostar o sucessor ou 3 para encerrar o sistema: ")
    if pergunta != "1" and pergunta != "2" and pergunta != "3":
        pergunta = input("As opções são 1 ou 2 ou 3. tente novamente: ")
    elif pergunta == "1":
        print(f"O antecessor de {num} é {num - 1}")
    elif pergunta == "2":
        print(f"O sucessor de {num} é {num +1}")
else:
    print("ENCERRADO!")
