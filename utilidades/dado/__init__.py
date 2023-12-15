def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha():
            print(f'\033[0;31mERRO! "{n}" é um preço invalido. \033[m ')
        else:
            valor = float(n)
            ok = True
        if ok:
            break
    return float(valor)

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero valido. \033[m ')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero \033[0;34m{n}\033[m ')

