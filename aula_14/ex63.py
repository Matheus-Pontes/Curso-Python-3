# SEQUÊNCIA DE FIBONACCI
# 0 -> 1 -> 1 -> 2 -> 3 ...
# t1 - t2 - t3

num = int(input("Aumentar a sequência: "))

t1 = 0
t2 = 1
cont = 3

print("{} -> {}".format(t1, t2), end=" ")

while cont <= num:
    t3 = t1 + t2
    print("-> {}".format(t3), end=" ")
    t1 = t2
    t2 = t3
    cont += 1
print("FIM")