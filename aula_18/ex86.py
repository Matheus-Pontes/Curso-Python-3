#   CRIANDO UMA MATRIZ 3x3
#   fazendo uso de dois laços

matriz = [[0, 0, 0], [0, 0, 0], [0, 0 ,0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input("Digite um valor: "))

print("="*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()# QUEBRA DE LINHA
