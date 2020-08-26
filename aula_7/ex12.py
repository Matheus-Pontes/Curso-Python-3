# Calculando Desconto(5%)

preco = float(input("Valor do produto: "))

desconto = preco - (preco * 0.05)

print("Novo valor com desconto:R${:.1f}".format(desconto))