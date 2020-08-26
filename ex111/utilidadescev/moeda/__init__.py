def dobro(n=0, formato=False):
    res = n*2
    return res if formato is False else moeda(res)


def metade(n=0, formato=False):
    res = n/2
    return res if formato is False else moeda(res)


def aumento(n=0, formato=False):
    res = n + (n * 0.1)
    return res if formato is False else moeda(res)


def diminuir(n=0, formato=False):
    res = n - (n * 0.15)
    return res if formato is False else moeda(res)


def moeda(n=0, moeda="R$"):
    return f"{moeda} {n:.2f}".replace(".", ",")


def resumo(n=0, taxaa=10, taxar=5):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Preço analisado: \t{moeda(n)}")
    print(f"Dobro do preço:  \t{dobro(n, True)}")
    print(f"Metade do preço: \t{metade(n, True)}")
    print(f"10% de aumento: \t{aumento(n, True)}")
    print(f"15% de redução: \t{diminuir(n, True)}")
    print("-"*30)
