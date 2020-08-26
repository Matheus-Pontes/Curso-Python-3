# Calculando o dobro, o triplo e a raiz quadrada

from time import sleep

n1 = float(input("Digite um número: "))
d = n1 * 2
t = n1 * 3
r = n1 **(1/2)

print("Calculando raiz quadrada,triplo e o dobro...")
sleep(1)
print("Dobro: {} \nTriplo: {} \nRaiz quadrada: {}".format(d, t, r))
