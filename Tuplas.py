#introdução a tuplas em python

lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
a = 2, 5, 4
b = 5, 8, 1, 2
c = a + b
#for cont in range(0, len(lanche)):
    #print(f'eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'eu vou comer {comida}')

print('comi afuu ')
print(sorted(lanche))
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
