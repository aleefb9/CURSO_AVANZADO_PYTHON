diccionario = {
    'nombre': 'Alex',
    'apellidos': 'Banda',
    'tutoriales':  ['python', 'JS', 'php']
}

print(diccionario)
print(type(diccionario))
print(diccionario['nombre'])
print(diccionario['tutoriales'])
print(diccionario['tutoriales'][1])
for clave in diccionario:
    print(clave, ":", diccionario[clave])

# Metodos de los diccionarios
persona = dict(nombre='Alex', apellidos='FB', edad=48)
print(persona)
print(type(persona))

diccionario02 = dict(zip('aeiou', [1,2,3,4,5]))
print(diccionario02)
print(type(diccionario02))

print(diccionario02.items())

print(diccionario02.keys())
print(diccionario02.values())

# diccionario02.clear()
# print(diccionario02)

copiaDiccionario = diccionario02.copy()
print(copiaDiccionario)
diccionario03 = dict.fromkeys(['a','e','i','o','u'], 34)
print(diccionario03)
print(diccionario.get('nombre'))
print(diccionario.get('amigo'))
borrado = diccionario.pop('nombre')
print(borrado)
print(diccionario)