from ex107 import moeda

p = float(input("Digite um preço: R$ "))
print(f"O dobro de R$ {p} é R$ {moeda.dobro(p)}")
print(f"A metade de R$ {p} é R$ {moeda.metade(p)}")
print(f"Aumentando em 10%, temos R$ {moeda.aumento(p)}")
print(f"Diminuindo em 15%, temos R$ {moeda.diminuir(p)}")