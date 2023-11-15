# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()

while True:
        n = int(input('digite um numero para sua lista: '))
        if n not in lista:
            lista.append(n)
            resp = str(input('voce quer continuar? S/N ').lower().strip())
            if resp != 's':
                break

        else:
            print('valor duplicado, não será adicionado ')

print(sorted(lista))