pergunta = "s"
while pergunta == "s":
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    media = (nota1 + nota2)/2
    if media < 7:
        if media >= 4:
            print(f"O aluno está em RECUPERAÇÃO com média {media}")
        else:
            print(f"O aluno está REPROVADO com média {media}")
    else:
        print(f"O aluno está APROVADO com média {media}")
    pergunta = input("Deseja continuar calculando? ")
else:
    print("Obrigada!")
    