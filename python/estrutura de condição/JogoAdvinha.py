from random import randint # estou acessando a biblioteca 'random' e escolhendo apenas a função 'randint' da biblioteca.
print('jogo da advinhação')
print('------------------')
numero_aleatorio = randint(1,10) # nesta linha de codigo estou fazendo q a função 'numero_aleatorio' receba um numero aleatorio de 1 a 10.
escolha = int(input('Escolha um numero de 1 a 10: '))
if escolha == numero_aleatorio: # estrutura condicional if else
    print('parabens! você acertou na mosca')  # caso o usuario acertou
else:
    print('Você errou, tente novamente!')# caso o usuario errou
print('------------------')      
print('FIM DE JOGO') # fim de jogo
