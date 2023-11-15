#introdução a listas

num = [2, 5, 9, 1]

num[2] = 3 # substituir o elemento
num.append(7) # adicionar um elemento no final
num.sort() # ordem numerica ou alfabetica
sorted(num) # outra forma de colocar em ordem
num.sort(reverse=True) # ordem numerica ou alfabetica ao contrario
num.insert(2, 0) # inserir valores, primeiro a posição e depois o elemento que deseja inserir (no caso, foi inserido o elemento 0 na posição 2
# e os outros elementos foram pra frente e trocaram de posição)
num.pop(2) # deletar o elemento na posição desejada
num.remove(1) # deleta o elemento desejado (na sua primeira ocorrencia na lista)
if 4 in num: # no caso de não ter certeza se o elemento esta na lista
    num.remove(4)
else:
    print('não foi encontrado o numero 4 ')

print(num)
for c, v in enumerate(num): # para mostrar de outro jeito mais organizado
    print(f'Na posição {c} encontrei o valor {v}')
print(f'Essa lista tem {len(num)} elementos')