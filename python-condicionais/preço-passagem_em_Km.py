#programa que pede uma distancia em Km, se a distancia for menor ou igual a 200Km terá uma taxa de 50 centavos por Km
#se não, tera uma taxa de 45 centavos
print('-----------------------------------')
distancia = float(input('Qual foi a distancia da viagem?: '))
print(f'você está prestes a começar uma viagem de {distancia}')
if distancia <= 200:
   preço = distancia * 0.50
else:    
   preço = distancia * 0.45
print(f'E o preço a ser pago será de {preço}')
print('fim')
print('------------------------------------')
