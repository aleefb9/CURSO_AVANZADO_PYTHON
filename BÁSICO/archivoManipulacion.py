import os
# crear carpeta o directorio
os.makedirs("MiCarpeta")
# listar el contenido
print(os.listdir("./"))
# mostrar directorio actual
print(os.getcwd())
# mostrar tamaño de carpeta o directorio
print(os.path.getsize("MiCarpeta"))
# comprobar si es archivo
print(os.path.isfile("MiCarpeta"))
# comprobar si es directorio
print(os.path.isdir("MiCarpeta"))
# cambiar de directorio
os.chdir("MiCarpeta")
print(os.getcwd())
print(os.listdir("./"))
os.chdir("../")
print(os.getcwd())
# renombrar 
os.rename("MiCarpeta")
# borrar
os.remove(os.getcwd()+"/archico.txt")
print(os.listdir("./"))
# borrar una carpeta
os.rmdir("MiCarpeta")
os.chdir("../")
print(os.listdir("./"))