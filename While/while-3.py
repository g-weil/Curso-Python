#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

n = 'S'
barato = ''
contp = contp2 = menor = cont = 0

while n == 'S':
    nome = str(input("digite o nome do produto: "))
    preco = float(input("digite o preço do produto escolhido: "))
    contp = preco + contp
    cont += 1

    if preco > 1000:
        contp2 = contp2 + 1

    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome

    n = str(input("quer cadastrar mais alguma pessoa? [S/N] ")).upper()

    if n == 'N':
        break
    if n != 'N' and n != 'S':
        n = str(input('resposta invalida! voce deve responder [S] ou [N]: ')).upper()

print('A) O valor total gasto na compra é R${} reais  '.format(contp))
print('B) {} produtos custaram mais de R$1.000,00 reais  '.format(contp2))
print('C) {} é o produto mais barato, que custou R${} reais '.format(barato, menor))
