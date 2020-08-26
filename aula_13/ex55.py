#   MAIOR E MENOR PESO
maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input("Peso da {}º pessoa: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("\nO maior peso foi de {}kg".format(maior))
print("O menor peso foi de {}kg".format(menor))