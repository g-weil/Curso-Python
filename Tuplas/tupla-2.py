# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time do Corinthians.

brasileirao = ('botafogo', 'palmeiras', 'gremio', 'flamengo', 'fluminense', 'bragantino', 'atltetico-pr', 'fortaleza', 'atletico-mg', 'cuiaba', 'sao paulo', 'cruzeiro',
               'corinthians', 'internacional', 'goias', 'bahia', 'santos', 'vasco da gama', 'coritiba', 'america-mg')

print('os 5 primeiros times sao: ')
print(brasileirao[:5])
print('na zona de rebaixamento estao: ')
print(brasileirao[16:])
print('em ordem alfabetica: ')
print(sorted(brasileirao))
print('o Corinthians esta na posiçao: ')
print(brasileirao.index('corinthians')+1)





