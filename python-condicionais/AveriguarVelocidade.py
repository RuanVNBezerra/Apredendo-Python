#programa que pergunta qual a velocidade atual do dono do carro e averigua se o carro excedeu a velocidade ou não
#caso excedeu, recebera uma multa de 7 reais para cada kilometro andado acima dos 80 kilometros
velocidade = float(input('Qual a velocidade do seu carro? '))
if velocidade > 80:
    print('ALTA VELOCIDADE!! você excedeu o limite de velocidade!')
    multa = (velocidade- 80) * 7
    print(f'Você sera multado em {multa} R$')
else:
    print('Tenha um bom dia e derija com segurança!')