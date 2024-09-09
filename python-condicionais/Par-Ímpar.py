# programa para saber se um numero é par ou ímpar
print('Par ou ímpar?')
print('-----------------------------')
numero = int(input('Digite um numero inteiro: '))
resultado = numero % 2 # a porcentagem irá mostrar o resto da divisão de numero por 2(ou seja, mostrar se é par ou ímpar, 0 ou 1)
if resultado == 1:
    print(f'O número {numero} é ímpar')
else:
    print(f'O número {numero} é par')
print('-----------------------------')
print('fim!')
