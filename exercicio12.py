eleitores = int(input("Informe a quantidade de eleitores do múnicipio: "))
brancos = int(input("Quantos votos brancos tiveram a eleição? "))
nulos = int(input("Quantos votos nulos tiveram a eleição? "))
validos = int(input("Quantos votos válidos tiveram a eleição? "))
pct_brancos = (brancos * 100)/eleitores
pct_nulos = (nulos * 100)/eleitores
pct_validos = (validos * 100)/eleitores
print(f"A porcentagem de votos brancos é {pct_brancos}%")
print(f"A porcentagem de votos nulos é {pct_nulos}%")
print(f"A procentagem de votos válidos é {pct_validos}%")