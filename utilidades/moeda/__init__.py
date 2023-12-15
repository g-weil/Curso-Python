def metade(n, format=False):
    resp = n / 2
    return resp if format == False else moeda(resp)

def dobro(n, format=False):
    resp = n * 2
    return resp if format == False else moeda(resp)

def aumentar(n, porc, format=False):
    resp = n + ((n * porc) / 100)
    return resp if format == False else moeda(resp)

def diminuir(n, porc, format=False):
     resp = n - ((n * porc) / 100)
     return resp if format == False else moeda(resp)

def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def resumo(n, aumento, reduçao):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(n)}')
    print(f'Dobro do preço: {dobro(n, True)}')
    print(f'Metade do preço: {metade(n, True)}')
    print(f'{aumento}% de aumento: {aumentar(n, aumento, True)}')
    print(f'{reduçao}% de redução: {diminuir(n, reduçao, True)}')
    print('-' * 30)
