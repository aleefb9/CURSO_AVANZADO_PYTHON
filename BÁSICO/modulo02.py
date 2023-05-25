# from random import randint as azar
from random import *

continua = 's'
while continua == 's' or continua == 'S':
    lanzaDado = randint(1, 6)
    print(f'Has sacado un {lanzaDado}')
    continua = input('Continuamos(s/n)')

print('Ya no tiro mas el dado, chao pescao')