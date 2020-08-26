#   A soma dos números ímpares e multiplos de 3 
#   NO INTERVALO DE 1 A 500
soma = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
print("A soma de todos os números {}".format(soma))