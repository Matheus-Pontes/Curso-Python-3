#   VERIFICANDO SALÁRIOS

salario = float(input("Digite o valor do seu salário R$: "))

if salario <= 1250:
    aumento = salario + (salario * 0.15)
    print("Seu salário teve um aumento de 15% passando a ser R$ {}".format(aumento))
else:
     aumento = salario + (salario * 0.10)
     print("Seu salário teve um aumento de 10% passando a ser R$ {}".format(aumento))
