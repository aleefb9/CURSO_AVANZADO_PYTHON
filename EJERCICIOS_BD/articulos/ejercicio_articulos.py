import sqlite3
import sys

# MÉTODO QUE CREA CONEXIÓN CON LA BASE DE DATOS
def conectar():
    conexion = sqlite3.connect("EJERCICIOS_BD/articulos/articulosBD.db") #realiza la conexión
    cursor = conexion.cursor() 
    return conexion, cursor

# MÉTODO QUE CIERRA LA CONEXIÓN CON LA BASE DE DATOS
def cerrar_conexion(conexion):
    conexion.close()

# MÉTODO QUE CREA LA TABLA ARTÍCULOS
def crearTabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS articulos(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(20) NOT NULL,
            cantidad INT NOT NULL,
            importe FLOAT NOT NULL
        )
    """
    if (cursor.execute(sql)):
        print("Tabla creada")
    else: 
        print("No se pudo crear la tabla")
    cerrar_conexion(conexion)

# MÉTODO QUE NOS CARGA EL MENÚ Y NOS DIRIGE A LA OPCIÓN SELECCIONADA
def menu():
    print("\nINDIQUE QUE ACCIÓN DESEA REALIZAR")
    print("1. Alta")
    print("2. Listar")
    print("3. Modificacion")
    print("4. Borrado")
    print("0. Salir")

    opcion = input('--> ')
    if opcion not in ['1','2','3','4','0']:
        print('\n********* Selecciona una opcion valida *********\n')
    else:
        if opcion == '1':
            anadir_datos()
        if opcion == '2':
            listar_datos()
        if opcion == '3':
            modificar_datos()
        if opcion == '4':
            eliminar_datos()
        if opcion == '0':
            print('HASTA PRONTO !!')
            sys.exit()   

# MÉTODO QUE AÑADE DATOS A LA BASE DE DATOS
def anadir_datos():
    conexion, cursor = conectar()

    nombre = input("\nINSERTA NOMBRE: ")
    cantidad = input("INSERTA CANTIDAD: ")
    importe = input("INSERTA IMPORTE: ")
    datos = (nombre, cantidad, importe)

    sql = """INSERT INTO articulos(nombre, cantidad, importe) VALUES (?, ?, ?)"""
    if(cursor.execute(sql, datos)):
        print('\n --- Datos guardados ---')
    else:
        print('*** No se pudieron guardar los datos ***')

    conexion.commit()
    conexion.close()
    menu()

# MÉTODO QUE LISTA LOS DATOS DE LA BASE DE DATOS
def listar_datos():
    conexion, cursor = conectar()
    sql = "SELECT * FROM articulos"
    cursor.execute(sql)
    for fila in cursor:
        print("\n")
        print("*"*25)
        print(f"ID = {fila[0]}")
        print(f"NOMBRE = {fila[1]}")
        print(f"CANTIDAD = {fila[2]}")
        print(f"IMPORTE = {fila[3]}€")
        print("*"*25)

    conexion.close()
    menu()


def seleccionarId():
    conexion, cursor = conectar()
    idSeleccioando = input("\nINSERTA ID DEL ARTÍCULO QUE QUIERAS MODIFICAR: ")

    seleccionar = "SELECT * FROM articulos WHERE id="+idSeleccioando
    cursor.execute(seleccionar)

    for fila in cursor:
        print("\n")
        print("*"*25)
        print(f"ID = {fila[0]}")
        print(f"NOMBRE = {fila[1]}")
        print(f"CANTIDAD = {fila[2]}")
        print(f"IMPORTE = {fila[3]}€")
        print("*"*25)

    nombre = input("\nINSERTA NUEVO NOMBRE: ")
    cantidad = input("INSERTA NUEVO CANTIDAD: ")
    importe = input("INSERTA NUEVO IMPORTE: ")

    conexion.close()
    return nombre,cantidad,importe,idSeleccioando
    

# MÉTODO QUE MODIFICA LOS DATOS DE LA BASE DE DATOS
def modificar_datos():
    conexion, cursor = conectar()

    nombre,cantidad,importe,idSeleccioando = seleccionarId()

    sql = "UPDATE articulos SET NOMBRE='"+nombre+"',CANTIDAD='"+cantidad+"',IMPORTE='"+importe+"' WHERE ID='"+idSeleccioando+"'"
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
    menu()

# MÉTODO QUE ELIMINA LOS DATOS DE LA BASE DE DATOS
def eliminar_datos():
    conexion, cursor = conectar()

    idSeleccioando = input("\nINSERTA ID DEL ARTÍCULO QUE QUIERAS MODIFICAR: ")
    sql = "DELETE FROM articulos WHERE ID="+idSeleccioando
    if(cursor.execute(sql)):
        print(f'Se ha eliminado correctamente el articulo con id: {idSeleccioando}')
    else:
        print(f'Error al borrar el id: {idSeleccioando}')

    conexion.commit()
    conexion.close()
    menu()



if __name__ == '__main__':
    crearTabla()
    menu()