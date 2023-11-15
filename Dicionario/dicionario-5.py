# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = dict()
lista = list()
cont = total = 0
print('Cadastro de pessoas: ')
while True:
    pessoas['Nome'] = str(input('Nome: '))
    while True:
        pessoas['Sexo'] = str(input('Sexo: (M para masculino e F para feminino) ')).upper().strip()
        if pessoas['Sexo'] in 'MF':
            break
        print('Opção inválida! Digite apenas m ou f ')
    pessoas['Idade'] = int(input('Idade: '))
    cont += 1
    total = (pessoas['Idade'] + total)
    lista.append(pessoas.copy())
    resp = str(input('Quer continuar cadastrando? digite S para continuar ')).strip().upper()
    if resp != 'S':
        break

media = total / cont
print(f'A) Foram cadastradas {cont} pessoas ')
print(f'B) A media de idade das pessoas cadastradas é de {media:.2f} anos ')
print('C) As mulheres cadastradas são: ')
for p in lista:
    if p['Sexo'] == 'F':
        print([p['Nome']], end=' ')
print()
print('D) Lista de pessoas com idade acima da média: ')
for p in lista:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{k}: {v}; ', end=' ')
        print()