#   Usando função
#   chamada área()
#   e fazer a área de uma terreno 
#   retangular
def title(txt):
    print("="*52)
    print(f"{txt:^52}")
    print("="*52)


def area():
    a = largura * comprimento
    print(f"A área do terreno {largura}m^2x{comprimento}m^2 vale {a:.2f}m^2")

title("Cálculo de Área do Terreno")
comprimento = float(input("Comprimento em [m]: "))
largura = float(input("Largura em [m]: "))
area()

