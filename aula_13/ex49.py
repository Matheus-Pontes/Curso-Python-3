#   tabuada utilizando o for
n = int(input("TABUADA DO: "))

for c in range(0, 11):
    mul = n * c
    print("{} x {} = {}".format(c, n, mul))