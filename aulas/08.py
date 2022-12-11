# if else // operadores de condição

from traceback import print_tb


velocidade = 50

if velocidade > 100:
    print('Acima da velocidade permitida')
    print('Reduza agora a sua velocidade')

elif velocidade < 60:
    print('Favor dirigir acima de 60Km/h')

else:
    print('Velocidade OK')