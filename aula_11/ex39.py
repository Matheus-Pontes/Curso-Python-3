#   HORA DE SE ALISTAR?

from datetime import date # buscar ano do sistema

ano_atual = date.today().year # armazenar em uma variavel o ano atual

nascimento = int(input("Ano de nascimento: "))

idade = ano_atual - nascimento

if idade == 18:
    print("Você deve se alistar IMEDIATAMENTE !!!")

elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para você se alistar".format(saldo))
    ano = ano_atual + saldo
    print("Seu alistamento será {}".format(ano))

elif idade > 18:
    saldo = idade - 18
    print("Já passou {} anos para o seu alistamento.".format(saldo))
    ano = ano_atual - saldo
    print("Sendo no ano de {}".format(ano))
