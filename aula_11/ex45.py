#   JO-KEN-PO

from random import randint
from time import sleep

opçoes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''\nFAÇA SUA ESCOLHA:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual sua jogada? "))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print("PO")
sleep(1)

print("-="*15)

print("Computador  jogou {} ".format(opçoes[computador]))
print("Jogador jogou {}".format(opçoes[jogador]))

print("-="*15)

if computador == 0:
    if jogador == 0:
        print("EMPATE.")
    elif jogador == 1:
        print("JOGADOR VENCEU.")
    elif jogador == 2:
        print("COMPUTADOR VENCEU")

elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCEU")

elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCEU")
    elif jogador == 1:
        print("COMPUTADOR VENCEU")
    elif jogador == 2:
        print("EMPATE.")