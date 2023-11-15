# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}

print('Valores sorteados: ')
for j, n in jogo.items():
    print(f'{j} tirou o numero {n}')
    sleep(0.5)

ranking = dict()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores: ')
for l, j in enumerate(ranking):
    print(f'{l+1}ºlugar: {j[0]} com {j[1]}')



