# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando
# se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from utilidades import moeda

valor = float(input('Digite um preço: R$'))
desc = int(input('Quantos % quer aumentar/diminuir? '))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'O valor de {moeda.moeda(valor)} com um acréscimo de {desc}% fica {moeda.aumentar(valor, desc, True)}')
print(f'O valor de {moeda.moeda(valor)} com um desconto de {desc}% fica {moeda.diminuir(valor, desc, True)}')
