#  CADASTRO NOME E IDADE E SITUAÇÃO

aluno = dict()

aluno['nome'] = str(input("Nome: ")).upper()
aluno['média'] = float(input("Média: "))

if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 >= aluno['média'] <= 6.9:
    aluno["situação"] = "RECUPERAÇÃO"
else:
    aluno["situação"] = "REPROVADO"

print("="*20)
for k, v in aluno.items():
    print(f"{k} é igual {v}")



