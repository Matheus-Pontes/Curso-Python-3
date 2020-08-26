#   SORTEANDO 4 NÚMEROS
from random import randint
from time import sleep
from operator import itemgetter
#   OUTRA FORMA 
ranking = list()
jogadas = dict()
print('='*30)
print(f'{"JOGOS EM UM DADO ":^30}')
print('='*30)

for c in range(1, 5):
    jogadas[f"Jogador_{c}"] = randint(1, 6)
ranking.append(jogadas.copy())

print("=-"*3, f'{"JOGOS DOS JOGADORES"}', "-="*3)
for k, v in jogadas.items():
    print(f"   {k} jogou {v} no dado.")
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print("-="*3, f"{'RANKING DOS JOGADORES'}", "=-"*3)
for i, n in enumerate(ranking):
    print(f"   {i+1}º lugar: {n[0]} jogou {n[1]}")
    sleep(1)



    



