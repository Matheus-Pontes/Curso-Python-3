#   Gerenciamento de um jogador

jogador = dict()
gols = list()

jogador["nome"] = str(input("Nome do jogador: ")).upper().strip()
quant = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for c in range(0, quant):
    gols.append(int(input(f"Quantos gols na {c+1}º partida? ")))
    jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print("="*30)
print(jogador)
print("="*30)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("="*30)

print(f"O jogador {jogador['nome']} jogou {quant} partidas.")
for p, g in enumerate(gols):
    print(f"    => Na {p+1}º partida, fez {g} gols.")
print(f"Foi um total de {jogador['total']} gols.")


