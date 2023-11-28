#  Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#  Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

valor = float(input('Digite um preço: R$'))
desc = int(input('Quantos % quer aumentar/diminuir? '))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'O valor de {moeda.moeda(valor)} com um acréscimo de {desc}% fica {moeda.moeda(moeda.aumentar(valor, desc))}')
print(f'O valor de {moeda.moeda(valor)} com um desconto de {desc}% fica {moeda.moeda(moeda.diminuir(valor, desc))}')

