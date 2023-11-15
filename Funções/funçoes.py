# introduçao a funções

def mensagem(msg): # nomeando uma função bastante usada para diminuir a repetição
    print('-'*30)
    print(msg)
    print('-'*30)

# programa principal
mensagem('Curso de Python')
mensagem('Gabriel Weil')

def soma(a, b): # definindo a soma dos elementos a e b
    print(f'A soma entre {a} e {b} é igual a {(a+b)}')

# programa principal
soma(4, 5)
soma(8, 8)
soma(b=8, a=9)

print()
def contador(*num): # o '*' antes de num serve para dizer que ele vai receber parametros
    print(f'Recebi os valores {num} e são ao todo {len(num)} numeros ') # para escrever sempre o tamanho dos elementos na funçao

# programa principal
contador(2, 1, 7)
contador(1, 2, 3, 4, 5)
contador(0, 9)

print()

def dobra(lista): # para saber o dobro de cada numero da lista depois digitada
    cont = 0
    while cont < len(lista):
        lista[cont] *= 2 # ou lista[cont] * 2 = lista[cont]
        cont += 1

# programa principal
valores = [0, 1, 2, 3, 4, 5, 6]
dobra(valores)
print(valores)