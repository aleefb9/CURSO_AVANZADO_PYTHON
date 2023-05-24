def menu():
    print('1. SUMAR')
    print('2. RESTAR')
    print('3. MULTIPLICAR')
    print('4. DIVIDIR')
    print('0. SALIR')

    opcion = int(input("?__"))
    return opcion

def solicitarDatos():
    num1 = int(input('Primer numero: '))
    num2 = int(input('Segundo numero: '))
    return num1, num2

def operacion(operador, num1, num2):
    if operador == "suma":
        resultado = num1 + num2
    elif operador == "resta":
        resultado = num1 - num2
    elif operador == "multiplica":
        resultado = num1 * num2
    elif operador == "divide":
        resultado = num1 / num2
    return resultado

while True: 
    opcion = menu()
    if opcion == 1:
        num1, num2 = solicitarDatos()
        print(f'El resultado de {num1} + {num2} es = ')
        print(operacion('suma', num1, num2))
    elif opcion == 2:
        num1, num2 = solicitarDatos()
        print(f'El resultado de {num1} - {num2} es = ')
        print(operacion('resta', num1, num2))
    elif opcion == 3:
        num1, num2 = solicitarDatos()
        print(f'El resultado de {num1} * {num2} es = ')
        print(operacion('multiplica', num1, num2))
    elif opcion == 4:
        num1, num2 = solicitarDatos()
        print(f'El resultado de {num1} / {num2} es = ')
        print(operacion('divide', num1, num2))
    elif opcion == 0:
        break
    else:
        print('Introduce una opción válida')
    print('\n')
print("Salimos")