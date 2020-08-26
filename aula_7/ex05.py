# Calculando antecessor e sucessor

from time import sleep

n1 = float(input("Digite um valor: "))

a = n1 - 1 #antecessor  
s = n1 + 1 #sucessor

print("Calculando o antecessor e sucessor...")
sleep(1)
print("O antecessor vale {} e o sucessor vale {}".format(a, s))
