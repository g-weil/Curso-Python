# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso

cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

for c in cont:
    c = int(input('digite um numero de 0 a 20: '))

    if 20 >= c >= 0:
        break
    else:
        print('voce digitou um numero maior que 20 ou menor que 0, tente novamente! ')

print(cont[c])
