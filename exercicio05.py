num = int(input("Digite um número: "))
while num == 0:
    num = int(input("O número precisa ser DIFERENTE DE 0. Tente digitar novamente: "))
if num % 2 == 0:
    print(f"{num} é PAR")
else:
    print(f"{num} é ÍMPAR")