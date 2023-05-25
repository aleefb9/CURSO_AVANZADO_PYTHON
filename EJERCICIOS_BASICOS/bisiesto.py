def bisiesto(anio):
    if anio % 4 != 0:
        return False
    if anio % 4 == 0 and anio % 100 != 0:
        return True
    if anio % 4 == 0 and anio % 100 == 0 and anio % 400!= 0:
        return False
    if anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
        return True
    
anio = int(input('INTRODUCE AÑO: '))

if bisiesto(anio):
    print('BISIESTO')
else:
    print('NO BISIESTO')