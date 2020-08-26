# Dissecando uma variavel

x = input("Digite algo: ")

#Devolve em [true] or [false]

print("O tipo primitivo é", type(x)) #tipo da variavel
print("Só tem espaço?", x.isspace()) #Se tem só espaço
print("É um número?", x.isnumeric()) #Se é um número
print("É alfabético?", x.isalpha()) #Se é alfabético
print("É alfanumérico?", x.isalnum()) #Se é número
print("Está maiusculo?", x.isupper()) #Se é maiusculo
print("Está minusculo?", x.islower()) #Se é minusculos