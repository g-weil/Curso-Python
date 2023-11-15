# continuação de funções e docstrings

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s        # A instrução return encerra a execução de uma função e retorna o controle para a função de chamada.
                    # A execução é retomada na função de chamada no ponto imediatamente após a chamada.

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')
print('-'*30)
# exercicio de exemplo

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f

nro = int(input('Digite um numero: '))
print(f'O fatorial de {nro} é igual a {fatorial(nro)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
print('-'*30)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

numero = int(input('Digite um numero: '))
if par(numero):
    print('É par!')
else:
    print('Não é par!')

