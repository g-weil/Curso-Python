#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.

valores = int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: '))

print(f'valores: {valores}')

print(f'A) o numero 9 apareceu {valores.count(9)} vez/vezes ')

if 3 in valores:
    print(f'B) o primeiro numero 3 foi digitado na posição {valores.index(3)+1}')
else:
    print('B) o numero 3 não está presente na tupla de valores ')

print('C) os numeros pares são: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')

