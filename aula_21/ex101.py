#   criar um programa com função votar
#   e verificar se pelo ano de nascimento
#   o voto é opcional,negado e obrigatório

# obrigatorio =  18 e 70 anos.
# opcional = entre 16 e 17 anos, pessoas com mais de 70 anos e analfabetos, o voto é facultativo.
# negado = >= 80 anos
from datetime import datetime

def votar():
    print(f"Com {idade} anos: ", end="")
    if idade >= 18 and idade <= 70:
        resp = print("Voto Obriatório")
    elif idade >= 16 and idade <= 17 :
        resp = print("Voto Opcional")
    elif idade >= 80:
        resp = print("Voto Negado")
    return resp


print("="*30)
nasc = int(input("Em que ano você nasceu? "))
idade = datetime.now().year - nasc

votar()
