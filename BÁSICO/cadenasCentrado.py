texto = "Esto es un texto para el ejemplo que vamos a realizar"
print("La cadena empieza con: ", texto.startswith("Esto"))
print("La cadena acaba con: ", texto.startswith("realizar"))

# alinear texto
# centrado
print(texto.center(80, '/'))
longitudCadena = len(texto)
print(longitudCadena)
print(texto.center(longitudCadena+7, '-'))

# Poner caracteres a la izquierda o derecha de nuestra cadena
print(texto.ljust(80, '-'))
print(texto.rjust(80, '-'))