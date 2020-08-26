#   DETECTOR DE PALÍNDROMO
#   DESCONSIDERANDO ESPAÇO E ACENTOS
print("="*30)
print("     DETECTOR DE PALÍNDROMO     ")
print("="*30)


frase = str(input("Digite uma frase: ")).strip().upper() #sem espaços
palavras = frase.split() #sepera transformando em um vetor

junto = ''.join(palavras) # juntar as palavras que tiverem espaços

inverso  = ''   #PARA CONSESUIR INVERTER A frase 

for c in range(len(junto)-1, -1, -1): #len para contar
    inverso += junto[c]
print("O inverso de {} é {}".format(junto, inverso))

if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase não é um palíndromo.")



