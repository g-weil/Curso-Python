# Aprimore o exercicio 4 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome: '))
    jogos = int(input('Quantidade de partidas jogadas: '))
    partidas.clear()

    for c in range(0, jogos):
        partidas.append(int(input(f'Quantos gols marcados na {c+1}ª partida? ')))

    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    resp = str(input('Quer continuar? S/N ')).upper().strip()
    if resp == 'N':
        break

print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Digite o código do jogador que quer visualizar os dados: (999 interrompe) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o codigo {busca}')
    else:
        print(f'Dados do jogador {time[busca]["Nome"]}: ')
        for p, g in enumerate(time[busca]['Gols']):
            print(f'    Na {p+1}ª partida, o jogador {time[busca]["Nome"]} tem {g} gols ')

        print(f'    {time[busca]["Nome"]} tem {jogador["Total"]} gols no total ')



