# funcion map
lista = [23,56,7,2,6,9,18,21,75,65]
print(list(map((lambda valor: valor * valor), lista))) # los eleva al cuadrado

# funcion filter
print(list(filter((lambda valor: valor%2==0), lista))) # saca los números pares

# funcion reduce
import functools
print(str(functools.reduce((lambda x, resultado: x + resultado), lista))) #suma toda la lista

