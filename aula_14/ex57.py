# LEIA O SEXO 

sexo = str(input("Informe seu sexo: ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("[ERROR] Informe novamente seu sexo: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))
