# PEDIR DATOS A UN USUARIO

# Pedir string y saludar
nombre = input('Dime tu nombre: ')
print('Hola, '+nombre)
print('Hola, ', nombre)
print(f'Hola, {nombre}\n')

# Pedir dos números y sumarlos
numero1 = int(input('Dime un número: '))
numero2 = int(input('Dime un segundo numero: '))
total = numero1 + numero2
print(f'La suma de {numero1} más {numero2} es igual a: {total}')