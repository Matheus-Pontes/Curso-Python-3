# CALCULANDO ALUGUEL DO CARRO

dia = int(input("Dias de viagem: "))
km = float(input("Quilometragem da viagem: "))
cdia = dia * 60
pkm = km * 0.15
s = cdia + km
print("O aluguel será {}".format(s))