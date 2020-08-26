#   Calculando a hipotenusa com módulos
import math
cateto_oposto = float(input("Distância do cateto oposto: "))
cateto_adjacente = float(input("Distância do cateto adjacente: "))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print("A hipotenusa sera {}".format(hipotenusa))
