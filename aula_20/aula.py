#   USANDO FUNÇÕES

def linha():
    print("-"*30)

def mensagem(msg):
    print("-"*30)
    print(msg)
    print("-"*30)

#   PROGRAMA PRINCIPAL 
#   E MENSAGEM FUNCIONANDO COMO COMANDO INTERNO
#   print()
#   mensagem(f"{'SISTEMA DE ALUNOS':^30}") 


#   PARTE PRÁTICA


def soma(a, b):
    s = a + b
    print(f"A SOMA VALE {s}")

#a = int(input("Digite um número: "))
#b = int(input("Digite outro número: "))

#soma(a, b)


def media():  
    m = sum(n) / len(n)
    print(f"A média da lista foi {m}")


n = []
for c in range(0, 5):
    n.append(int(input("digite um número: ")))
print(n)
media()



def contador(*num):
    print(num)

#contador(1, 2, 3) # MOSTROU COMO UMA tupla()
#contador(5, 8, 9)

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 5]
dobra(valores)
print(valores)