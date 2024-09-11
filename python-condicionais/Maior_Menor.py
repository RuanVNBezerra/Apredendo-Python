print('saber qual numero é maior e menor')
print('------------------------------------')
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero:'))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor digitado foi {menor}')    

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print(f'O maior valor digitado foi {maior}')
print('fim')
print('--------------------------------------')
