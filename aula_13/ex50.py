#   SOMA DE NÚMEROS INTEIROS
soma = 0

for c in range(1, 7):
    n = int(input("digite um valor: "))
    if n % 2 == 0:
        soma += n
print("A soma vale {}".format(soma))