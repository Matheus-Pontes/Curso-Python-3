#   Pegar a tabela do brasileirão e
#   mostrar os 5 primeiros times # fatiamento
#   os 4 últimos
#   em ordem alfabética # função sorted()
#   Posição da chapecoense # função index(chapecoense)
print("="*30)
print("{:^30}".format("BRASILEIRÃO 2019"))
print("="*30)

times = ("Flamengo", "Santos", "Palmeiras", "Grêmio", "Athletica-PR", "São Paulo", "Internacional", "Corinthians", "Fortaleza", "Goiás", "Bahia", "Vasco da Gama", "Atlético-MG", "Fluminense", "Botafogo", "Ceará SC", "Cruzeiro", "CSA", "Chapecoense", "Avaí")

for pos, t in enumerate(times):
    print(f"{pos + 1}º {t}")

print("\nOs 5 primeiros colocados")

for pos, t in enumerate(times[0:5]):
    print(f"{pos + 1}º {t}")

print("\nOs 4 últimos colocados")
for pos, t in enumerate(times[-4:]):
    print(f"{pos + 1}º {t}")

print(f"\nEm ordem... {sorted(times)}")

print(f"\nPosição da chapecoense é {times.index('Chapecoense')+1}")


