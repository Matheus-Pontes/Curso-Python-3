#   ANÁLISANDO TRIÂNGULOS
#   A  soma dos dois segmentos tem que ser menor q outro exemplo: a < b+c 
print("=-"*25)
print("Análisando se forma ou não forma triângulo")
print("=-"*25)

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

#   Lógica

if a < b+c and b < a+c and c < b+a:
    print("Os segmento acima podem formar um triêngulo")
else:
    print("Os segemntos acima não podem formar um triângulo")


