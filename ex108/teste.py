from ex108 import moeda

p = float(input("Digite um preço: R$ "))
print(f"O dobro de  {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"A metade de  {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"Aumentando em 10%, temos {moeda.moeda(moeda.aumento(p))}")
print(f"Diminuindo em 15%, temos {moeda.moeda(moeda.diminuir(p))}")