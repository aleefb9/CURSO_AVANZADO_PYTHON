lista_colores = input('Escribe un nuevo color a añadir: ')
lista_colores = set(lista_colores.split(","))

colores = []

for color in lista_colores:
    colores.append(color)

colores.sort()
print(colores)