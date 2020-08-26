#   usando uma tupla 
#   fazer a tabulção exemplo
#   lapis..............R$ 1,75
#   borracha...........R$ 2.00

produtos = ("Lápis", 1.75 ,
"Borracha", 2,
"Caderno", 15.90,
"Estojo", 25,
"Transferidor", 4.20,
"Compasso", 9.99,
"Mochila", 120.30,
"Canetas", 22.30, 
"Livro", 34.90,)

print("-"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-"*40)

#UTILIZANDO O len() para colocar uma contagem
# e depois utilizando o resto da divisão saber qual era o número
# par ou ímpar dependendo resultado ele printa

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<30}", end =" ") # Comando alinhado a esquerda {:.<30}
    else:
        print(f"R$ {produtos[pos]:>6.2f}")   
print("-"*40)


