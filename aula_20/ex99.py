#   DIZER QUAL É O MAIOR
from time import sleep
def maior(*valor):
    
    print("Analisando os valores passados...")
    for d in valor:
        for f in d:
            print(f, end=" ", flush=True)
            sleep(0.5)
    print(f"Foram informados {len(d)} valores ao todo.")
    print(f"O maior valor informados foi {max(d)}")

valor = [1, 2, 3, 4]
print("-="*25)
maior(valor)
print("-="*25)
lista = [5, 8, 9 ,7 , 5]
maior(lista)