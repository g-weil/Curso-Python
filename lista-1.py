# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num = list()
for cont in range(0, 5):
    num.append(int(input('digite um valor: ')))

print(f'Lista: {num}')
print(f'O maior numero é {max(num)} e está na posição {num.index(max(num))+1}')
print(f'O maior numero é {min(num)} e está na posição {num.index(min(num))+1}')
