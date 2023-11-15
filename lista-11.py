# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, nota1, nota2, media])
    resp = str(input('Quer continuar? S/N ')).strip().upper()
    if resp == 'N':
        break

for c, v in enumerate(ficha):
    print(f'{c}: Nome: {v[0]} ----- Media: {v[3]}')

while True:
    nro = int(input('Mostrar notas de qual aluno? (999 finaliza) '))
    if nro == 999:
        break
    if nro < len(ficha):
        print(f'As notas de {ficha[nro][0]} são {ficha[nro][1]} e {ficha[nro][2]}')


