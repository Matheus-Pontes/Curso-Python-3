#   MAIOR E MENOR E MÉDIA

opçao = 'S'
soma = cont = media = maior = menor = 0

while opçao != 'N':    
    num = int(input("Digite um número: "))
    opçao = str(input("Deseja continuar? [S/N]: ")).strip()[0].upper()
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor: 
            menor = num

media = soma / cont

print("Você digitou {} números e média entre eles vale {:.2f}".format(cont, media))
print("O maior foi {} e menor foi {}".format(maior, menor))
