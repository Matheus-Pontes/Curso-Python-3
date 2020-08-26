#   CÁLCULO DE IMC

massa = float(input("Seu peso: "))
altura = float(input("Sua altura: "))

imc = massa / (altura ** 2)
print("Seu imc é {:.1f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print("Você está com peso ideal.")
elif imc > 25 and imc <= 30:
    print("Você está com sobrepeso.")
elif imc > 30 and imc <= 40:
    print("Você está com obesidade.")
else:
    print("Você está com obesidade mórbida.")
    
