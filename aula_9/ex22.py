#   Manipulando STRING

nome = str(input("Digite seu nome completo: ")).strip()

# MAIUSCULO E MINUSCULO

print("Seu nome em maiúsculo {}".format(nome.upper()))
print("Seu nome em minúsculo {}".format(nome.lower()))

# CONTAGEM 

print("Seu nome tem {} letras".format(len(nome) - nome.count(" ")))
#print("Seu primeiro nome tem {} letras ".format(nome.find(" ")))
separa = nome.split()
print("Seu primeiro nome tem {} letras".format(len(separa[0])))
