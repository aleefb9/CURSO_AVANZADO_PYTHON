# Función parOimpar
def esPar(numero):   
    if numero%2==0:
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} es impar')

bandera = True

# Mientras la bandera esté True, siempre se repetirá la acción
while bandera:
    numero = int(input('Dime un número y te digo si es par o impar: '))
    esPar(numero)