

numeros = [[], []]

valor = 0

for c in range(0, 7):
    valor = int(input(f"Digite {c}º número: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print("="*20)

numeros[0].sort()
numeros[1].sort()

print(f"Os valores pares digitados foram {numeros[0]}")
print(f"Os valores ímpares digitados foram {numeros[1]}")

   






