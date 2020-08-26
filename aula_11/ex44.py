#   CAIXA ELETRÔNICO

valor = float(input("Valor produto:R$ "))

print('''\nESCOLHA UMA DAS FORMAS DE PAGAMENTO:
[0] À vista/cheque: 0.1 de desconto 
[1] À vista no cartão: 0.05 de desconto
[2] Em até 2x no cartão: preço normal
[3] 3x ou mais no cartão: 0.20 de juros''')

escolha = int(input("\nSua opção de pagamento: "))

if escolha == 0:
    desconto = valor - (valor * 0.10)
    print("O valor a ser pago com desconto será de R$ {}".format(desconto))
    
elif escolha == 1:
    desconto = valor - (valor * 0.05)
    print("O valor a ser pago com desconto será de R$ {}".format(desconto))

elif escolha == 2:
    parcela = valor / 2
    print("Você pagará em 2x parcelas de R$ {}".format(parcela))

elif escolha == 3:
    parcelas = int(input("Quantas parcelas? "))
    juros = valor + (valor * 0.20)
    preço = juros / parcelas 
    print("Você pagará {}x parcelas de R$ {}".format(parcelas, preço))

