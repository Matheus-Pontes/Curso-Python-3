#   JOGO DA ADIVINHA

from random import randint
from time import sleep

computador = randint(0,5)
print("Vou pensar num número de 0 a 5 tente adivinhar...")

player = int(input("Tente adivinhar: "))
print("IN PROCESS ... ")
sleep(2)

#   Condição
if player == computador :
    print("Parabêns você acertou!!!")
else:
    print("Ganhei você pensou no {} e eu no {}".format(player, computador))