#   COMPARANDO NÚMEROS

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))

print("-=" * 10)

if num1 > num2:
    print("Primeiro valor MAIOR.")
elif num2 > num1: 
    print("Segundo valor MAIOR.")
else:
    print("Os dois valores são iguais.")