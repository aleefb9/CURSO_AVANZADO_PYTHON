import os
# import pandas as pd

# directorio actual
directorio_actual = os.getcwd()
print(directorio_actual)
# directorio datos
directorio_datos = os.path.join(directorio_actual, "datos")
print(directorio_datos)
print('Existe el directorio')
print(os.path.exists(directorio_datos))
print('Es una carpeta o directorio?')
print(os.path.isdir(directorio_datos))

# listar archivos de datos
listado = [os.path.join(directorio_actual, item) for item in os.listdir(directorio_datos)]