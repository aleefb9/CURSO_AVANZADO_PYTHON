def suma(num1, num2):
    resultado = num1 + num2
    return resultado

num1 = int(input('Dime un número: '))
num2 = int(input('Dime otro número: '))

# llamada a la función
resultado = suma(num1, num2)
print(f'La suma es igual a {resultado}')