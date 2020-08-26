#   Calculando seno, cosseno e tangente
import math

angulo = int(input("Valor de um angulo: "))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print("Valores\nseno: {} \ncosseno: {} \ntangente: {}".format(seno, cos, tan))
