num = list()
pares = list()
impares = list()

while True:
    num.append(int(input("Digite um valor: ")))

    opçao = ' '
    while opçao not in  "SN":
        opçao = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    if opçao == "N":
        break

for n in num:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)



print(f"A lista gerada foi {num}")
print(f"A lista com os números pares foi {pares}")
print(f"A lista com os números ímpares foi {impares}")
