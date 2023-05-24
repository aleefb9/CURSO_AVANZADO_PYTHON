print('-- Bienvenidos a mi primer programa --')

# Lista de los tipos
print('Tipo entero')
print(type(23))
print('Tipo decimal')
print(type(12.32))
print('Tipo cadena')
print(type('Saludo'))
print('Tipo booleano')
print(type(False))

# Ejemplos con las cadenas
print('Hola, '+' amigos!!')
print('Saludo'*4)
variable = "Cadena en variable"
variable = "Sumo esto a "+variable
print(variable[3]) # Nos muestra la tercera posicion de la cadena empezando de 0
print(variable[-1]) # Nos muestra la primera posicion de la cadena empezando por el final
print(variable[2:5]) #Nos muestra los caracteres entre los valores indicados
print(len(variable)) # Nos cuenta la cadena con espacios en blanco incluidos
print(variable.upper()) # Todo el texto en mayúsculas
print(variable.lower()) # Todo el texto en minúsculas
print(variable.capitalize()) # Empieza en Mayúsculas

cadena = "    Esto es una      cadena con       muchos   espacios    "
print(cadena)
print(cadena.strip()) # Elimina los espacios en blanco sobrantes por detrás y por delante de la cadena

cadena2 = "esto es una cadena sin reemplazar"
print(cadena2)
print(cadena2.replace("sin reemplazar", "reemplazada")) # Reemplaza el texto seleccionado por el nuevo que escribamos