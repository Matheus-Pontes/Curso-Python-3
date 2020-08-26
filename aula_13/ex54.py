#   ATINGINDO A MAIORIDADE
totmaior = 0
totmenor = 0

for c in range(1, 8):
    ano = int(input("Ano de nascimento da {}º pessoa: ".format(c)))
    idade = 2020 - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
        
print("Ao todo tivemos {} pessoas maior de idade.".format(totmaior))
print("Ao todo tivemos {} pessoas menor de idade.".format(totmenor))
