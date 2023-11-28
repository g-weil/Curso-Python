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

def moeda(valor, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')



