# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()

jogador['Nome'] = str(input('Nome: '))
jogos = int(input('Quantidade de partidas jogadas: '))

for c in range(0, jogos):
    partidas.append(int(input(f'Quantos gols marcados na {c+1}ª partida? ')))

jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print(f'O jogador {jogador["Nome"]} jogou {jogos} partidas')

for p, n in enumerate(jogador['Gols']):
    print(f'Na {p+1}ª partida, o jogador {jogador["Nome"]} marcou {n} gols')

print(f'{jogador["Nome"]} marcou {jogador["Total"]} gols no total ')
