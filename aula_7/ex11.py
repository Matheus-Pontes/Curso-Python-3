# QUANTIDADE DE TINTA EMUMA DETERMINADA PAREDE

largura  = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area_da_parede = largura * altura

tinta_em_litros = area_da_parede * 2

print("A quantidade de tinta em litros será: {:.1f}L".format(tinta_em_litros))