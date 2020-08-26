def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def aumento(n=0):
    a = n + (n * 0.1)
    return a


def diminuir(n=0):
    d = n - (n * 0.15)
    return d


def moeda(n=0, moeda="R$"):
    return f"{moeda}{n:.2f}".replace(".", ",")
