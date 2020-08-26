def leiaint():
    while True:
        n = str(input("Digite um número: "))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print("[ERRO] DIGITE APENAS NÚMERO INTEIRO")
    return n

resp = leiaint()
print(f"Você digitou o número {resp}")



