# PROGRAMA QUE PIDA EDAD A UN USUARIO Y LE DIGA SI ES ,MAYOR DE EDAD O NO

edad = int(input("¿Cuántos años tienes?\n"))

if edad >= 18:
    print(f'TIENES {edad} AÑOS: ERES MAYOR DE EDAD')
else:
    print(f'TIENES {edad} AÑOS: ERES MENOR DE EDAD')