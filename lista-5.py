# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
pares = list()
impares = list()

while True:
        n = int(input('digite um numero para sua lista: '))
        lista.append(n)
        if n % 2 == 0:
                pares.append(n)
        else:
                impares.append(n)

        resp = str(input('voce quer continuar? S/N ').lower().strip())
        if resp != 's':
            break

print(f'Lista: {lista}')
print(f'Numeros pares: {pares}')
print(f'Numeros impares: {impares}')
