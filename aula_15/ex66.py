#   usando do while usando break


num = cont = soma = 0

while  True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    soma += num
    cont += 1

print(f"A soma entre os {cont} vale {soma}.")
