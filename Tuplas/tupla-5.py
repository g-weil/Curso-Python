#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
#na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = 'lapis', 1.75, 'borracha', 2, 'caneta', 3

print('tabela de preços: ')

for p in range(0, len(lista)):
    if p % 2 == 0:
        print(f'{lista[p]:.<20}', end='')

    else:
        print(f'R${lista[p]:>7.2f}')
