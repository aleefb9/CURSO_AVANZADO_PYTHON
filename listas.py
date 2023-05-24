lista = [1,2.3,'Alex',[7,8],12]
print(type(lista))
print(lista)

print(lista[2])
print(lista[3][1])
print(lista[1:4])
print(lista[2:4:2])

for elemento in lista:
    print(elemento)

lista.append(10)
lista.append('Lucia')
lista.append([2,3,4,5])
print(lista)

lista.extend([4,5,2,4])
print(lista)

lista.remove('Lucia')
print(lista)

print(lista.index('Alex'))
print(lista.count(15))

lista.reverse()
print(lista)

listaCompra = ['pan', 'patatas', 'naranjas', 'kiwis']
print(listaCompra)
print(type(listaCompra))

# crear una lista de variables
cantidadPan = 5
precioPan = 0.40
total = cantidadPan * precioPan
pedido = [cantidadPan, precioPan, total]
print(pedido)

# ejemplo añadir con bucle for
cuadrados = []
for numero in range(1, 11):
    cuadrados.append(numero*numero)
print(cuadrados)
print(min(cuadrados))
print(max(cuadrados))
print(sum(cuadrados))
