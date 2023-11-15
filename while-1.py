# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

cont = 0
while True:
    n = randint(1,9)
    escolha = str(input('voce quer ser par ou impar? [p/i] '))
    n2 = int(input('escolha um numero de 1 a 9: '))
    total = n + n2

    if escolha == 'p':
        if total % 2 == 0:
            cont = cont + 1
            print('voce acertou, voce jogou {} e o computador jogou {}, o total foi {}, jogue novamente! '.format(n2,n,total))
        else:
            print('voce perdeu :(, voce jogou {} e o computador jogou {}, o total foi {} '.format(n2,n,total))
            break

    if escolha == 'i':
        if total % 2 != 0:
            cont = cont + 1
            print('voce acertou, voce jogou {} e o computador jogou {}, o total foi {}, jogue novamente! '.format(n2,n,total))
        else:
            print('voce perdeu, voce jogou {} e o computador jogou {}, o total foi {} '.format(n2,n,total))
            break

print('voce ganhou {} vez(es)'.format(cont))