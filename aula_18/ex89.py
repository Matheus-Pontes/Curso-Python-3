ficha = list()

print("-="*3,  f"{'Verificando Boletim'}", "=-"*3)

while True:    
    nome = str(input("Nome: ")).upper()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    continuar = " "
    while continuar not in "SN":
       continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    if continuar == "N":
        break
print("="*30)
print(f"{'No.'} {'NOME':>8} {'MÉDIA':>14}")
print("="*30)

for c, f in enumerate(ficha):
    print(f"{c} {f[0]:>12} {f[2]:>11.1f}")
print("="*30)
while True:
    
    opçao = int(input("Qual nota quer ver?[999 para parar]: "))    
    
    if opçao == 999:
        break
    if opçao <= len(ficha) - 1:
        print(f"As notas do {ficha[opçao][0]} foram {ficha[opçao][1]}")


print("FIM DA SESSÃO")
