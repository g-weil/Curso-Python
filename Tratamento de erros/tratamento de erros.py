try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('tivemos um problema com os tipos de dados inseridos ')

except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero ')

except Exception as erro:
    print(f'o erro encontrado foi {erro.__cause__}')

else:
    print(f'o resultado é {r}')

finally:
    print('Volte sempre!  ')

# modifique o exercicio 9 de funçoes com o tratamento de erros
