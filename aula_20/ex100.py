from random import randint
from time import sleep


def sortear(lista):
    print('Sorteando 5 valores:', end= " ")
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f"{n}", end=" ", flush=True)
        sleep(0.3)

def somapar(lista):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f"Somando os valores pares da {lista}, temos {soma}")         

numeros = []
sortear(numeros)
print()
somapar(numeros)