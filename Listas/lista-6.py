#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#  Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('digite uma expressao numerica: '))
cont1 = 0
cont2 = 0

for simb in expr:
    if simb == '(':
        cont1 += 1
    elif simb == ')':
        cont2 += 1

if cont1 == cont2:
    print('essa expressao é valida! ')

else:
    print('essa expressao é invalida! ')





