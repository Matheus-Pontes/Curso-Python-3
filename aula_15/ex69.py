#   validando cadastro de uma pessoa

cont18 = contM = contF = 0
while True:
    print("="*30)
    print("     Cadastre uma pessoa:   ")
    print("="*30)

    idade = int(input("Idade: "))

    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

    if idade >= 18:
        cont18 += 1
    if sexo == "M":
        contM += 1
    if sexo == "F" and idade <= 20:
        contF += 1
    
    opçao = " "
    while opçao not in "SN":
        opçao = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if opçao == "N":
        break  


print(f"\nA {cont18} maiores de 18 anos.")
print(f"A {contM} homens cadastrados.")
print(f"A {contF} mulheres menores de 20 anos.")
print("FIM DO PROGRAMA")