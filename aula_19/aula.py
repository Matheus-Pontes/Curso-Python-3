#   ESTRUTURA COMPOSTA DICONÁRIOS



dados = {"nome": "Pedro",
         "idade": 25, 
         "sexo": "M"}

dados["peso"] = float(input("Seu peso: "))

print(dados.values()) # TODOS OS VALORES DO DICIONÁRIOS
print(dados.keys())   # TODOS OS ÍNDICIES NOME IDADE E SEXO
print(dados.items())   # MOSTRA TUDO


for k, v in  dados.items():
    print(f"O {k} é {v}")

print("="*30)

locadora = list()
filmes = dict()

filmes["titulo"] = str(input("Noem do filme: ")).upper()
filmes["ano"] = int(input("Ano de lançamento: "))

locadora.append(filmes)

for l in locadora[0]["titulo"]:
    print(f'{l}', end='')


estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end='')
    print()
