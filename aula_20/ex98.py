#   fazer um contador usando função()
#   encrementando e decrementando autómatico
#   e lendo pelo teclado
from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print("="*30)
    print(f"A contagem inica em {inicio} finaliza em {fim} indo de {passo}")
   
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.25)
            cont += passo
        print("FIM")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.25)
            cont -= passo
        print("FIM")


contador(1, 10, 1)
print()
contador(10, 1, 2)
print()
print("-="*30)

print("Agora personalize: ")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)