#   GERADOR DE PA 2.0

primeiro = int(input("Primeiro: "))
razao = int(input("Razao: "))

termo = primeiro
cont = 1
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print("{}".format(termo), end=' ')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais: "))
print("Progressão finalizada com {} termos".format(total))
    
