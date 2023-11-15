# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gols ')

# programa principal:
nome = str(input('Qual o nome do jogador: ')).strip()
gols = str(input('Numero de gols: '))

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if nome in '':
    nome = '<desconhecido>'

else:
    nome = str(nome)

ficha(nome,gols)
