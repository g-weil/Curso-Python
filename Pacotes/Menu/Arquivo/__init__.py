from Pacotes.Menu.Interface import *

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo! ')

    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo! ')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
        linha()

def addArquivo(nome, pessoa='desconhecido', idade=0):
    try:
        a = open(nome, 'a')
    except:
        print('Erro ao cadastrar pessoa! ')
    else:
        a.write(f'{pessoa:<30}{idade:>7} anos\n')
        cabeçalho('USUÁRIO CADASTRADO COM SUCESSO')
