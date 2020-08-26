#   Sorteando um nome numa lista

import random

nome_1 = str( input("nome:"))
nome_2 = str (input("nome:"))
nome_3 = str (input("nome:"))
nome_4 = str (input("nome:"))

lista = [nome_1, nome_2, nome_3, nome_4]

escolhido = random.choice(lista) #escolha aleatória

print("O aluno escolhido foi {}".format(escolhido.upper())) # Deixando em maiusculo
