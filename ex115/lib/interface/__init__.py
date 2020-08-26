def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31m[ERROR] digite um valor inteiro valido...\033[m")
            continue
        except KeyboardInterrupt:
            n = 0
            break
        else:
            return n


def linha(tam=42):
    return "=" * tam


def cabeçalho(txt):
    print(linha())
    print(f"{txt:^42}")
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for l in lista:
        print(f"\033[34m{c}\33[m - \033[32m{l}\033[m")
        c += 1
    print(linha())
    opc = leiaint("\033[32mSua opção: \033[m")

    return opc