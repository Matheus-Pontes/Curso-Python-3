from ex109 import moeda

p = float(input("Digite um preço: R$ "))
print(f"O dobro de  {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"A metade de  {moeda.moeda(p)} é {moeda.metade(p, True)}")
print(f"Aumentando em 10%, temos {moeda.aumento(p, True)}")
print(f"Diminuindo em 15%, temos {moeda.diminuir(p, True)}")