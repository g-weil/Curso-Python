# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = list()
dado = list()
cont = menorp = maiorp = 0

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    cont += 1
    if cont == 1:
        maiorp = lista[1]
        menorp = lista[1]
    else:
        if lista[1] >= maiorp:
            maiorp = lista[1]

        elif lista[1] <= menorp:
            menorp = lista[1]

    dado.append(lista[:])
    lista.clear()

    resp = str(input('voce quer continuar? S/N ').lower().strip())
    if resp != 's':
        break


print(f'A) Foram cadastradas {cont} pessoas')
print(f'B) O maior peso foi de {maiorp}, peso de ', end='')
for p in dado:
    if p[1] == maiorp:
        print(f'[{p[0]}] ', end='')
print(f'\nC) O menor peso foi de {menorp}, peso de ', end='')
for p in dado:
    if p[1] == menorp:
        print(f'[{p[0]}] ', end='')