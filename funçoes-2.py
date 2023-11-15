# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(msg): # nomeando uma função bastante usada para diminuir a repetição
    print('-'*30)
    print(msg)
    print('-'*30)

# programa principal
escreva('Curso de Python')
escreva('Gabriel Weil')
escreva('Ola, mundo! ')