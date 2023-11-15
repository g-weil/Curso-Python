# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    print(f'Contador de {inicio} ate {fim} de {passo} em {passo}: ')
    sleep(1.5)
    print('-' * 30)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' '), sleep(0.3)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' '), sleep(0.3)
            cont -= passo

    print('FIM! ')
    print('-' * 30)

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de criar o seu contador: ')
primeiro = int(input('Inicio: '))
ultimo = int(input('Fim: '))
intervalo = int(input('Passo: '))

contador(primeiro, ultimo, intervalo)



