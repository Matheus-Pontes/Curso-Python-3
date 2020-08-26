#   VERIFICANDO STRING 

nome = str(input("Digite seu nome: ")).strip() # tirar os espaços

n = nome.split() # armazendao como uma lista 

print("Seu primeiro nome é: {}".format(n[0])) # [0] posição inicial
print("Seu último nome é: {}".format(n[len(n) - 1])) # o len() vai contar a quantidade de posições e -1 para encontrar o ultimo
