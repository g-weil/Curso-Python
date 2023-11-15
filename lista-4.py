# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()

while True:
        n = int(input('digite um numero para sua lista: '))
        lista.append(n)
        resp = str(input('voce quer continuar? S/N ').lower().strip())
        if resp != 's':
            break

print(f'Lista: {lista}')
print(f'A) Foram digitados {len(lista)} numeros ')
lista.sort(reverse=True)
print(f'B) Ordem decrescente: {lista}')
if 5 in lista:
    print(f'C) O valor 5 foi digitado e esta na lista ')
else:
    print(f'C) O valor 5 não foi encontrado ')