inicio = int(input("Informe a hora de ínicio do jogo de xadrez no formato 24h: "))
fim = int(input("Informe a hora de ínicio do jogo de xadrez no formato 24h: "))
if fim < 12:
    jogo = (24 - inicio)+fim
else:
    jogo = fim - inicio
print(f"O jogo de xadrez teve {jogo}h")