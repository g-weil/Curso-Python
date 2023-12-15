# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações
# geradas pelas funções que já temos no módulo criado até aqui.

from utilidades import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 50, 10)