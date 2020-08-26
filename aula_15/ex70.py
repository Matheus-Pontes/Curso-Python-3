#   Estáticas em produtos
total = totalmil = cont = menor =  0
while True:
    print("="*30)
    print("     Loja dos Devs     ")
    print("="*30)
    produto = str(input("Nome do produto: ")).strip().upper()[0]
    preço = int(input("Valor do produto R$: "))
    
    cont += 1
    total += preço
    
    if preço >= 1000:
        totalmil += 1
    
    # vereificando qual é o menor
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    
    #   Verificando se quer continuar depois de executar acima
    opçao = " "
    while opçao not in "SN":
        opçao = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if opçao == "N":
        break

print("{:=^40}".format("FIM DO PROGRAMA"))
print(f"O total da compra foi R$ {total}.")
print(f"A {totalmil} produtos que custaram mais de R$ 1000.")
print(f"O produto mais barato custa R$ {menor}")
