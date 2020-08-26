#    MUNDO 3:
#    VARIAVEIS COMPOSTAS(TUPLAS(), LISTAS[] E DICIONÁRIOS{})
#    Aula de Tuplas 

#   TUPLAS SÃO IMUTÁVEIS

lanches = ("hamburguer", "suco", "pizza", "pudim")
print(lanches[0:2]) #   FATIAMENTO DE 0 ATÉ 1 O 2 NÃO CONTA
print(lanches[:2])
print(len(lanches)) #   len(COMPRIMENTO DA TUPLA) 

#   O CONTADOR c VAI SER CRIADO PELO PYTHON
#   O c PASSA A RECEBER A TUPLA LANCHES UM POR UM DE 0 A 4

for comida in lanches:
    print(f"Eu vou comer {comida}")

#   OUTRA MANEIRA

for cont in range(0, len(lanches)):
    print(lanches[cont], end=" ")    #   Quando for o cont = 0 irá mostrar
                                     #   o lanche(0) sendo, hamburguer
    
#   OUTRA MANEIRA

for pos, comi in enumerate(lanches): #  enumerate(tanto os dados e as posições)
    print(f"Eu vou comer {comi} na posição {pos + 1}")

print("Comi pra caramba")

#   ORGANIZANDO A TUPLA

print(sorted(lanches))  #   no caso ordem alfabética

#   Somando tuplas

a = (1, 2, 4, 5)
b = (5, 2, 1, 4)
c = a + b   #   O inverso é diferente
print(c.count(5)) # Contando a quantidade de um elemento na tupla

print(c.index(8)) # Em que posição esta o 8


