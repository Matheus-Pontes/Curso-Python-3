#   fatorial(n, sow=False)
#   se for true mostrar processo de calculo 
#   se n so o resultado

def fatorial(num, show=False):
    f= 1
    for c in range(num, 0, -1):
        if show:
            print(f"{c} ", end="")
            print("x " if c > 1 else "= ",end="")
        f *= c
    return f

        
def titulo(txt):
    print(f"="*(len(txt)+4))
    print(f"  {txt}")    
    print("="*(len(txt)+4))



#   Programa Principal
from time import sleep
titulo("Cálculo de Fatorial")
n = int(input("Qual número deseja ver o fatorial? "))
resp = str(input("Deseja ver o cálculo ou o resutado? [S para cálculo/N para resultado] ")).upper().strip()[0]


if resp == 'S':
    print("Calculando...")
    sleep(1)
    print(fatorial(n, True))
else:
    print("Imprimindo resultado...")
    sleep(1)
    print(fatorial(n))
    

