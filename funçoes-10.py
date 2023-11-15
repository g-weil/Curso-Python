# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*nota, situ=False):
    r = dict()

    r['Total'] = len(nota)
    r['Maior'] = max(nota)
    r['Menor'] = min(nota)
    media = sum(nota)/len(nota)
    r['Media'] = media

    if situ == True:
        if media < 3.0:
            r["Situação"] = 'PÉSSIMA'

        if 3.0 <= media < 7.0:
            r["Situação"] = 'RUIM'

        if 7.0 <= media < 9:
            r["Situação"] = 'BOA'

        if media >= 9:
            r["Situação"] = 'EXCELENTE'

    return r


# programa principal

resp = notas(8.4, 9.6, 9.3, situ=True)
print(resp)