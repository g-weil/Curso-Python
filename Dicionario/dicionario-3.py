# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = dict()
print('Cadastro do funcionario: ')
dados['Nome'] = str(input('Qual o nome? '))
ano_nasc = int(input('Qual o ano de nascimento? '))
idade = datetime.now().year - ano_nasc
dados['Idade'] = idade
dados['ctps'] = int(input('Qual o numero da carteira de trabalho? (0 se não possuir) '))

if dados['ctps'] != 0:
    dados['Ano de contratação'] = int(input('Qual o ano de contratação? '))
    dados['Salario'] = float(input('Qual o salario? '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - datetime.now().year)

for c, d in dados.items():
    print(f'{c}: {d}')


