#   PA
print('='*30)
print("     10 TERMOS DE UMA PA     ")
print('='*30)

ptermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = ptermo + (7 - 1) * razao

for c in range(ptermo, decimo + razao, razao):
    print("{}".format(c), end=" - ")
print('ACABOU')
