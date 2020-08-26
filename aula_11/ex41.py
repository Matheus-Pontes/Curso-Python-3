#   NATAÇÃO: CATEGORIA DE ACORDO COM A IDADE

idade = int(input("Sua idade por favor: "))

if idade  <= 9:
    print("Nadador MIRIM")
elif idade > 9 and idade <= 14:
    print("Nadador INFANTIL")
elif idade > 14 and idade <= 19:
    print("Nadador JUNIOR")
elif idade == 20:
    print("Nadador SÊNIOR")
else:
    print("Nadador MASTER")
