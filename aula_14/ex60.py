#   CALCULANDO FATORIAL
from math import factorial

n = int(input("Digite um número paracalcular seu fatorial: "))

f = 1
c = n

while c > 0:
    print("{}".format(c), end=' ') 
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c 
    c -= 1
print("O fatorial {} vale {}".format(n, f))

n1 = int(input("Digite um valor para calcular seu fatorial: "))
fact = factorial(n1)
print("O fatorial de {} é {}".format(n1, fact))
