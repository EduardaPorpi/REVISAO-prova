base = float(input("Informe o valor da BASE do triângulo em cm: "))
while base <= 0:
    base = float(input("A base precisa ser DIFERENTE DE 0. Tente novamente: "))
altura = float(input("Informe a ALTURA do triângulo em cm: "))
while altura <= 0:
    altura = float(input("A altura precisa ser DIFERENTE DE 0. Tente novamente: "))
area = (base * altura)/2
print(f"A área do triângulo informado é {area:.1f}cm²")