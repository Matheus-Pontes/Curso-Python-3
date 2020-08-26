#   Listas parte II

dados = list()
pessoas = list()

dados.append("Pedro")
dados.append(25)

dados.append("Maria")
dados.append(19)

dados.append("João")
dados.append(32)

pessoas.append(dados)

pessoas = [["Pedro", 25], ["Maria", 19], ["João", 32]]
print(pessoas[0][0])#   Posicinamento na lista


teste = []
teste.append("Gustavo")
teste.append(40)

galera = []
galera.append(teste[:]) # uma cópia 
teste[0]= "Maria"
teste[1]= 22
galera.append(teste[:])
print(galera)

print(f"{'Nomes: ':<10}", end='')
print(f"{'Idades:':>8}")

for p in galera:
    print(f"{p[0]:.<13}",end= "")
    print(f"{p[1]:> 2}")

# Não esquecer de fazer a cópia da

























