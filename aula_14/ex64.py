# 

num = 0
cont = 0
total = 0

num = int(input("Digite um numero [999 para parar]: "))

while num != 999:
    
    cont += num
    total += 1
    num = int(input("Digite um numero: "))
    
print("A soma entre os números vale {}".format(cont))
print("Você digitou {} números".format(total))




