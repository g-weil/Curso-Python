# dicionário em python

pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas.keys()) # mostra as chaves
print(pessoas.values()) # mostra os valores das chaves
print(pessoas.items()) # mostra todos os itens

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

from operator import itemgetter
key=itemgetter(1) # para ordenar lista de dicionários

pessoas['nome'] = 'gabriel' # para trocar um valor
pessoas['peso'] = 78.5 # ou add um novo valor

for k, v in pessoas.items(): # para enumerar os itens e mostrar em ordem
    print(f'{k} = {v}')

# para criar dicionarios e colocar dentro de uma lista:
brazil = []
estado1 = {'UF': 'Rio Grande do Sul', 'sigla': 'RS'}
estado2 = {'UF': 'Santa Catarina', 'sigla': 'SC'}
brazil.append(estado1)
brazil.append(estado2)
print(brazil[0]['UF'])


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # para criar uma copia de um estado e pode registrar todos os itens

for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')

