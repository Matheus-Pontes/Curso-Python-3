#   INTERROMPENDO REPETIÇÕES COM WHILE
#   QUASE UM DO WHILE
#   USANDO O BREAK

n = s = 0 

while True:    
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    s += n 

print(s)
print(f"A soma vale {s}") # fstring


nome ='Jose' 
idade = 33

print(f"O {nome} tem {idade} anos.")

nome = "jose"
idade = 33
salario = 956.33
#   (^) para centralizar um string em um determinado espaço

print(f"O {nome:^20} tem {idade} anos e ganha R$ {salario}")






