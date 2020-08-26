#   VERIFICANDO QUANDO APARECE Á LETRA 'A'

nome = str(input("Digite seu nome: ")).strip().upper()

#   Quantidade de vezes
print("A letra A aparece {} vezes.".format(nome.count("A"))) # count = contar 

#   posição 
print("A letra A aparece na posição {}.".format(nome.find("A"))) # procura e informa a primeira posição

#   ultima posição
print("A letra A aparece na ultima posição {}".format(nome.rfind("A"))) # procura e informa a ultima posição





