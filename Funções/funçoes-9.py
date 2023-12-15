# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero inteiro valido. \033[m ')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuario preferiu nao digitar o numero. \033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero real valido. \033[m ')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuario preferiu nao digitar o numero. \033[m')
            return 0
        else:
            return n

n = leiaInt('Digite um numero inteiro: ')
r = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi \033[0;34m{n}\033[m e o real foi \033[0;35m{r}\033[m ')
