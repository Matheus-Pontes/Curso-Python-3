#   ler 4 valores pelo teclado
#   dizer quantas vezes apareceu 9
#   posição que foi digitada o valor 3
#   quais foram os números pares

#valor1 = int(input("Digite um número: "))
#valor2 = int(input("Digite outro número: "))
#valor3 = int(input("Digte mais um número: "))
#valor4 = int(input("Digite outro número: "))

#valores = (valor1, valor2, valor3, valor4)

#print("\nNúmeros digitados: ", end="")
#for v in valores:
 #   print(f"{v} ", end="")

#print(f"\nO número 9 pareceu {valores.count(9)}")
#print(f"O número 3 apareceu na posição {valores.index(3)}")

#for v in valores: 
#    if v % 2 == 0:
#        print(f"Digitou {v} eram pares")
#    else:
#        print("Você digitou nenhum valor par")


#   COM MACETE

num = (int(input("Digite um valor: ")),
       int(input("Digite outro valor: ")),
       int(input("Digite mais um valor: ")),
       int(input("Digite o último valor: ")))

print("Você digitou os valores: ", end=" ")
for n in num:
    print(f"{n} ",end=" ")

print(f"\nO valor 9 apareceu {num.count(9)} vezes")

if  3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}º posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")

print("Os valores pares digitados foram ", end="")
for n in num:
    if  n % 2 == 0:
        print(n, end=' ')




