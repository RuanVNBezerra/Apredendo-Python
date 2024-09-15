# programa que pede o comprimento de lados de um triângulo e ver se os lados formam ou não um triângulo

reta1 = float(input('Digite o comprimento do primeiro lado: '))
reta2 = float(input('Digite o comprimento do segundo lado: '))
reta3 = float(input('Digite o comprimento do terceiro lado: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta3 + reta2 > reta1:
    print('as retas podem formar um triângulo!')
else:
    print('as retas não podem formar um triângulo!')