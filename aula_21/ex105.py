def notas(*num, sit=False):
    soma = media = 0
    alunos = dict()
   
    alunos['total'] = len(num)
    alunos['maior'] = max(num)
    alunos['menor'] = min(num)

    for n in num:
        soma += n
    alunos["média"] = soma/alunos['total']

    if sit:
        if alunos['média'] >= 7.0:
            alunos['situação'] = "BOA"
        elif 6 <= alunos['média'] <= 6.9 :
            alunos['situação'] = "RAZOÁVEL" 
        else:
            alunos['situação'] = "RUIM"
    return alunos


#   Programa principal
resp = notas(4.5, 6.2, 5, 6.7, sit=True)
print(resp)