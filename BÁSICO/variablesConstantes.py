# Damos valor a variable
precio = 225
cantidad = 3

# Calculamos total
total = precio * cantidad
# podemos mostrar de las dos siguientes formas:
print('El precio total es de: '+str(total)) 
print(f'El precio total es de: {total}')

# borrar variables
del precio
print(cantidad)

# asignamos otros valores
precio = 25
cantidad = 21

# Calculamos total
total = precio * cantidad
print('El precio total es de: '+str(total)) 

# Las variables constantes(No cambian) se escriben en mayúsculas
PASSWORD = '1234'

# Asignamos varios valores
a,b,c,d = 1, 4, "nombre", True
print(a)
print(b)
print(c)
print(d)

# asignar mismo valor
x = y = z = 68
print(x)
print(y)
print(z)