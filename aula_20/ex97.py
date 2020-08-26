#   Usando função escreva()
#   para o tamanho da palavra escrita
#   te ja um detalhe com tamanho semelhante


def escreva(txt):
    print("="*(len(txt)+4))
    print(f"  {txt}")
    print("="*(len(txt)+4))

escreva("MATHEUS")
escreva("Curso em Video")
escreva("Python")