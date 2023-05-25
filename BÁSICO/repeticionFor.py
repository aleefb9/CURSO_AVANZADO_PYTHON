# Tabla de multiplicar con FOR
tabla = int(input("¿Qué tabla quieres calcular? "))
print(f'Tabla del {tabla}')

for contador in range(1,11):
    resultado = contador * tabla
    print(f'{tabla} * {contador} = {resultado}')

print('\nFin de la tabla\n')

# Ejemplo for con lista
nombres = ['Jose', 'Alejandro', 'Antonio', 'Lucia']
for nombre in nombres:
    print(f'Hola, {nombre}\n')

# mostrar 100 números
for numero in range(1, 101):
    print(numero)