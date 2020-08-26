#   FUNÇÕES 101, 102, 103, 104, 105, 106
#   escopo de variáveis
#   retorno de resultados

#   Interactive Help help()
#   docstrings
#help(print)
#print(input.__doc__) 

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: Sem retorno
    """
    c = i
    while c<= f:
        print(f'{c}', end=" ")
        c += p
    print("FIM!")

#help(contador)

#   argumentos opcionais
#   a=0, b=0, c=0 
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'valor da soma {s}')

#somar(1, 2, 3)
#somar(1, 1)

#   Escopo de variáveis

def teste(b):
    global a
    a = 8
    b += 4                  # a, b e c são variáveis locais
    c = 2                   
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")    


a = 5                       # Variável global com o comando local global
#teste(a)                    # de dentro da função a que era 5 passa a ser 
#print(f"A fora vale {a}")


#   Retorno de valor
from random import randint
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s   

resp = somar(randint(0, 10), randint(0, 10), randint(0, 10))
resp2 = somar(10, 4)
#print(f"Meus cálculos deram {resp} e {resp2}")


def fatorial(num = 1):
    f = 1
    for c in range(num, 0,  -1):
        f*=c
    return f

n = int(input("Digite um número: "))
print(f"O fatorial de {n} é igual a {fatorial(n)}")

f1= fatorial(5)
f2= fatorial(4)
f3= fatorial()

print(f"O fatorial dos numeros vale {f1}, {f2} e {f3}")

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um valor: "))
if par(num):
    print("É PAR")
else:
    print("NÃO É PAR")







