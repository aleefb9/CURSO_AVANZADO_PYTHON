# Tabla de multiplicar

tabla = int(input("¿Qué tabla quieres calcular? "))
# Creamos una variable contador 
contador = 1
print(f'Tabla del {tabla}')

# Repetición
while (contador<11):
    resultado = tabla * contador
    # Incrementamos el contadr
    contador = contador + 1
    # Mostramos la tabla
    print(f'{tabla} * {contador - 1} = {resultado}')

print('\nFin de la tabla')