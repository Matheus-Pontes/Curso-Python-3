#   RADAR ELETRÔNICO

velocidade = float(input("Informe sua velocidade: "))
print("Sua velocidade é {} km/h.".format(velocidade))

if velocidade >= 80:
    multa = 7*(velocidade - 80)
    print("[Alert]Você ultrapassou o limite de velocidade de 80 km/h.")
    print('O valor da multa é R$ {}'.format(multa))
else:
    print("Dirija com cuidado.Tenha um bom dia.")
    

