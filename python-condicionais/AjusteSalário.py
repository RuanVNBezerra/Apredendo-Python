# programa que reajusta o salário de um funcionario
salario = int(input('Digite seu salario atual: '))
if salario <= 1250: # se o salário for menor que 1250, terá um ajuste de mais 15% de aumento
   novo_salario = salario + (salario * 15 / 100)
   print(f'o seu novo salario de {salario} sera de {novo_salario}')
else:
   novo_salario = salario + (salario * 10 / 100)  # se o salario for maior, terá um ajuste de 10%
   print(f' o seu salario de {salario} sera de {novo_salario}')   