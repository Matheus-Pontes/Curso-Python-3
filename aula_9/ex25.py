# VERIFICANDO SE TEM SILAVA NO NOME

nome = str(input("Digite seu nome completo: ")).upper().strip()

# procura = nome.find('SILVA') # devolve a posição 

print("Seu nome tem SILVA? {}".format("SILVA" in nome))