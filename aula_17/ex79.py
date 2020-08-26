#   Digitar varios valores e se for duplicado n adicionar

num = []

while True:
    n = int(input("Digite um valor: "))
    
    # Adicionando o valor e caso seja igual não adiciona
    if n not in num:
        num.append(n)
        print("Valor adicionado na lista...")
    else:
        print("Valor duplicado! Não vou adicionar")
        
    opçao = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    if opçao == "N":
        break    

num.sort()
print("Você digitou os valores", end='')
print(num)