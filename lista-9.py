#  Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação correta e os seguintes itens:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = terceira = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par = par + matriz[l][c]
        if matriz[l][2]:
            terceira = terceira + matriz[l][c]
        if matriz[1][c]:
            if matriz[1][c] > maior:
                maior = matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print (f'{[matriz[l][c]]}', end='')

    print()

print(f'A) A soma dos valores pares digitados é {par}')
print(f'B) A soma dos valores da terceira coluna é {terceira}')
print(f'C) O maior valor da segunda linha é {maior}')




