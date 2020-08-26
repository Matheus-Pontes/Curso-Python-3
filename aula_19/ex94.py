pessoa = dict()
galera = list()
soma = media = 0

while True:

    pessoa.clear()
    pessoa["nome"] = str(input("Nome: ")).upper().strip()
    while True:
        pessoa["sexo"] = str(input("Sexo[M/F]: ")).upper()[0]
        if pessoa["sexo"] in "MF":
            break
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    
    res = " "
    while res not in 'SN':
        res = str(input("Quer continuar [S/N]? ")).upper()[0]
    if res in "N":
        break
print("="*40)
print(F"{'ANÁLISE DOS CADASTROS':^40}")
print("="*40)

print(f"A) O grupo tem {len(galera)} pessoas.")
media = soma/len(galera)
print(f"B) A média de idade do grupo é {media:.2f}")

print("C) As mulheres cadastradas foram: ", end=" ")
for p in galera:
    if p["sexo"] == "F":
        print(f"{p['nome']}", end=" ")
print()
print("D) As pessoas com a idade maior que a média: ")
for p in galera:
    if p["idade"] >= media:
        for k, v in p.items():
            print(f"\n=> {k} = {v};", end=" ")
        print()
print("<<<<<< SESSÃO ENCERRADA >>>>>>")

