
dados = list()
cadastro = list()
maior = menor =  0


while True:
    dados.append(str(input("Nome: ")).upper())
    dados.append(float(input("Peso: ")))
    #   Maior e menor peso
    if len(cadastro) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    cadastro.append(dados[:])
    dados.clear()

    opçao = " "
    while opçao not in "SN":
        opçao = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if opçao == "N":
        break 

print("+"*30)
print(f"Foram cadastrados {len(cadastro)} pessoas")
print(f"O maior peso foi {maior}Kg, da(o) ", end="")
for c in cadastro:
    if c[1] == maior:
        print(f"{c[0]}")

print(f"O menor peso foi {menor}Kg da(o) ", end=" ")
for c in cadastro:
    if c[1] == menor:
        print(f"{c[0]}", end="")

