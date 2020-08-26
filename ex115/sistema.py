from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar novas pessoas", "Sair do sistema"])

    if resposta == 1:
        #   Listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #   Cadastrar nova pessoa
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Tenha um bom dia")
        break
    else:
        print("\033[31m[ERROR] Digite uma opção válida!\033[m")
