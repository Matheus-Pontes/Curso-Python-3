#   Melhorando O ex93 
#   Cadastrando varios jogadores
jogadores = []
jogador = dict()
gols = []
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome: ")).upper()
    quant = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
    gols.clear()
    for c in range(0, quant):
        gols.append(int(input(f"Quantos gols na {c+1}º partida? ")))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar [S/N]? ")).upper()[0]
    if resp in "N":
        break
for k in jogador.keys():
    print(f"{k:<15} ", end=" ")
print()
print("="*40)
for k, v in enumerate(jogadores):
    print(f"{k:>3}", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("="*40)
while True:
    busca = int(input("Qual jogador quer conferir os dados? (999 para parar)")) 
    if busca == 999:
        break
    if busca >= len(jogadores):
        print("[ERROR] Tente novamente")
    else:
        print(f"Levantamento do jogador {jogador['nome'][busca]}")
        print("-"*40)
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f" => No {i+1}º jogo fez {g} gols.")
        print("="*40)
print("<<<< VOLTE SEMPRE >>>>")

