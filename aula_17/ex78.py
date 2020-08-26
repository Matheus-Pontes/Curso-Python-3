#   COLOCAR 5 NÚMEROS NUMA LISTA VAZIA
#   DEPOIS DIZER QUAL MAIOR E MENOR
num = []

maior = menor = 0

for c in range(0, 5):

    num.append(int(input(f"Digite um número na posição {c}:")))

    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]

print(f"O maior valor é {maior} na posição ", end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...')

print(f"O menor valor é {menor} na posição ", end="")
for i, v in enumerate(num):
    if v == menor:
        print(f"{i}...")