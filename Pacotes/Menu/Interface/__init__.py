
def linha(tam = 42):
    return '-' * tam

def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def menu(lista):
        cabeçalho('MENU PYTHON')
        c = 1
        for item in lista:
            print(f'{c} - {item}')
            c += 1
        print(linha())
        opc = leiaNum('Sua opção: ')
        return opc


def leiaNum(resp):
    while True:
        try:
            n = int(input(resp))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero inteiro valido. \033[m ')
            continue
        else:
            return n