# parte 3 de listas em python

galera = [['joao', 19], ['ana', 25], ['ricardo', 20], ['gabriel', 30]]
print(galera[0][0]) # para mostrar so o primeiro elemento do primeiro elemento da lista
print(galera[3][1])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

print('')
lista = list()
dado = list()
totalmen = totalmai = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    lista.append(dado[:])
    dado.clear()

for d in lista:
    if d[1] >= 18:
        print(f'{d[0]} é maior de idade. ')
        totalmai += 1

    else:
        print(f'{d[0]} é menor de idade. ')
        totalmen += 1

print(f'{totalmai} sao maiores de idade e {totalmen} são menores ')

