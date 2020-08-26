#   PARTE I
#   UTILIZANDO LISTAS []
#   LISTAS SÃO MUTÁVEIS

lanches = ["hamburguer", "suco", "pizza", "pudim"]

lanches[3] = "sorvete"

print(lanches)

# Comandos para adição de itens

lanches.append("pudim") #  para a última posição
lanches.insert(1, "fritas") #  Escolho uma posição

print(lanches)

#   Apagando elementos

del lanches[3]
lanches.pop()   # Normalmente usa-se para apagar o último elemento
                # mas, pode colocar um parâmetro
lanches.remove("sorvete")

print(lanches)
print(f"A lista tem {len(lanches) + 1} elementos")


#  Utilizando range e a função list para criar uma lista
import random
valor = list(range(1, 10))

valores = [random.randint(0, 10),random.randint(0, 10), random.randint(0, 10) ]

for c in valores:
    print(f"{c} ")

#   Arrumando listas

velocidades = [80, 20, 50, 40, 90, 30]
velocidades.sort(reverse= True)
print(velocidades)

print("="*30)

valores = []
valores.append(9)
valores.append(4)
valores.append(5)

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei os valores {v}")

c=0
for v in range (0, len(valores)):
    print(f"Na posição {c} encontrei os valores {valores[v]}")
    c+=1

valores = list()
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

print(valores.sort(), end="")

print("\nCheguei ao final da lista")