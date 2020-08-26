# MÉDIA DE DOIS ALUNOS

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2)/2

if media < 5.0:
    print("Sua média foi {}".format(media))
    print("Você foi REPROVADO !!!")

elif media >= 5.0 and media <= 6.9:
    print("Sua média foi {}".format(media))
    print("Você está de RECUPERAÇÃO")
    
elif media >= 7.0:
    print("Sua média foi {}".format(media))
    print("Parabêns, Você foi APROVADO !!!")
