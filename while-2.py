# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

n = 'S'
cont = contm = contf = 0
while n == 'S':
    idade = int(input("digite a idade: "))
    sexo = str(input("digite o genero, [M] para Masculino e [F] para Feminino: ")).upper()

    if idade > 18:
        cont = cont + 1
    if sexo == 'M':
        contm = contm + 1
    if idade < 20 and sexo == 'F':
        contf = contf + 1

    n = str(input("quer cadastrar mais alguma pessoa? [S/N] ")).upper()

    if n == 'N':
        break
    if n != 'N' and n != 'S':
        n = str(input('resposta invalida! voce deve responder [S] ou [N]: ')).upper()

print('A) {} pessoas são maiores de 18 anos '.format(cont))
print('B) {} homens foram cadastrados '.format(contm))
print('C) {} mulheres tem menos de 20 anos '.format(contf))