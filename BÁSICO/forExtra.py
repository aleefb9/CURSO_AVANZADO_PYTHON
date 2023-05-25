# Ejemplo con strings
lista_colores = ['rojo', 'amarillo', 'verde', 'azul', 'negro']
mi_color = input('Introduce color a buscar: ')

for color in lista_colores:
    if mi_color == color:
        print('SI EXISTE EL COLOR')
        break
else: 
    print(f'No he encontrado el color {mi_color}')
        
# Ejemplo con números
rango_largo = range(1, 10000)
print(rango_largo)
for numero in rango_largo:
    print(numero)
    if numero == 5:
        print('encontrado')
        break
else:
    print('No he encontrado el numero indicado')