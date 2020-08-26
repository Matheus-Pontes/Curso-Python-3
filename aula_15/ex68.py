#   JOGO ÍMPAR OU PAR
import random

vit = 0

print("="*30)
print("   VAMOS JOGAR PAR OU ÍMPAR")

print("="*30)

while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0, 11)
    soma = jogador + computador
    
    opçao = " "
    while opçao not in "PpIi":
        opçao = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total de {soma}")
    
    if opçao == "P":
        if soma % 2 == 0:
            print("Você VENCEU.")
            vit += 1
        else:
            print("Você PERDEU.")
            break
    elif opçao == "I":
        if soma %  2 == 1:
            print("Você VENCEU.")
            vit += 1
        else:
            print("Você PERDEU.")
            break
    
    print("TRY AGAIN ...")
print(f"[GAMER OVER] Você venceu {vit} vezes")   
    
    
    