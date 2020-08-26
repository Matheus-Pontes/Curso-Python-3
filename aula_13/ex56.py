#   NOME, SEXO E IDADE

somaidade = 0
media = 0 
maioridadehomem = 0
nomevelho = ''
totmulher = 0

for c in range(1, 5):

    print("----- {}ª PESSOA -----".format(c))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()

    somaidade += idade

    if c == 1 and sexo in "Mm":
        maioridade = idade
        nomevelho = nome 

    if sexo in 'Mm' and idade  > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in'Ff' and idade > 20:
        totmulher += 1

media = somaidade / 4
print("A média de idade do grupo é de {} anos".format(media))

print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))

print("A {} mulheres menores de 20 anos.".format(totmulher))