#   CONVERSÃO DE BASE NUMÉRICAS
#   BINÁRIO, OCTAL E HEXADECIMAL

num = int(input("Digite um número inteiro: "))
print('''Escolha a conversão:
[0] BINÁRIO
[1] OCTAL
[2] HEXADECIMAL ''')
option = int(input("Faça sua escolha: "))

if option == 0:
    print("{} em BINÁRIO {}".format(num, bin(num)))
elif option == 1:
    print("{} em OCTAL {}".format(num, oct(num)))
elif option == 2:
    print("{} em HEXADECIMAL {}".format(num, hex(num)))
else:
    print("[ERRROR] TRY AGAIN !!!")