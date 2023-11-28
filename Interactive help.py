# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep

# Tabela de cores:

c = ('\033[m', # 0 - sem cor
     '\033[0;31m', # 1 - vermelho
     '\033[0;32m', # 2 - verde
     '\033[0;33m', # 3 - amarelo
     '\033[0;34m', # 4 - azul
     '\033[0;35m', # 5 - roxo
     '\033[0;36m', # 6 - branco
     );
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'...', 4)
    help(com)
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~'*tam)
    print(f'{msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# programa principal

comando = ''
while True:
    titulo('SISTEMA DE AJUDA NO PYTHON', 1)
    comando = str(input('Função ou Biblioteca > ' ))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('FIM!', 5)
