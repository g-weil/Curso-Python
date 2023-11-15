# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dados = dict()

dados['Nome'] = str(input('Qual o nome do aluno? '))
dados['Media'] = float(input('Qual a media desse aluno? '))

if dados['Media'] >= 7.0:
    dados['Situação'] = 'APROVADO'

elif 3.0 <= dados['Media'] < 7.0:
    dados['Situação'] = 'RECUPERAÇÃO'

else:
    dados['Situação'] = 'REPROVADO'

for c, d in dados.items():
    print(f'{c} = {d} ')
