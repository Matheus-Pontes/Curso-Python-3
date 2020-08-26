

num = list()
pos = 0
while True:
    num.append(int(input("Digite um valor: ")))

    option = " "
    while option not in "SN":
        option = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    if option == "N":
        break

print("="*30)
print(f"Você digitou a seguinte lista {num}")
print(f"Foram digitados {len(num)} termos")

if 5 in num:
    print("O número 5 está na lista, ", end="")
    for pos, n in enumerate(num):
        if n == 5:
            print(f"{pos}...", end="")
        pos += 1
else:
    print("\nO número 5 não esta na lista")

num.sort(reverse=True)
print(f"\nA lista em ordem decrescente é {num}")
        
