# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(lar, comp):
    print(f'A área de um terreno {lar}x{comp} é de {lar*comp}m²')

print('CALCULO DE UM TERRENO: ')
print('-'*30)

largura = float(input('Qual a largura do terreno? '))
comprimento = float(input('Qual o comprimento do terreno? '))

area(largura, comprimento)




