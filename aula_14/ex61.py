#   10 TERMOS DE UMA PA
print("\n   GERADOR DE PA  ")
print('-='*10)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

cont = 1

while cont <= 10:
    print("{}".format(primeiro), end=' ')
    primeiro += razao
    cont += 1
print("FIM")
