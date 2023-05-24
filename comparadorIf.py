numero1 = int(input('Dime un número: '))
numero2 = int(input('Dime un segundo numero: '))

if (numero1 > numero2):
    print(f'\nEl numero {numero1} es mayor que {numero2}')
elif (numero1 < numero2):
     print(f'\nEl numero {numero1} es menor que {numero2}')
else:
     print('Los números son iguales\n')

print('Hemos terminado de comparar')


# segundo ejemplo, edades para tarifa

edad = int(input("Dime tu edad y te indico su tarifa"))
if edad < 5:
    precio = 0
elif edad < 15:
    precio = 5
elif edad < 65:
    precio = 20
else:
    precio = 15

print("Tu tarifa para entrar es de "+str(precio))