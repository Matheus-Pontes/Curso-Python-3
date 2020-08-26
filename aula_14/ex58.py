# JOGO DA ADIVINHAÇÃO

from random import randint


print("\nVou pensar em um número de 0 a 10 tente adivinhar.")
computador = randint(0, 10)

jogador = int(input("Faça sua jogada: "))

palpite = 0
acertou  = False

while jogador != computador:
    jogador = int(input("Tente novamente: "))
    palpite += 1

    if jogador == computador:
        acertou == True
    else:
        if jogador < computador:
            print("Mais... , Tente mais uma vez")
        elif jogador > computador:
            print("Menos... , Tente mais uma vez")

print("Você preciou de {} chutes para acertar".format(palpite))

