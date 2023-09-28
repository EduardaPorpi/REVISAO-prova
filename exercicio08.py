soma = 0
qnt = int(input("Com quantos números iremos trabalhar? "))
for x in range (qnt):
    num = float(input("Digite um número: "))
    soma += num
media = soma/qnt
print(f"A soma desses números é {soma} e a média entre eles é {media}")