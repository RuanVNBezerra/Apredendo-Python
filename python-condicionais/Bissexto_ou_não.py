from datetime import date # estou apenas accesando a ' date' para ter acesso ao ano atual
print('Saber se o ano é bissexto ou não')
print('----------------------------------')
ano = int(input('Que ano você quer analisar? Coloque "0" para saber o ano atual: '))
if ano == 0:
    ano = date.today().year #ira pegar o ano atual configurado na máquina
    print(f'Ano Atual {ano}')

elif ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'o ano {ano} é BISSEXTO!')

else:
    print(f'o ano {ano} não é BISSEXTO') 
       
print('fim')
print('----------------------------------')