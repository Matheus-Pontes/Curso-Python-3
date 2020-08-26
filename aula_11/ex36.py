#   Validação de emprestimo no banco
#   Para comprar uma casa não podendo ultrapassar 30%

valor_casa = float(input("Valor da casa: R$ "))
salário = float(input("Seu salário: R$ "))
anos = int(input("Em quantos anos vai pagar? "))
print("=-"*25)
prestação = valor_casa / (anos * 12)
porcentagem = salário * 0.30

print("A prestação é de R${}".format(prestação))

if prestação <= porcentagem:
     print("Seu empréstimo foi aprovado com sucesso.")
else:
    print("Infelizmente não podemos continuar com o empréstimo.")
    print("Foi SONEGADO.")


