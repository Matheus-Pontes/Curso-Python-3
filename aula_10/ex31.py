#   CALCULANDO O PREÇO DA VIAGRM

distancia = float(input("Qual a distancia da viagem:"))

if distancia <= 200:
    preço = 0.50*distancia
    print("O preço será de R$ {}".format(preço))
else:
    preço = 0.45 * distancia
    print("O preço será de R$ {}".format(preço))
print("Tenha uma boa viagem !!!")

#   AGORA USANDO IF INLINE

preço_2 = distancia * 0.50 if distancia <= 200 else distancia * 0.45

