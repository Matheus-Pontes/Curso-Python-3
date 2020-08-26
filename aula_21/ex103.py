def ficha(n, g):
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if n.strip() == "":
        n = "<desconhecido>"

    return f"O jogador {n} fez {g} gol(s)."

#   Programa principal
nome = str(input("Nome do jogador: "))
gols = str(input("Quantos gols marcou no campeonato? "))

print(ficha(nome, gols))