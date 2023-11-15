
a = [2, 3, 4, 5]
b = a # quando voce iguala duas ou mais listas, tudo que voce mudar em uma vai mudar nas outras, a nao ser que crie uma cópia
c = a[:] # C criando uma copia da lista A (e coincidentemente da lista B) que nao sera alterada se A ou B mudarem)
b[2] = 8
print(f'lista A: {a}')
print(f'lista B: {b}')
print(f'lista C: {c}')

# para criar uma lista:

valores = list()
for cont in range(0, 3):
    valores.append(int(input('digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Fim!')
