#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('qual o valor a ser sacado? '))
total = valor

ced1 = 50
ced2 = 20
ced3 = 10
ced4 = 1
cont1 = cont2 = cont3 = cont4 = 0

while total > 0:
    if total >= ced1:
        total = total - ced1
        cont1 += 1

    if total < ced1 and total >= ced2:
        total = total - ced2
        cont2 += 1

    if total < ced2 and total >= ced3:
        total = total - ced3
        cont3 += 1

    if total < ced3 and total >= ced4:
        total = total - ced4
        cont4 += 1


print('Serão entregues {} notas de R$50, {} notas de R$20, {} notas de R$10 e {} notas de R$1 '.format(cont1, cont2, cont3, cont4))


