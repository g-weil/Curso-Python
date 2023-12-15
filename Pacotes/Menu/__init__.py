from Pacotes.Menu.Interface import *
from Pacotes.Menu.Arquivo import *
from time import sleep

arquivo = 'pessoas.txt'

if not arqExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resp == 1:
        lerArquivo(arquivo)
    elif resp == 2:
        cabeçalho('CADASTRAR PESSOA')
        while True:
            addArquivo(arquivo, str(input('Nome: ')), str(input('Idade: ')))
            resp = str(input('Quer cadastrar mais alguem? ENTER para continuar e "sair" para parar: ')).upper().strip()
            linha()
            if resp == 'SAIR':
                cabeçalho('SAINDO...')
                break
    elif resp == 3:
        cabeçalho('Saindo do sistema... ')
        break
    else:
        print('\033[0;31mDigite um numero valido nas opções! \033[m')
    sleep(0.5)



