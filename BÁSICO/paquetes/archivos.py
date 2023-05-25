# guardar datos en archivos
# arbimos el archivo
escritura = open("archivos.txt", "w")
escritura.write("Esto se escribe en el archivo \ny esto en la linea siguiente \n\t\t\tY esto en otro linea tabulando")
escritura.close()

# lectura de fichero
lectura = open("archivos.txt", "r")
# leemos una línea
leeLinea = lectura.readline()
print(leeLinea)
lectura.close()
#leemos todo el fichero
lectura = open("archivos.txt", "r")
leetoto = lectura.read()
print(leetoto)
lectura.close()