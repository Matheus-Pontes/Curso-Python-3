#   Sorteando uma ordem de apresentação
#   alunos

import random
from time import sleep

aluno_1 = input("nome:")
aluno_2 =input("nome:")
aluno_3 = input("nome:")
aluno_4 = input("nome:")

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

print("Sorteando...")
sleep(1)

random.shuffle(lista)
print(lista)