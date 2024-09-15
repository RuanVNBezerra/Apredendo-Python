print('Programa que simula empréstimo bancário ')
print('----------------------------------------')

valor_casa = float(input('Digite o valor da casa: '))
Salario = float(input('Digite o seu salário: '))
Anos = int(input('Quantos anos você irá pagar a casa?: '))

# calcula a prestação mensal
prestação_mensal = valor_casa / (Anos * 12)
# calcula o limite do salário e ver se excede o limite de 30% 
limite_salario = Salario / 0.30

if prestação_mensal > limite_salario:  # vê e analisa se o salário for menor que a prestação, a compra será negada
    print('O valor excedeu o limite do salário, o empréstimo será negada!')
else:
    print('Compra aprovada!')  # se não, a compra será aprovada

print('----------------------------------------')    
print('fim')