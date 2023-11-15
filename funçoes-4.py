# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*valores):
    maior = cont = 0
    print('-' * 30)
    print(f'Analisando os valores passados: ')
    sleep(1)
    for valor in valores:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados {len(valores)} valores ao todo')
    sleep(0.5)
    print(f'O maior valor é {maior}')
    sleep(0.5)
    print('-' * 30)


maior(7, 5, 4, 3, 1)
maior(3, 5, 2)
maior(2, 5, 5, 4)
maior(3, 3, 6)
maior()