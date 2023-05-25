def guarda_texto(nombre_archivo, texto):
    fichero = open(nombre_archivo+"txt", "w")
    fichero.write(texto)
    fichero.close()
    print('Texto guardado')
    return True

def lee_texto(nombre_archivo):
    fichero = open(nombre_archivo+"txt", "r")
    texto = fichero.read()
    fichero.close()
    return texto

archivo = input('Indica el nombre del archivo: ')
texto = input('Pon aquí el texto a guardar: ')
guarda_texto(archivo, texto)
texto = lee_texto(archivo)
print(f'Este es el texto guaradado en {archivo}: {texto}')